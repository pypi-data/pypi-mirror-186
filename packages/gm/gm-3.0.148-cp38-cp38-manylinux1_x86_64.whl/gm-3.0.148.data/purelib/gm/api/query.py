# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

import json
import traceback
import zlib
from typing import Any, Text, List, Dict, Optional
from datetime import datetime as Datetime, date as Date

import grpc
import pandas as pd
import six

from gm import utils
from gm.constant import DATA_TYPE_TICK
from gm.csdk.c_sdk import py_gmi_history_ticks_l2, c_status_fail, py_gmi_history_bars_l2, \
    py_gmi_history_transaction_l2, py_gmi_history_order_l2, py_gmi_history_order_queue_l2,\
    py_gmi_raw_func
from gm.enum import ADJUST_NONE
from gm.model.fundamental import FundamentalApi
from gm.model.history import HistoryApi
from gm.pb.data_pb2 import Ticks, Bars, L2Transactions, L2Orders, L2OrderQueues
# history 和 history level2 拆分成不同的proto文件进行重新定义了。这里不能直接用这样的路径引入.
# from gm.pb.history_pb2 import GetHistoryL2TicksReq, GetHistoryL2BarsReq, GetHistoryL2TransactionsReq
from gm.pb.history_l2_pb2 import GetHistoryL2TicksReq, GetHistoryL2BarsReq, GetHistoryL2TransactionsReq, GetHistoryL2OrdersReq, GetHistoryL2OrderQueuesReq
from gm.pb.trade_rawfunc_service_pb2 import RawFuncReq, RawFuncRsp
from gm.pb_to_dict import protobuf_to_dict
from gm.retrying import retry
from gm.utils import load_to_datetime_str, standard_fields, gmsdklogger

fundamentalapi = FundamentalApi()
historyapi = HistoryApi()

# 兼容 Pandas 1.4.0 版本, 之前的不做改动防止出错
try:
    _pd_version = pd.__version__.split(".")
    if int(_pd_version[0]) >= 1 and int(_pd_version[1]) >= 4:
        pd.set_option('display.precision', 4)
    else:
        pd.set_option('precision', 4)
except:
    pd.set_option('precision', 4)


def reset_historyapi():
    historyapi.reset_addr()


def reset_fundamentalapi():
    fundamentalapi.reset_addr()


