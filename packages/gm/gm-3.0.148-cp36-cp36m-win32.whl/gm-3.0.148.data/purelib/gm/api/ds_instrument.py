from typing import List, Dict

import pandas as pd

from gm.api._utils import invalid_status
from gm.csdk.c_sdk import (
    py_gmi_get_symbol_infos,
    py_gmi_get_symbols_v2,
    py_gmi_get_history_symbol,
    py_get_trading_dates_by_year,
    py_gmi_get_trading_session,
    py_gmi_get_contract_expire_rest_days,
)
from gm.pb_to_dict import protobuf_to_dict
from gm.pb.instrument_service_pb2 import (
    GetSymbolInfosReq, GetSymbolInfosResp,
    GetSymbolsReq, GetSymbolsResp,
    GetHistorySymbolReq, GetHistorySymbolResp,
    GetTradingDatesByYearReq, GetTradingDatesByYearResp,
    GetTradingSessionReq, GetTradingSessionResp,
    GetContractExpireRestDaysReq, GetContractExpireRestDaysResp,
)


def _datetime_to_str(value):
    if pd.notnull(value):
        return value.strftime("%Y-%m-%d")
    return ""


def get_symbol_infos(sec_type1, sec_type2=0, exchanges=None, symbols=None, df=False):
    # type: (int, int, str|List[str], str|List[str], bool) -> List[Dict]|pd.DataFrame
    """
    查询标的基本信息
    """
    if exchanges is None:
        exchanges = []
    elif isinstance(exchanges, str):
        exchanges = [exchange.strip() for exchange in exchanges.split(",")]
    if symbols is None:
        symbols = []
    elif isinstance(symbols, str):
        symbols = [symbol.strip() for symbol in symbols.split(",")]

    req = GetSymbolInfosReq(
        sec_type1=sec_type1,
        sec_type2=sec_type2,
        exchanges=exchanges,
        symbols=symbols,
    )
    req = req.SerializeToString()
    status, result = py_gmi_get_symbol_infos(req)
    if invalid_status(status):
        data = []
    else:
        rsp = GetSymbolInfosResp()
        rsp.ParseFromString(result)
        result = protobuf_to_dict(rsp)
        data = result.get("symbol_infos", [])   # type: List[Dict]
    if df:
        data = pd.DataFrame(data)
    return data


def get_symbols(sec_type1, sec_type2=0, exchanges=None, symbols=None, skip_suspended=True, skip_st=True, trade_date="", df=False):
    # type: (int, int, str|List[str], str|List[str], bool, bool, str, bool) -> List[Dict]|pd.DataFrame
    """
    查询指定交易日多标的交易信息
    """
    if exchanges is None:
        exchanges = []
    elif isinstance(exchanges, str):
        exchanges = [exchange.strip() for exchange in exchanges.split(",")]
    if symbols is None:
        symbols = []
    elif isinstance(symbols, str):
        symbols = [symbol.strip() for symbol in symbols.split(",")]

    req = GetSymbolsReq(
        sec_type1=sec_type1,
        sec_type2=sec_type2,
        exchanges=exchanges,
        symbols=symbols,
        skip_suspended=skip_suspended,
        skip_st=skip_st,
        trade_date=trade_date,
    )
    req = req.SerializeToString()
    status, result = py_gmi_get_symbols_v2(req)
    if invalid_status(status):
        data = []
    else:
        rsp = GetSymbolsResp()
        rsp.ParseFromString(result)
        result = protobuf_to_dict(rsp)
        data = result.get("symbols", [])   # type: List[Dict]
        for item in data:
            item.update(item["info"])
            del item["info"]
    if df:
        data = pd.DataFrame(data)
    return data


def get_history_symbol(symbol, start_date="", end_date="", df=False):
    # type: (str, str, str, bool) -> List[Dict]|pd.DataFrame
    """
    查询指定标的多日交易信息
    """
    req = GetHistorySymbolReq(
        symbol=symbol,
        start_date=start_date,
        end_date=end_date,
    )
    req = req.SerializeToString()
    status, result = py_gmi_get_history_symbol(req)
    if invalid_status(status):
        data = []
    else:
        rsp = GetHistorySymbolResp()
        rsp.ParseFromString(result)
        result = protobuf_to_dict(rsp)
        data = result.get("symbols", [])   # type: List[Dict]
        for item in data:
            item.update(item["info"])
            del item["info"]
    if df:
        data = pd.DataFrame(data)
    return data


def get_trading_dates_by_year(exchange, start_year, end_year):
    # type: (str, int, int) -> pd.DataFrame
    """查询年度交易日历"""
    req = GetTradingDatesByYearReq(
        exchange=exchange,
        start_year=start_year,
        end_year=end_year,
    )
    req = req.SerializeToString()
    status, result = py_get_trading_dates_by_year(req)
    data = []
    if not invalid_status(status):
        rsp = GetTradingDatesByYearResp()
        rsp.ParseFromString(result)
        result = protobuf_to_dict(rsp)
        data = result.get("dates", [])
    return pd.DataFrame(data).applymap(_datetime_to_str)


def get_trading_session(symbols, df=False):
    # type: (str|List[str], bool) -> List
    """
    查询交易日的可交易时段
    """
    if isinstance(symbols, str):
        symbols = [symbol.strip() for symbol in symbols.split(",")]
    req = GetTradingSessionReq(
        symbols=symbols,
    )
    req = req.SerializeToString()
    status, result = py_gmi_get_trading_session(req)
    if invalid_status(status):
        data = []
    else:
        rsp = GetTradingSessionResp()
        rsp.ParseFromString(result)
        result = protobuf_to_dict(rsp)
        data = result.get("trading_sessions", [])   # type: List[Dict]
    if df:
        data = pd.DataFrame(data)
    return data


def get_contract_expire_rest_days(symbols, start_date="", end_date="", trade_flag=False, df=False):
    # type: (str|List[str], str, str, bool, bool) -> List
    """
    查询合约到期剩余天数
    """
    if isinstance(symbols, str):
        symbols = [symbol.strip() for symbol in symbols.split(",")]
    req = GetContractExpireRestDaysReq(
        symbols=symbols,
        start_date=start_date,
        end_date=end_date,
        by_trading_days=trade_flag,
    )
    req = req.SerializeToString()
    status, result = py_gmi_get_contract_expire_rest_days(req)
    if invalid_status(status):
        data = []
        if df:
            data = pd.DataFrame(data)
        return data

    rsp = GetContractExpireRestDaysResp()
    rsp.ParseFromString(result)
    result = protobuf_to_dict(rsp)
    data = result.get("contract_expire_rest_days", [])   # type: List[Dict]
    for value in data:
        if value["days_to_expire"] == "":
            value["days_to_expire"] = None
        else:
            value["days_to_expire"] = int(value["days_to_expire"])

    if df:
        data = pd.DataFrame(data)
    return data
