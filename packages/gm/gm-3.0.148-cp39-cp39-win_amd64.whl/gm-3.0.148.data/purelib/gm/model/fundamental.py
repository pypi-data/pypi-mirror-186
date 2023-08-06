# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

from datetime import date as Date, datetime as Datetime
from gm.api.basic import get_encrypted_token, get_orgcode

import grpc
import six
from google.protobuf.timestamp_pb2 import Timestamp
from six import string_types
from typing import List, Dict, Optional, Text, Any, Union
import pandas as pd

from gm import utils
from gm.constant import FUNDAMENTAL_ADDR
from gm.csdk.c_sdk import py_gmi_get_serv_addr
from gm.model.storage import context
from gm.pb.data_pb2 import Instrument, InstrumentInfo, ContinuousContract, Dividend, VarietyInfos
from gm.pb.fundamental_pb2_grpc import FundamentalServiceStub
from gm.pb.fundamental_pb2 import GetFundamentalsReq, GetInstrumentsReq, GetHistoryInstrumentsReq, \
    GetInstrumentInfosReq, GetConstituentsReq, GetIndustryReq, GetConceptReq, GetOptionDelistedDatesReq, GetOptionDelistedDatesRsp, GetOptionExercisePricesReq, GetOptionExercisePricesRsp, GetOptionSymbolsByExchangeReq, GetOptionSymbolsByExchangeRsp, GetOptionSymbolsByInAtOutReq, GetOptionSymbolsByInAtOutRsp, GetTradingDatesReq, \
    GetPreviousTradingDateReq, GetNextTradingDateReq, GetDividendsReq, \
    GetContinuousContractsReq, GetFundamentalsRsp, GetFundamentalsNReq, GetTradingTimesExtReq, GetTradingTimesExtReq, GetTradingTimesExtRsp, GetVarietyInfosReq, \
    GetConvertibleBondCallInfoReq, GetConvertibleBondCallInfoRsp
from gm.pb_to_dict import protobuf_to_dict
from gm.utils import proto_to_dict, str_lowerstrip, load_to_list, utc_datetime2beijing_datetime

GmDate = Union[Text, Datetime, Date]  # 自定义gm里可表示时间的类型
TextNone = Union[Text, None]  # 可表示str或者None类型

MAX_MESSAGE_LENGTH = 1024 * 1024 * 128


def get_sec_type_str(sec_types):
    """把int类型的sectype转为字符串的sectype, 不能转换则返回None"""
    d = {
        1: 'stock',
        2: 'fund',
        3: 'index',
        4: 'future',
        5: 'option',
        6: 'credit',
        7: 'bond',
        8: 'bond_convertible',
        10: 'confuture',
        '1': 'stock',
        '2': 'fund',
        '3': 'index',
        '4': 'future',
        '5': 'option',
        '6': 'credit',
        '7': 'bond',
        '8': 'bond_convertible',
        '10': 'confuture',
        'stock': 'stock',
        'fund': 'fund',
        'index': 'index',
        'future': 'future',
        'option': 'option',
        'credit': 'credit',
        'bond': 'bond',
        'bond_convertible': 'bond_convertible',
        'confuture': 'confuture',
    }
    result = []
    for sec_type in sec_types:
        if isinstance(sec_type, six.string_types):
            sec_type = sec_type.strip().lower()

        if sec_type in d:
            result.append(d.get(sec_type))
        else:
            result.append(str(sec_type))

    return result