def condune_error(func):
    """
    网络调用尝试三次
    """

    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except grpc.RpcError as e:
            func_name = func.__name__
            details_fun = getattr(e, 'details', None)
            code_fun = getattr(e, 'code', None)
            if callable(details_fun) and callable(code_fun):
                detailsstr = details_fun()
                code = code_fun()
                if code is grpc.StatusCode.RESOURCE_EXHAUSTED and 'extract' in detailsstr:
                    exc_msg = traceback.format_exc()
                    gmsdklogger.warn(
                        "你今天的数据限额已用完,请联系商务提高数据限额.返回空数据给你. api[%s]", func_name)
                    # 这个会记录到日志文件里
                    gmsdklogger.debug("你今天的数据限额已用完,请联系商务提高数据限额.返回空数据给你. api[%s] 返回的详细信息:%s\n 执行堆栈信息:%s", func_name, e,
                                      exc_msg)
                elif code is grpc.StatusCode.OUT_OF_RANGE and 'outofrange' in detailsstr:
                    exc_msg = traceback.format_exc()
                    params = []
                    params.extend(args)
                    for k, v in six.iteritems(kw):
                        params.append('{}={}'.format(k, v))
                    gmsdklogger.warn(
                        "%s. 返回空数据给你. api[%s] param=%s", detailsstr, func_name, params)
                    # 这个会记录到日志文件里
                    gmsdklogger.debug("%s. 返回空数据给你. api[%s] param=%s 返回的详细信息:%s\n 执行堆栈信息:%s", detailsstr, func_name,
                                      params, e, exc_msg)
                elif 'header' in detailsstr and 'http2' in detailsstr and '429' in detailsstr:
                    exc_msg = traceback.format_exc()
                    gmsdklogger.warn(
                        "你调用api[%s]的速度太快了, 服务器对你做限流了.返回空数据给你", func_name)
                    # 这个会记录到日志文件里
                    gmsdklogger.debug(
                        "你调用api[%s]的速度太快了. 返回空数据 返回的详细信息:%s\n 执行堆栈信息:%s", func_name, e, exc_msg)
                else:
                    gmsdklogger.exception(e)

                dfval = kw.get('df', None)
                if dfval:  # df 参数为true
                    return pd.DataFrame([])
                else:
                    # 这两个函数比较特殊
                    if func_name in {'get_previous_trading_date', 'get_next_trading_date', }:
                        return ""
                    return []

        except Exception as e:
            func_name = func.__name__
            gmsdklogger.exception(e)
            dfval = kw.get('df', None)
            if dfval:  # df 参数为true
                return pd.DataFrame([])
            else:
                if func_name in {'get_previous_trading_date', 'get_next_trading_date', }:  # 这两个函数比较特殊
                    return ""
                return []

    return wrapper


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_fundamentals(table, symbols, start_date, end_date, fields=None,
                     filter=None, order_by=None, limit=1000, df=False):
    """
    查询基本面财务数据
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=True)
    start_date = utils.to_datestr(start_date)
    end_date = utils.to_datestr(end_date)
    data = fundamentalapi.get_fundamentals(table=table, symbols=symbols,
                                           start_date=start_date,
                                           end_date=end_date, fields=fields_str,
                                           filter=filter, order_by=order_by,
                                           limit=limit)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            fields_list = ['symbol', 'pub_date', 'end_date'] + fields_list
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_fundamentals_n(table, symbols, end_date, fields=None, filter=None,
                       order_by=None, count=1, df=False):
    """
    查询基本面财务数据,每个股票在end_date的前n条
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=True)
    data = fundamentalapi.get_fundamentals_n(table=table, symbols=symbols,
                                             end_date=end_date,
                                             fields=fields_str,
                                             filter=filter, order_by=order_by,
                                             count=count)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            fields_list = ['symbol', 'pub_date', 'end_date'] + fields_list
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_instruments(symbols=None, exchanges=None, sec_types=None, names=None,
                    skip_suspended=True, skip_st=True, fields=None, df=False):
    """
    查询最新交易标的信息,有基本数据及最新日频数据
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)
    data = fundamentalapi.get_instruments(symbols, exchanges, sec_types, names,
                                          skip_suspended, skip_st, fields_str)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_history_instruments(symbols, fields="", start_date="", end_date="", df=False):
    # type: (str, str, str, str, bool) -> List[Dict] | pd.DataFrame
    """
    返回指定的symbols的标的日指标数据
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)

    data = fundamentalapi.get_history_instruments(
        symbols, fields_str, start_date, end_date)

    if df:
        data = pd.DataFrame(data)
    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_instrumentinfos(symbols=None, exchanges=None, sec_types=None,
                        names=None, fields=None, df=False):
    """
    查询交易标的基本信息
    如果没有数据的话,返回空列表. 有的话, 返回list[dict]这样的列表. 其中 listed_date, delisted_date 为 datetime 类型
    @:param fields: 可以是 'symbol, sec_type' 这样的字符串, 也可以是 ['symbol', 'sec_type'] 这样的字符list
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)
    data = fundamentalapi.get_instrumentinfos(symbols, exchanges, sec_types,
                                              names, fields)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_constituents(index, fields=None, df=False):
    """
    查询指数最新成分股
    返回的list每项是个字典,包含的key值有:
    symbol 股票symbol
    weight 权重
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)
    data = fundamentalapi.get_constituents(index, fields, df)
    if df:
        data = pd.DataFrame(data)
        if fields_list:
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_history_constituents(index, start_date=None, end_date=None):
    """
    查询指数历史成分股
    返回的list每项是个字典,包含的key值有:
    trade_date: 交易日期(datetime类型)
    constituents: 一个字典. 每个股票的sybol做为key值, weight做为value值
    """
    return fundamentalapi.get_history_constituents(index, start_date, end_date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_sector(code):
    """
    查询板块股票列表
    """
    return fundamentalapi.get_sector(code)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_industry(code):
    """
    查询行业股票列表
    """
    return fundamentalapi.get_industry(code)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_concept(code):
    """
    查询概念股票列表
    """

    return fundamentalapi.get_concept(code)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_trading_dates(exchange, start_date, end_date):
    """
    查询交易日列表
    如果指定的市场不存在, 返回空列表. 有值的话,返回 yyyy-mm-dd 格式的列表
    """
    return fundamentalapi.get_trading_dates(exchange, start_date, end_date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_previous_trading_date(exchange, date):
    """
    返回指定日期的上一个交易日
    @:param exchange: 交易市场
    @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
    @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
    """
    return fundamentalapi.get_previous_trading_date(exchange, date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_next_trading_date(exchange, date):
    """
    返回指定日期的下一个交易日
    @:param exchange: 交易市场
    @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
    @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
    """
    return fundamentalapi.get_next_trading_date(exchange, date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_dividend(symbol, start_date, end_date=None, df=False):
    """
    查询分红送配
    """
    data = fundamentalapi.get_dividend(symbol, start_date, end_date)

    if df:
        data = pd.DataFrame(data)

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=3)
def get_continuous_contracts(csymbol, start_date=None, end_date=None):
    """
    获取连续合约
    """
    return fundamentalapi.get_continuous_contracts(csymbol, start_date,
                                                   end_date)


@condune_error
@retry(pre_func=reset_historyapi, stop_max_attempt_number=3)
def history(symbol, frequency, start_time, end_time, fields=None,
            skip_suspended=True, fill_missing=None, adjust=None,
            adjust_end_time='', df=False):
    """
    查询历史行情
    """
    start_time = load_to_datetime_str(start_time)
    end_time = load_to_datetime_str(end_time)
    adjust_end_time = load_to_datetime_str(adjust_end_time)
    frequency = frequency.strip()

    # 如果是列表，组合成字符串
    if isinstance(symbol, list):
        symbol = ",".join(symbol)

    symbol = symbol.strip()

    if frequency == DATA_TYPE_TICK:
        return historyapi.get_history_ticks(symbols=symbol,
                                            start_time=start_time,
                                            end_time=end_time, fields=fields,
                                            skip_suspended=skip_suspended,
                                            fill_missing=fill_missing,
                                            adjust=adjust,
                                            adjust_end_time=adjust_end_time,
                                            df=df)

    else:
        return historyapi.get_history_bars(symbols=symbol, frequency=frequency,
                                           start_time=start_time,
                                           end_time=end_time, fields=fields,
                                           skip_suspended=skip_suspended,
                                           fill_missing=fill_missing,
                                           adjust=adjust,
                                           adjust_end_time=adjust_end_time,
                                           df=df)


@condune_error
@retry(pre_func=reset_historyapi, stop_max_attempt_number=3)
def history_n(symbol, frequency, count, end_time=None, fields=None,
              skip_suspended=True, fill_missing=None, adjust=None,
              adjust_end_time='', df=False):
    """
    查询历史行情
    """
    end_time = load_to_datetime_str(end_time)
    adjust_end_time = load_to_datetime_str(adjust_end_time)
    symbol = symbol.strip()
    frequency = frequency.strip()

    if frequency == DATA_TYPE_TICK:
        return historyapi.get_history_n_ticks(symbol=symbol, count=count,
                                              end_time=end_time, fields=fields,
                                              skip_suspended=skip_suspended,
                                              fill_missing=fill_missing,
                                              adjust=adjust,
                                              adjust_end_time=adjust_end_time,
                                              df=df)

    else:
        return historyapi.get_history_n_bars(symbol=symbol, frequency=frequency,
                                             count=count, end_time=end_time,
                                             fields=fields,
                                             skip_suspended=skip_suspended,
                                             fill_missing=fill_missing,
                                             adjust=adjust,
                                             adjust_end_time=adjust_end_time,
                                             df=df)


def get_history_ticks_l2(symbols, start_time, end_time, fields=None,
                         skip_suspended=True, fill_missing=None,
                         adjust=ADJUST_NONE, adjust_end_time='', df=False):
    gmsdklogger.warning("请使用 get_history_l2ticks 查询数据")
    return get_history_l2ticks(symbols, start_time, end_time, fields,
                               skip_suspended, fill_missing,
                               adjust, adjust_end_time, df)


def get_history_l2ticks(symbols, start_time, end_time, fields=None,
                        skip_suspended=True, fill_missing=None,
                        adjust=ADJUST_NONE, adjust_end_time='', df=False):
    req = GetHistoryL2TicksReq(symbols=symbols, start_time=start_time, end_time=end_time, fields=fields,
                               skip_suspended=skip_suspended, fill_missing=fill_missing, adjust=adjust,
                               adjust_end_time=adjust_end_time)

    req = req.SerializeToString()
    status, result = py_gmi_history_ticks_l2(req)
    if c_status_fail(status, 'py_gmi_history_ticks_l2') or not result:
        return [] if not df else pd.DataFrame([])

    res = Ticks()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(
        tick, is_utc_time=True, including_default_value_fields=True) for tick in res.data]
    return datas if not df else pd.DataFrame(datas)


def get_history_bars_l2(symbols, frequency, start_time, end_time, fields=None,
                        skip_suspended=True, fill_missing=None,
                        adjust=ADJUST_NONE, adjust_end_time='', df=False):
    gmsdklogger.warning("请使用 get_history_l2bars 查询数据")
    return get_history_l2bars(symbols, frequency, start_time, end_time, fields,
                              skip_suspended, fill_missing,
                              adjust, adjust_end_time, df)


def get_history_l2bars(symbols, frequency, start_time, end_time, fields=None,
                       skip_suspended=True, fill_missing=None,
                       adjust=ADJUST_NONE, adjust_end_time='', df=False):
    req = GetHistoryL2BarsReq(symbols=symbols, frequency=frequency, start_time=start_time, end_time=end_time,
                              fields=fields,
                              skip_suspended=skip_suspended, fill_missing=fill_missing, adjust=adjust,
                              adjust_end_time=adjust_end_time)

    req = req.SerializeToString()
    status, result = py_gmi_history_bars_l2(req)
    if c_status_fail(status, 'py_gmi_history_bars_l2') or not result:
        return [] if not df else pd.DataFrame([])

    res = Bars()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(
        bar, is_utc_time=True, including_default_value_fields=True) for bar in res.data]
    return datas if not df else pd.DataFrame(datas)


def get_history_transaction_l2(symbols, start_time, end_time, fields=None, df=False):
    gmsdklogger.warning("请使用 get_history_l2transactions 查询数据")
    return get_history_l2transactions(symbols, start_time, end_time, fields, df)


def get_history_l2transactions(symbols, start_time, end_time, fields=None, df=False):
    req = GetHistoryL2TransactionsReq(
        symbols=symbols, start_time=start_time, end_time=end_time, fields=fields)
    req = req.SerializeToString()
    status, result = py_gmi_history_transaction_l2(req)
    if c_status_fail(status, 'py_gmi_history_transaction_l2') or not result:
        return [] if not df else pd.DataFrame([])

    res = L2Transactions()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(
        trans, is_utc_time=True, including_default_value_fields=True) for trans in res.data]
    return datas if not df else pd.DataFrame(datas)


def get_history_l2orders(symbols, start_time, end_time, fields=None, df=False):
    req = GetHistoryL2OrdersReq(
        symbols=symbols, start_time=start_time, end_time=end_time, fields=fields)
    req = req.SerializeToString()
    status, result = py_gmi_history_order_l2(req)
    if c_status_fail(status, 'py_gmi_history_order_l2') or not result:
        return [] if not df else pd.DataFrame([])

    res = L2Orders()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(
        item, is_utc_time=True, including_default_value_fields=True) for item in res.data]
    return datas if not df else pd.DataFrame(datas)


def get_history_l2orders_queue(symbols, start_time, end_time, fields=None, df=False):
    req = GetHistoryL2OrderQueuesReq(
        symbols=symbols, start_time=start_time, end_time=end_time, fields=fields)
    req = req.SerializeToString()
    status, result = py_gmi_history_order_queue_l2(req)
    if c_status_fail(status, 'py_gmi_history_order_queue_l2') or not result:
        return [] if not df else pd.DataFrame([])

    res = L2OrderQueues()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(
        item, is_utc_time=True, including_default_value_fields=True) for item in res.data]
    return datas if not df else pd.DataFrame(datas)


def raw_func(account_id, func_id, func_args):
    # type: (Text, Text, Dict) -> Dict
    """
    功能码调用
    :param account_id:  资金账户id
    :param func_id:     功能码id
    :param func_args:   功能码参数
    :return:
    """
    func_args = bytes(json.dumps(func_args), encoding='utf8')

    req = RawFuncReq(account_id=account_id,
                     func_id=func_id, func_args=func_args)
    req = req.SerializeToString()
    status, result = py_gmi_raw_func(req)
    if c_status_fail(status, 'py_gmi_raw_func') or not result:
        return None

    res = RawFuncRsp()
    res.ParseFromString(result)
    res = protobuf_to_dict(res)
    data = res.get("data", None)
    if data is not None:
        # 为了减少数据传输，data使用了zlib压缩，所以这里要用zlib解压一下
        return {'data': json.loads(zlib.decompress(data).decode('utf-8'))}
    return {"error": res.get("error")}