class FundamentalApi(object):
    def __init__(self):
        self.addr = None

    def _init_addr(self):
        new_addr = py_gmi_get_serv_addr(FUNDAMENTAL_ADDR)
        if not new_addr:
            raise EnvironmentError("获取不到基本面服务地址")

        if not self.addr:
            self.addr = new_addr
            channel = grpc.insecure_channel(self.addr,
                                            options=[('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
                                                     ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
            self.stub = FundamentalServiceStub(channel)

    def reset_addr(self):
        self.addr = None

    def get_fundamentals(self, table, symbols, start_date, end_date, fields=None, filter=None, order_by=None,
                         limit=1000):
        """
        查询基本面财务数据
        """
        self._init_addr()

        if isinstance(symbols, string_types):
            symbols = [s.strip() for s in symbols.split(',') if s.strip()]
        if not symbols:
            symbols = []

        req = GetFundamentalsReq(table=table, start_date=start_date, end_date=end_date,
                                 fields=fields, symbols=','.join(symbols), filter=filter,
                                 order_by=order_by, limit=limit)
        resp = self.stub.GetFundamentals(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])

        result = []
        for item in resp.data:  # type: GetFundamentalsRsp.Fundamental
            r = {
                'symbol': item.symbol,
                'pub_date': utils.utc_datetime2beijing_datetime(item.pub_date.ToDatetime()),
                'end_date': utils.utc_datetime2beijing_datetime(item.end_date.ToDatetime()),
            }
            r.update(item.fields)
            result.append(r)

        return result

    def get_instruments(self, symbols=None, exchanges=None, sec_types=None, names=None, skip_suspended=True,
                        skip_st=True, fields=None):
        """
        查询最新交易标的信息,有基本数据及最新日频数据
        """
        self._init_addr()
        # todo 这里代码限定的太死了, 后面优化一下
        instrument_fields = {
            'symbol', 'sec_level', 'is_suspended', 'multiplier', 'margin_ratio',
            'settle_price',
            'position', 'pre_close', 'upper_limit', 'lower_limit', 'adj_factor',
            'created_at', 'trade_date'
        }

        info_fields = {
            'sec_type', 'exchange', 'sec_id', 'sec_name', 'sec_abbr',
            'price_tick', 'underlying_symbol', 'conversion_price', 'exercise_price', 'conversion_start_date',
            'listed_date', 'delisted_date', 'trade_n', 'is_strike_price_adjusted',
            'call_or_put', 'sec_type_ext', 'margin_ratio',
            'option_margin_ratio1',  'option_margin_ratio2', 'board', 'option_type',
        }
        field_map = {
            'is_adjusted': 'is_strike_price_adjusted',
        }

        if fields is None:
            input_fields = ""
        else:
            input_fields = fields

        all_fields = instrument_fields.union(info_fields)

        if isinstance(symbols, string_types):
            symbols = [s for s in map(str_lowerstrip, symbols.split(',')) if s]
        if not symbols:
            symbols = []

        VALID_EXCHANGES = {'SHSE', 'SZSE',
                           'CFFEX', 'SHFE', 'DCE', 'CZCE', 'INE'}
        # exchanges 为 None 或空字符代表查询所有的交易所, 传给服务器 ""
        if exchanges is None or exchanges == "":
            exchanges = ""
        elif isinstance(exchanges, string_types):
            exchanges = ",".join(
                exchange
                for exchange in map(lambda x: x.strip(), exchanges.split(','))
                if exchange in VALID_EXCHANGES
            )
            # 没有传入正确的交易所代码, 直接返回空结果, 无需调用服务查询
            if exchanges == "":
                return []
        elif isinstance(exchanges, list):
            exchanges = ",".join(exchange.strip()
                                 for exchange in exchanges if VALID_EXCHANGES)
        else:
            # 传入的 exchanges 类型不对也返回空结果
            return []

        if isinstance(sec_types, six.string_types):
            sec_types = [it.strip()
                         for it in sec_types.split(',') if it.strip()]

        if isinstance(sec_types, int):
            sec_types = [sec_types]

        if isinstance(sec_types, list):
            sec_types = get_sec_type_str(sec_types)

        if not sec_types:
            sec_types = []

        if isinstance(names, string_types):
            names = [s for s in names.split(',') if s]
        if not names:
            names = []

        if not fields:
            filter_fields = all_fields
            fields = ""
        elif isinstance(fields, string_types):
            filter_fields = set()
            for field in fields.split(','):
                field = str_lowerstrip(field)
                if field in field_map:
                    field = field_map[field]
                if field in all_fields:
                    filter_fields.add(field)
            fields = ",".join(filter_fields)
        else:
            filter_fields = set()
            for field in fields:
                field = str_lowerstrip(field)
                if field in field_map:
                    field = field_map[field]
                if field in all_fields:
                    filter_fields.add(field)
            fields = ",".join(filter_fields)

        if 'trade_date' in filter_fields:
            filter_fields.add('created_at')

        if not filter_fields:
            return []

        req = GetInstrumentsReq(symbols=','.join(symbols),
                                exchanges=exchanges,
                                sec_types=','.join(sec_types),
                                names=','.join(names), skip_st=skip_st,
                                skip_suspended=skip_suspended,
                                fields=input_fields)
        resp = self.stub.GetInstruments(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        result = []
        instrument_copy_field = filter_fields & instrument_fields
        info_copy_field = filter_fields & info_fields
        for ins in resp.data:  # type: Instrument
            row = dict()
            utils.protomessage2dict(ins, row, *instrument_copy_field)

            created_at_val = row.get('created_at', None)
            if isinstance(created_at_val, Datetime):
                row['trade_date'] = utils.utc_datetime2beijing_datetime(
                    created_at_val)
                row.pop('created_at')

            #! 需要重构 protomessage2dict 函数
            row_tmp = dict()
            utils.protomessage2dict(ins.info, row_tmp, *info_copy_field)
            for k, v in six.iteritems(row_tmp):
                if k not in row:
                    row[k] = v

            listed_date_val = row.get('listed_date', None)
            if isinstance(listed_date_val, Datetime):
                row['listed_date'] = utils.utc_datetime2beijing_datetime(
                    listed_date_val)

            delisted_date_val = row.get('delisted_date', None)
            if isinstance(delisted_date_val, Datetime):
                row['delisted_date'] = utils.utc_datetime2beijing_datetime(
                    delisted_date_val)

            if isinstance(row.get('conversion_start_date', None), Datetime):
                row['conversion_start_date'] = utils.utc_datetime2beijing_datetime(
                    row.get('conversion_start_date', None))

            if row.get("is_strike_price_adjusted", None) is not None:
                row['is_adjusted'] = 1 if row.pop(
                    'is_strike_price_adjusted') else 0

            result.append(row)
        return result

    def get_history_instruments(self, symbols, fields="", start_date="", end_date=""):
        # type: (str, str, str, str) -> List[Dict]
        """
        返回指定的symbols的标的日指标数据
        """
        self._init_addr()
        symbols = load_to_list(symbols)
        start_date = utils.to_datestr(start_date)
        end_date = utils.to_datestr(end_date)

        instrument_fields = {
            'symbol', 'sec_level', 'is_suspended', 'multiplier', 'margin_ratio',
            'settle_price',
            'position', 'pre_close', 'upper_limit', 'lower_limit', 'adj_factor',
            'created_at', 'trade_date', 'conversion_price'
        }
        info_fields = {
            'sec_type', 'exchange', 'sec_id', 'sec_name', 'sec_abbr',
            'price_tick', 'underlying_symbol', 'conversion_price', 'exercise_price', 'conversion_start_date',
            'listed_date', 'delisted_date', 'trade_n', 'is_strike_price_adjusted',
            'call_or_put', 'sec_type_ext', 'margin_ratio',
            'option_margin_ratio1',  'option_margin_ratio2', 'board', 'option_type',
        }
        field_map = {
            'is_adjusted': 'is_strike_price_adjusted',
        }

        if fields:
            output_fields = {field.strip() for field in fields.split(",")}
        else:
            output_fields = None

        all_fields = instrument_fields.union(info_fields)

        if not fields:
            filter_fields = all_fields
            fields = ""
        elif fields != "" and isinstance(fields, string_types):
            filter_fields = set()
            for field in fields.split(","):
                field = str_lowerstrip(field)
                if field in field_map:
                    field = field_map[field]
                if field in all_fields:
                    filter_fields.add(field)
            fields = ",".join(filter_fields)

        req = GetHistoryInstrumentsReq(symbols=','.join(symbols),
                                       fields=fields,
                                       start_date=start_date, end_date=end_date)
        resp = self.stub.GetHistoryInstruments(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        result = [protobuf_to_dict(
            res_order, including_default_value_fields=True) for res_order in resp.data]
        for info in result:
            created_at_val = info.get('created_at', None)
            if isinstance(created_at_val, Datetime):
                info['trade_date'] = utils.utc_datetime2beijing_datetime(
                    created_at_val)
                info.pop('created_at')

            if 'strike_price' in info:
                info['exercise_price'] = info.pop('strike_price')

            # 调整标志取 info 外的
            if info.get("is_strike_price_adjusted"):
                info["is_adjusted"] = 1
            else:
                info["is_adjusted"] = 0
            if "is_strike_price_adjusted" in info:
                del info["is_strike_price_adjusted"]

            inner_info = info.get("info", None)
            if inner_info is None:
                continue
            for field, value in six.iteritems(inner_info):
                if field in ["multiplier", "exercise_price", "conversion_price", "margin_ratio", "is_strike_price_adjusted"]:
                    continue
                elif field not in info or (value and field in filter_fields):
                    info[field] = value
            # 删除info字段
            del info['info']

        if output_fields:
            return [{k: v for k, v in r.items() if k in output_fields} for r in result]
        return result

    def get_instrumentinfos(self, symbols=None, exchanges=None, sec_types=None, names=None, fields=None):
        """
        查询交易标的基本信息
        如果没有数据的话,返回空列表. 有的话, 返回list[dict]这样的列表. 其中 listed_date, delisted_date 为 datetime 类型
        @:param fields: 可以是 'symbol, sec_type' 这样的字符串, 也可以是 ['symbol', 'sec_type'] 这样的字符list
        """
        self._init_addr()

        if isinstance(symbols, string_types):
            symbols = [s for s in symbols.split(',') if s]
        if not symbols:
            symbols = []

        all_fields = {
            'symbol', 'sec_type', 'exchange', 'sec_id', 'sec_name', 'sec_abbr', 'price_tick', 'listed_date',
            'delisted_date', 'trade_n', 'underlying_symbol', 'conversion_price', 'exercise_price', 'conversion_start_date',
            'call_or_put', 'sec_type_ext', 'multiplier', 'margin_ratio', 'option_margin_ratio1',  'option_margin_ratio2',
            'board', 'option_type',
        }

        if not fields:
            filter_fields = all_fields
            fields = ""
        elif isinstance(fields, string_types):
            filter_fields = [f for f in map(
                str_lowerstrip, fields.split(',')) if f in all_fields]
            fields = ",".join(filter_fields)
        else:
            filter_fields = [f for f in map(
                str_lowerstrip, fields) if f in all_fields]
            fields = ",".join(filter_fields)

        if isinstance(exchanges, string_types):
            exchanges = [utils.to_exchange(s) for s in exchanges.split(
                ',') if utils.to_exchange(s)]
        if not exchanges:
            exchanges = []

        if isinstance(sec_types, six.string_types):
            sec_types = [it.strip()
                         for it in sec_types.split(',') if it.strip()]

        if isinstance(sec_types, int):
            sec_types = [sec_types]

        if isinstance(sec_types, list):
            sec_types = get_sec_type_str(sec_types)

        if not sec_types:
            sec_types = []

        if isinstance(names, string_types):
            names = [s for s in names.split(',') if s]
        if not names:
            names = []

        req = GetInstrumentInfosReq(symbols=','.join(symbols), exchanges=','.join(exchanges),
                                    sec_types=','.join(sec_types), names=','.join(names),
                                    fields=fields)
        resp = self.stub.GetInstrumentInfos(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        result = []
        for ins in resp.data:  # type: InstrumentInfo
            row = dict()
            utils.protomessage2dict(ins, row, *filter_fields)
            listed_date_val = row.get('listed_date', None)
            if isinstance(listed_date_val, Datetime):
                row['listed_date'] = utils.utc_datetime2beijing_datetime(
                    listed_date_val)

            delisted_date_val = row.get('delisted_date', None)
            if isinstance(delisted_date_val, Datetime):
                row['delisted_date'] = utils.utc_datetime2beijing_datetime(
                    delisted_date_val)

            if isinstance(row.get('conversion_start_date', None), Datetime):
                row['conversion_start_date'] = utils.utc_datetime2beijing_datetime(
                    row.get('conversion_start_date', None))

            result.append(row)

        return result

    def get_history_constituents(self, index, start_date=None, end_date=None):
        # type: (TextNone, GmDate, GmDate) -> List[Dict[Text, Any]]
        """
        查询指数历史成分股
        返回的list每项是个字典,包含的key值有:
        trade_date: 交易日期(datetime类型)
        constituents: 一个字典. 每个股票的sybol做为key值, weight做为value值
        """
        self._init_addr()

        start_date = utils.to_datestr(start_date)
        end_date = utils.to_datestr(end_date)

        if not start_date:
            start_date = Date.today()
        else:
            start_date = Datetime.strptime(start_date, '%Y-%m-%d').date()

        if not end_date:
            end_date = Date.today()
        else:
            end_date = Datetime.strptime(end_date, '%Y-%m-%d').date()

        req = GetConstituentsReq(index=index, start_date=start_date.strftime('%Y-%m-%d'),
                                 end_date=end_date.strftime('%Y-%m-%d'))
        resp = self.stub.GetConstituents(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])

        return [
            {'trade_date': utils.utc_datetime2beijing_datetime(item.created_at.ToDatetime()),
             'constituents': dict(item.constituents)}
            for item in resp.data
        ]

    def get_constituents(self, index, fields=None, df=False):
        """
        查询指数最新成分股. 指定 fields = 'symbol, weight'
        返回的list每项是个字典,包含的key值有:
        symbol 股票symbol
        weight 权重

        如果不指定 fields, 则返回的list每项是symbol字符串
        """
        self._init_addr()

        all_fields = ['symbol', 'weight']
        if not fields:
            filter_fields = {'symbol'}
        elif isinstance(fields, string_types):
            filter_fields = {f for f in map(
                str_lowerstrip, fields.split(',')) if f in all_fields}
        else:
            filter_fields = {f for f in map(
                str_lowerstrip, fields) if f in all_fields}

        req = GetConstituentsReq(index=index, start_date='', end_date='')
        resp = self.stub.GetConstituents(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        if len(resp.data) > 0:
            filter_fields = list(filter_fields)
            if len(filter_fields) == 1 and filter_fields[0] == 'symbol':
                if not df:
                    return [k for k, v in resp.data[0].constituents.items()]
                else:
                    return [{'symbol': k} for k, v in resp.data[0].constituents.items()]
            else:
                return [{'symbol': k, 'weight': v} for k, v in resp.data[0].constituents.items()]
        else:
            return []

    def get_sector(self, code):
        """
        查询板块股票列表
        """
        # TODO 没有数据, 先不实现
        self._init_addr()

        return []

    def get_industry(self, code):
        """
        查询行业股票列表
        """
        self._init_addr()

        if not code:
            return []
        req = GetIndustryReq(code=code)
        resp = self.stub.GetIndustry(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        return [r for r in resp.symbols]

    def get_concept(self, code):
        """
        查询概念股票列表
        """
        self._init_addr()

        if not code:
            return []
        req = GetConceptReq(code=code)
        resp = self.stub.GetConcept(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        ds = [r for r in resp.symbols]
        return ds

    def get_trading_dates(self, exchange, start_date, end_date):
        # type: (Text, GmDate, GmDate) -> List[Text]
        """
        查询交易日列表
        如果指定的市场不存在, 返回空列表. 有值的话,返回 yyyy-mm-dd 格式的列表
        """
        self._init_addr()

        exchange = utils.to_exchange(exchange)
        sdate = utils.to_datestr(start_date)
        edate = utils.to_datestr(end_date)
        if not exchange:
            return []
        if not sdate:
            return []
        if not end_date:
            edate = Datetime.now().strftime('%Y-%m-%d')
        req = GetTradingDatesReq(
            exchange=exchange, start_date=sdate, end_date=edate)
        resp = self.stub.GetTradingDates(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])

        if len(resp.dates) == 0:
            return []
        ds = []
        for t in resp.dates:  # type: Timestamp
            ds.append(utils.utc_datetime2beijing_datetime(
                t.ToDatetime()).strftime('%Y-%m-%d'))

        return ds

    def get_previous_trading_date(self, exchange, date):
        # type: (Text, GmDate) -> TextNone
        """
        返回指定日期的上一个交易日
        @:param exchange: 交易市场
        @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
        @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
        """
        self._init_addr()

        exchange = utils.to_exchange(exchange)
        date_str = utils.to_datestr(date)
        if not exchange or not date_str:
            return None

        req = GetPreviousTradingDateReq(exchange=exchange, date=date_str)
        resp = self.stub.GetPreviousTradingDate(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        rdate = resp.date  # type: Timestamp
        if not rdate.ListFields():  # 这个说明查询结果没有
            return None
        return utils.utc_datetime2beijing_datetime(rdate.ToDatetime()).strftime('%Y-%m-%d')

    def get_next_trading_date(self, exchange, date):
        # type: (Text, GmDate) -> TextNone
        """
        返回指定日期的下一个交易日
        @:param exchange: 交易市场
        @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
        @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
        """
        self._init_addr()

        exchange = utils.to_exchange(exchange)
        date_str = utils.to_datestr(date)
        if not date_str or not exchange:
            return None

        req = GetNextTradingDateReq(exchange=exchange, date=date_str)
        resp = self.stub.GetNextTradingDate(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        rdate = resp.date  # type: Timestamp
        if not rdate.ListFields():  # 这个说明查询结果没有
            return None
        return utils.utc_datetime2beijing_datetime(rdate.ToDatetime()).strftime('%Y-%m-%d')

    def get_dividend(self, symbol, start_date, end_date=None):
        # type: (Text, GmDate, GmDate) -> List[Dict[Text, Any]]
        """
        查询分红送配
        """
        self._init_addr()

        if not symbol or not start_date:
            return []
        sym_tmp = symbol.split('.')  # List[Text]
        sym_tmp[0] = sym_tmp[0].upper()
        symbol = '.'.join(sym_tmp)

        if not end_date:
            end_date = Datetime.now().strftime('%Y-%m-%d')
        start_date = utils.to_datestr(start_date)
        end_date = utils.to_datestr(end_date)

        req = GetDividendsReq(
            symbol=symbol, start_date=start_date, end_date=end_date)
        resp = self.stub.GetDividends(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        result = []
        fields = ['symbol', 'cash_div', 'share_div_ratio', 'share_trans_ratio', 'allotment_ratio', 'allotment_price',
                  'created_at']
        for divi in resp.data:  # type: Dividend
            row = dict()
            utils.protomessage2dict(divi, row, *fields)
            created_at_val = row.get('created_at', None)
            if isinstance(created_at_val, Datetime):
                row['created_at'] = utils.utc_datetime2beijing_datetime(
                    created_at_val)
            result.append(row)
        return result

    def get_continuous_contracts(self, csymbol, start_date=None, end_date=None):
        # type: (Text, GmDate, GmDate) -> List[Dict[Text, Any]]

        self._init_addr()

        start_date = utils.to_datestr(start_date)
        end_date = utils.to_datestr(end_date)

        req = GetContinuousContractsReq(
            csymbol=csymbol, start_date=start_date, end_date=end_date)
        resp = self.stub.GetContinuousContracts(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])

        result = []
        for cc in resp.data:  # type: ContinuousContract
            row = {'symbol': cc.symbol, 'trade_date': utils.utc_datetime2beijing_datetime(
                cc.created_at.ToDatetime())}
            result.append(row)
        return result

    def get_fundamentals_n(self, table, symbols, end_date, fields=None, filter=None, order_by=None, count=1):
        """
        查询基本面财务数据,每个股票在end_date的前n条
        """
        self._init_addr()

        end_date = utils.to_datestr(end_date)

        if isinstance(symbols, string_types):
            symbols = [s.strip() for s in symbols.split(',') if s.strip()]

        req = GetFundamentalsNReq(table=table, end_date=end_date, fields=fields,
                                  symbols=','.join(symbols), filter=filter,
                                  order_by=order_by, count=count)

        resp = self.stub.GetFundamentalsN(req, metadata=[
            # (str('authorization'), context.token),
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ])
        result = []
        for item in resp.data:  # type: GetFundamentalsRsp.Fundamental
            r = {
                'symbol': item.symbol,
                'pub_date': utils.utc_datetime2beijing_datetime(item.pub_date.ToDatetime()),
                'end_date': utils.utc_datetime2beijing_datetime(item.end_date.ToDatetime()),
            }
            r.update(item.fields)
            result.append(r)

        return result

    def _get_metadata(self):
        # type: () -> List[(Text, Text)]
        return [
            (str('authorization'), get_encrypted_token()),
            (str('x-orgcode'), get_orgcode()),
            (str('sdk-lang'), context.sdk_lang),
            (str('sdk-version'), context.sdk_version),
            (str('sdk-arch'), context.sdk_arch),
            (str('sdk-os'), context.sdk_os),
        ]

    def get_varietyinfos(self, variety_names="", fields=None, df=False):
        # type: (Text|List, Optional[Text], bool) -> List[Dict[Text, Any]]|pd.DataFrame
        """
        查询品种信息\n
        VarietyInfo:
            variety_name            品种名称\n
            sec_type                       \n
            sec_type_ext            扩展类型\n
            exchange                交易市场代码\n
            quote_unit              报价单位\n
            price_tick              最小变动单位\n
            multiplier              合约乘数\n
            trade_n                 交易制度\n
            option_type             行权方式\n
            option_margin_ratio1    期权保证金比例计算参数1\n
            option_margin_ratio2	期权保证金比例计算参数2\n
        """
        self._init_addr()

        # 字段以逗号分隔, 输入None返回空数组代表全部字段
        req = GetVarietyInfosReq(
            variety_names=_to_field_list(variety_names),
            fields=_to_field_list(fields),
        )
        rsp = self.stub.GetVarietyInfos(
            request=req,
            metadata=self._get_metadata(),
        )  # type: VarietyInfos

        data = []
        if len(rsp.data) > 0:
            for info in rsp.data:
                row = proto_to_dict(info)
                data.append(row)
        if df:
            data = pd.DataFrame(data)
        return data

    def get_trading_times(self, variety_names=None):
        # type: (Text|List|None) -> List[Dict[Text, Any]]
        """
        查询品种的交易时段 \n
        """
        self._init_addr()

        req = GetTradingTimesExtReq(
            variety_names=_to_field_list(variety_names),
        )
        rsp = self.stub.GetTradingTimesExt(
            request=req,
            metadata=self._get_metadata(),
        )  # type: GetTradingTimesExtRsp
        result = []
        for tte in rsp.data:
            result.append(_tte_to_dict(tte))
        return result

    def option_get_symbols_by_exchange(self,
                                       exchange=None,
                                       trade_date=Datetime.now(),
                                       call_or_put="",
                                       adjust_flag=""
                                       ):
        # type: (Text|List|None, Text|Datetime, Text, Text) -> List[Text]
        """
        查询期权合约 \n
        return:
            list[symbol]
        """
        self._init_addr()

        if exchange is None:
            exchange = ""
        elif isinstance(exchange, list):
            exchange = ",".join(exchange)

        trade_date = utils.to_datestr(trade_date)

        req = GetOptionSymbolsByExchangeReq(
            exchange=exchange,
            trade_date=trade_date,
            call_or_put=call_or_put,
            adjust_flag=adjust_flag,
        )
        rsp = self.stub.GetOptionSymbolsByExchange(
            request=req,
            metadata=self._get_metadata(),
        )  # type: GetOptionSymbolsByExchangeRsp
        result = [symbol for symbol in rsp.symbols]
        return result

    def option_get_symbols_by_in_at_out(self,
                                        underlying_symbol=None,
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
        return:
            list[symbol]
        """
        self._init_addr()

        if underlying_symbol is None:
            underlying_symbol = ""

        trade_date = utils.format_datetime_str(trade_date)

        if execute_month is None:
            execute_month = 0

        if call_or_put is None:
            call_or_put = ""

        if in_at_out is None:
            in_at_out = ""
        else:
            in_at_out = str(in_at_out)

        if s is None:
            price = 0.0
            price_type = "last"
        elif isinstance(s, float):
            price = s
            price_type = ""
        elif isinstance(s, six.string_types):
            price = 0.0
            price_type = s

        req = GetOptionSymbolsByInAtOutReq(
            underlying_symbol=underlying_symbol,
            trade_time=trade_date,
            execute_month=execute_month,
            call_or_put=call_or_put,
            in_at_out=in_at_out,
            price=price,
            price_type=price_type,
            adjust_flag=adjust_flag,
        )
        rsp = self.stub.GetOptionSymbolsByInAtOut(
            request=req,
            metadata=self._get_metadata(),
        )  # type: GetOptionSymbolsByInAtOutRsp
        result = [symbol for symbol in rsp.symbols]
        return result

    def option_get_delisted_dates(self, underlying_symbol="", trade_date=Datetime.now(), execute_month=0):
        # type: (Text, Text|Datetime, int) -> List[Date]
        """
        查询期权到期日列表 \n
        return:
            list[Date]
        """
        self._init_addr()

        trade_date = utils.to_datestr(trade_date)
        req = GetOptionDelistedDatesReq(
            underlying_symbol=underlying_symbol,
            trade_date=trade_date,
            execute_month=execute_month,
        )
        rsp = self.stub.GetOptionDelistedDates(
            request=req,
            metadata=self._get_metadata(),
        )  # type: GetOptionDelistedDatesRsp
        return [utc_datetime2beijing_datetime(t.ToDatetime()).date() for t in rsp.delisted_date]

    def option_get_exercise_prices(self,
                                   underlying_symbol="",
                                   trade_date=Datetime.now(),
                                   execute_month=0,
                                   adjust_flag=""
                                   ):
        # type: (Text, Text|Datetime, int, Text) -> List[float]
        """
        查询期权行权价列表 \n
        return:
            list[exercise_price]
        """
        self._init_addr()

        trade_date = utils.to_datestr(trade_date)
        req = GetOptionExercisePricesReq(
            underlying_symbol=underlying_symbol,
            trade_date=trade_date,
            execute_month=execute_month,
            adjust_flag=adjust_flag,
        )
        rsp = self.stub.GetOptionExercisePrices(
            request=req,
            metadata=self._get_metadata(),
        )  # type: GetOptionExercisePricesRsp
        result = [exercise_price for exercise_price in rsp.exercise_prices]
        return result

    def bond_convertible_get_call_info(self, symbols=None, start_date=None, end_date=None):
        # type: (str|List, str|Datetime|None, str|Datetime|None) -> List[Dict]
        self._init_addr()

        if symbols is None:
            symbols = []
        elif isinstance(symbols, str):
            symbols = symbols.split(",")

        if start_date is None:
            start_date = ""
        else:
            start_date = utils.to_datestr(start_date)
        if end_date is None:
            end_date = ""
        else:
            end_date = utils.to_datestr(end_date)

        req = GetConvertibleBondCallInfoReq(
            symbols=symbols, start_date=start_date, end_date=end_date)
        rsp = self.stub.GetConvertibleBondCallInfo(
            request=req,
            metadata=self._get_metadata(),
        )  # type: GetConvertibleBondCallInfoRsp
        data = protobuf_to_dict(rsp)
        return data.get("infos", [])


def _to_field_list(fields):
    # type: (Text|List|None) -> List
    if isinstance(fields, list):
        return fields
    elif isinstance(fields, six.string_types):
        return [field.strip().lower() for field in fields.split(',')]
    else:
        return []


def _tte_to_dict(tte):
    # type: (GetTradingTimesExtRsp.TTE) -> Dict
    time_trading = _get_times(tte.sections)
    time_callauction = _get_times(tte.auctions)
    return {
        "variety_name": tte.variety_name,
        "time_trading": time_trading,
        "time_callauction": time_callauction,
    }


def _get_times(time_list):
    # type: (List) -> List[Dict[Text, Any]]
    times = []
    for i in range(0, len(time_list), 2):
        times.append(
            {
                "start": time_list[i],
                "end": time_list[i+1],
            }
        )
    return times