def get_varietyinfos(variety_names="", fields=None, df=False):
    # type: (Text|List, Optional[Text], bool) -> List[Dict[Text, Any]]|pd.DataFrame
    """
    查询品种信息\n
    VarietyInfo:
        variety_name        品种名称\n
        sec_type                   \n
        sec_type_ext        扩展类型\n
        exchange            交易市场代码\n
        quote_unit          报价单位\n
        price_tick          最小变动单位\n
        multiplier          合约乘数\n
        trade_n             交易制度\n
        option_type         行权方式\n
    """
    return fundamentalapi.get_varietyinfos(
        variety_names=variety_names,
        fields=fields,
        df=df,
    )


def get_trading_times(variety_names=""):
    # type: (Text|List|None) -> List[Dict[Text, Any]]
    """
    查询品种的交易时段 \n
    params: \n
    \t variety_names:           品种名称(全部大写)
    return: \n
    \t variety_name:            品种名称(全部大写)
    \t time_trading:            交易时段，如[{'start': '09:30','end': '11:30'}, {'start': '13:00', 'end': '15:00'}]
    \t time_callauction:        集合竞价时段，如[{’start': '09:15', 'end': '09:25'},{'start': '14:57', 'end': '15:00'}]
    """
    return fundamentalapi.get_trading_times(
        variety_names=variety_names,
    )


def _bin_search(lst, value):
    lo = 0
    hi = len(lst)
    while lo < hi:
        mid = (hi+lo)//2
        if lst[mid] == value:
            return mid
        elif lst[mid] > value:
            hi = mid - 1
        else:
            lo = mid + 1
    if lo < len(lst) and lst[lo] != value:
        return lo - 1
    return lo


def get_expire_rest_days(symbols=None, trade_date=None, trading_days=False, df=False):
    # type: (Text|List|None, Text|Datetime|None, bool, bool) -> List[Dict]|pd.DataFrame
    """查询到期剩余天数"""
    # 规范化输入参数
    date_fmt = "%Y-%m-%d"
    if trade_date is None:
        trade_date = Datetime.now()
    elif isinstance(trade_date, str):
        trade_date = utils.str2datetime(trade_date)
    trade_date = utils.beijing_zero_oclock(trade_date)
    if symbols is None:
        symbols = []
    elif isinstance(symbols, str):
        symbols = [s.strip() for s in symbols.split(',')]

    result = []
    infos = get_instrumentinfos(
        symbols=symbols,
        fields='symbol,delisted_date,listed_date',
    )
    if len(infos) != len(symbols):
        valid_symbols = {info["symbol"].strip() for info in infos}
        invalid_symbols = [s for s in symbols if s not in valid_symbols]
        raise ValueError("存在错误合约: {}".format(invalid_symbols))

    if trading_days:
        trade_date_str = Datetime.strftime(trade_date, date_fmt)

        valid_exchange = {'SHSE', 'SZSE',
                          'CFFEX', 'SHFE', 'DCE', 'CZCE', 'INE'}
        trading_date_range = {}  # key: exchange, value: [start_date, end_date]
        unlisted_symbols = []   # 未上市合约

        for info in infos:
            if info["listed_date"] > trade_date:
                unlisted_symbols.append(info["symbol"])
            exchange = info["symbol"].split(".")[0].strip()
            if exchange not in valid_exchange:
                continue

            delisted_date = info["delisted_date"]
            if exchange not in trading_date_range:
                if trade_date < delisted_date:
                    trading_date_range[exchange] = [trade_date, delisted_date]
                else:
                    trading_date_range[exchange] = [delisted_date, trade_date]
            else:
                trading_date_range[exchange][0] = min(
                    trading_date_range[exchange][0], delisted_date)
                trading_date_range[exchange][1] = max(
                    trading_date_range[exchange][1], delisted_date)

        if unlisted_symbols:
            raise ValueError("有未上市合约: {}".format(unlisted_symbols))

        exchange_trading_dates = {}
        for exchange, [start_date, end_date] in trading_date_range.items():
            exchange_trading_dates[exchange] = get_trading_dates(
                exchange, start_date, end_date)

        for info in infos:
            exchange = info["symbol"].split(".")[0].strip()
            delisted_date_str = info["delisted_date"].strftime(date_fmt)
            idx = _bin_search(
                exchange_trading_dates[exchange], delisted_date_str)
            trade_date_idx = _bin_search(
                exchange_trading_dates[exchange], trade_date_str)
            result.append({
                "symbol": info["symbol"],
                "days_to_expire": idx - trade_date_idx,
            })
    else:
        unlisted_symbols = []   # 未上市合约
        for info in infos:
            if info["listed_date"] > trade_date:
                unlisted_symbols.append(info["symbol"])
            result.append({
                "symbol": info["symbol"],
                "days_to_expire": (info["delisted_date"] - trade_date).days,
            })
        if unlisted_symbols:
            raise ValueError("有未上市合约: {}".format(unlisted_symbols))
    if df:
        return pd.DataFrame(result)
    return result


def option_get_symbols_by_exchange(exchange=None, trade_date=Datetime.now(), call_or_put="", adjust_flag=""):
    # type: (Text|List|None, Text|Datetime, Text, Text) -> List[Text]
    """
    查询期权合约 \n
    return:
        list[symbol]
    """
    return fundamentalapi.option_get_symbols_by_exchange(
        exchange=exchange,
        trade_date=trade_date,
        call_or_put=call_or_put,
        adjust_flag=adjust_flag,
    )


def option_get_symbols_by_in_at_out(underlying_symbol=None,
                                    trade_date=Datetime.now(),
                                    execute_month=None,
                                    call_or_put=None,
                                    in_at_out=None,
                                    s=None,
                                    adjust_flag="",
                                    ):
    # type: (Text|None, Text|Datetime, int|None, Text, int|None, float|Text|None, Text) -> list[Text]
    """
    查询实平虚值某档合约 \n
    return:z
        list[symbol]
    """
    return fundamentalapi.option_get_symbols_by_in_at_out(
        underlying_symbol=underlying_symbol,
        trade_date=trade_date,
        execute_month=execute_month,
        call_or_put=call_or_put,
        in_at_out=in_at_out,
        s=s,
        adjust_flag=adjust_flag,
    )


def option_get_delisted_dates(underlying_symbol="", trade_date=Datetime.now(), execute_month=0):
    # type: (Text, Text|Datetime, int) -> List[Date]
    """
    查询期权到期日列表 \n
    params: \n
    \t underlying_symbol:       标的物symbol, 全部大写, 不指定具体到期月份, 例'DCE.V'
    \t trade_date:              交易时间，默认当前最新时间
    \t execute_month:           合约月份，1-当月，2-下月，3-下季，4-隔季,
                                默认0, 返回所有合约月份的到期日列表
    return:
    \t 包含指定标的物的到期日列表 list
    """
    return fundamentalapi.option_get_delisted_dates(
        underlying_symbol=underlying_symbol,
        trade_date=trade_date,
        execute_month=execute_month,
    )


def option_get_exercise_prices(underlying_symbol="",
                               trade_date=Datetime.now(),
                               execute_month=0,
                               adjust_flag=""
                               ):
    # type: (Text, Text|Datetime, int, Text) -> List[float]
    """
    查询期权行权价列表 \n
    params: \n
    \t underlying_symbol:       标的物symbol, 全部大写, 不指定具体到期月份, 例'DCE.V'
    \t trade_date:              交易时间，默认当前最新时间
    \t execute_month:           合约月份，1-当月，2-下月，3-下季，4-隔季,
                                默认0, 返回所有合约月份的到期日列表
    \t adjust_flag:             表示是否过滤除权后合约(带A合约），不填默认为''（空字符串）\n
                                'M'表示不返回带A合约\n
                                'A'表示只返回带A合约\n
                                '' 表示不做过滤都返回\n
    return:
    \t 包含指定标的物、到期日的行权价列表 list
    """
    return fundamentalapi.option_get_exercise_prices(
        underlying_symbol=underlying_symbol,
        trade_date=trade_date,
        execute_month=execute_month,
        adjust_flag=adjust_flag,
    )


def bond_convertible_get_call_info(symbols=None, start_date=None, end_date=None):
    # type: (str|List, str|Datetime|None, str|Datetime|None) -> pd.DataFrame
    """
    查询可转债赎回信息
    """
    infos = fundamentalapi.bond_convertible_get_call_info(
        symbols, start_date, end_date)
    return pd.DataFrame(infos)
