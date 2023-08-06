# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import

from typing import Text, List, Dict, Any

import pandas as pd
from gm.csdk.c_sdk import c_status_fail, py_gmi_repay_cash_directly_pb, \
    py_gmi_get_collateral_instruments_pb, py_gmi_get_borrowable_instruments_pb, \
    py_gmi_get_borrowable_instruments_positions_pb, py_gmi_get_credit_contracts_pb, py_gmi_get_credit_cash_pb

from gm.enum import OrderQualifier_Unknown, OrderDuration_Unknown
from gm.pb.account_pb2 import Order, OrderBusiness_CREDIT_BOM, OrderBusiness_CREDIT_SS, \
    OrderType_Limit, OrderBusiness_CREDIT_RSBBS, OrderBusiness_CREDIT_RCBSS, OrderBusiness_CREDIT_BOC, \
    OrderBusiness_CREDIT_SOC, OrderBusiness_CREDIT_DRS, OrderType, OrderDuration, OrderQualifier, \
    OrderBusiness_CREDIT_CI, OrderBusiness_CREDIT_CO, OrderBusiness, PositionSrc, PositionSrc_Unknown
from gm.pb.trade_credit_service_pb2 import RepayCashDirectlyReq, RepayCashDirectlyRsp, \
    GetBorrowableInstrumentsPositionsReq, GetBorrowableInstrumentsPositionsRsp, \
    GetBorrowableInstrumentsReq, GetBorrowableInstrumentsRsp, GetCollateralInstrumentsReq, \
    GetCollateralInstrumentsRsp, GetCreditCashReq, GetCreditCashRsp, GetCreditContractsReq, \
    GetCreditContractsRsp
from gm.pb_to_dict import protobuf_to_dict
from .trade import get_account_id, _inner_place_order


def credit_repay_cash_directly(amount, account_id='', sno='', bond_fee_only=False):
    # type: (float, Text, Text, int) -> Dict[Text, Any]
    """
    直接还款
    :param account_id:      账号ID
    :param amount:          金额
    :param sno:             合约编号
    :param bond_fee_only:   是否仅偿还利息
    :return:
    """
    fee_only = '1' if bond_fee_only else '0'
    req = RepayCashDirectlyReq(account_id=account_id, amount=amount, properties={'debtsno':sno, 'bond_fee_only': fee_only})
    req = req.SerializeToString()
    status, result = py_gmi_repay_cash_directly_pb(req)
    if c_status_fail(status, 'py_gmi_repay_cash_directly_pb') or not result:
        return None

    res = RepayCashDirectlyRsp()
    res.ParseFromString(result)
    res = protobuf_to_dict(res)
    del res['rid']  # rid 不需要返回
    return res


def credit_get_collateral_instruments(account_id='', df=False):
    # type: (Text, bool) ->List[Dict[Text, Any]]
    """
    查询担保证券，可做担保品股票列表
    :param account_id:  账号id
    :param df:          是否返回DataFrame格式数据
    :return:
    """
    req = GetCollateralInstrumentsReq(account_id=account_id)
    req = req.SerializeToString()
    status, result = py_gmi_get_collateral_instruments_pb(req)
    if c_status_fail(status, 'py_gmi_get_collateral_instruments_pb') or not result:
        return [] if not df else pd.DataFrame([])

    res = GetCollateralInstrumentsRsp()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(item, is_utc_time=True, including_default_value_fields=True) for item in res.data]
    return datas if not df else pd.DataFrame(datas)


def credit_get_borrowable_instruments(position_src, account_id='', df=False):
    # type: (PositionSrc, Text, bool) -> List[Dict[Text, Any]]
    """
    查询标的证券，可做融券标的股票列表
    :param position_src: 头寸来源(仅适用融资融券)，取值参考enum PositionSrc
    :param account_id:  账号id
    :param df:          是否返回DataFrame格式数据
    :return:
    """
    req = GetBorrowableInstrumentsReq(position_src=position_src, account_id=account_id)
    req = req.SerializeToString()
    status, result = py_gmi_get_borrowable_instruments_pb(req)
    if c_status_fail(status, 'py_gmi_get_borrowable_instruments_pb') or not result:
        return [] if not df else pd.DataFrame([])

    res = GetBorrowableInstrumentsRsp()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(item, is_utc_time=True, including_default_value_fields=True) for item in res.data]
    return datas if not df else pd.DataFrame(datas)


def credit_get_borrowable_instruments_positions(position_src, account_id='', df=False):
    # type: (PositionSrc, Text, bool) -> List[Dict[Text, Any]]
    """
    查询券商融券账户头寸，可用融券的数量
    :param position_src: 头寸来源(仅适用融资融券)，取值参考enum PositionSrc
    :param account_id:  账号id
    :param df:          是否返回DataFrame格式数据
    :return:
    """
    req = GetBorrowableInstrumentsPositionsReq(position_src=position_src, account_id=account_id)
    req = req.SerializeToString()
    status, result = py_gmi_get_borrowable_instruments_positions_pb(req)
    if c_status_fail(status, 'py_gmi_get_borrowable_instruments_positions_pb') or not result:
        return [] if not df else pd.DataFrame([])

    res = GetBorrowableInstrumentsPositionsRsp()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(item, is_utc_time=True, including_default_value_fields=True) for item in res.data]
    return datas if not df else pd.DataFrame(datas)


def credit_get_contracts(position_src, account_id='', df=False):
    # type: (PositionSrc, Text, bool) -> List[Dict[Text, Any]]
    """
    查询融资融券合约
    :param position_src: 头寸来源(仅适用融资融券)，取值参考enum PositionSrc
    :param account_id:  账号id
    :param df:          是否返回DataFrame格式数据
    :return:
    """
    req = GetCreditContractsReq(position_src=position_src, account_id=account_id)
    req = req.SerializeToString()
    status, result = py_gmi_get_credit_contracts_pb(req)
    if c_status_fail(status, 'py_gmi_get_credit_contracts_pb') or not result:
        return [] if not df else pd.DataFrame([])

    res = GetCreditContractsRsp()
    res.ParseFromString(result)
    datas = [protobuf_to_dict(item, is_utc_time=True, including_default_value_fields=True) for item in res.data]
    return datas if not df else pd.DataFrame(datas)


def credit_get_cash(account_id=''):
    # type: (Text) -> Dict[Text, Any]
    """
    查询融资融券资金
    :param account_id:  账号id
    :return:
    """
    req = GetCreditCashReq(account_id=account_id)
    req = req.SerializeToString()
    status, result = py_gmi_get_credit_cash_pb(req)
    if c_status_fail(status, 'py_gmi_get_credit_cash_pb') or not result:
        return None

    res = GetCreditCashRsp()
    res.ParseFromString(result)
    res = protobuf_to_dict(res)
    return res


def credit_buying_on_margin(position_src, symbol, volume, price, order_type=OrderType_Limit, order_duration=OrderDuration_Unknown,
                            order_qualifier=OrderQualifier_Unknown, account_id=''):
    # type: (PositionSrc, Text, int, float, OrderType, OrderDuration, OrderQualifier, Text) -> Dict[Text, Any]
    """
    融资买入
    :param symbol:              标的
    :param volume:              数量
    :param price:               委托价格
    :param order_type:          委托订单类型
    :param order_duration:      委托时间属性
    :param order_qualifier:     委托成交属性
    :param position_src:        头寸来源(仅适用融资融券)，取值参考enum PositionSrc
    :param account_id:          账号id
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_BOM, symbol, volume, price,
                               order_type, order_duration, order_qualifier, position_src, account_id=account_id)


def credit_short_selling(position_src, symbol, volume, price, order_type=OrderType_Limit, order_duration=OrderDuration_Unknown,
                         order_qualifier=OrderQualifier_Unknown, account_id=''):
    # type: (PositionSrc, Text, int, float, OrderType, OrderDuration, OrderQualifier, Text) -> Dict[Text, Any]
    """
    融券卖出
    :param position_src:        头寸来源(仅适用融资融券)，取值参考enum PositionSrc
    :param symbol:              标的
    :param volume:              数量
    :param price:               委托价格
    :param order_type:          委托订单类型
    :param order_duration:      委托时间属性
    :param order_qualifier:     委托成交属性
    :param account_id:          账号id
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_SS, symbol, volume, price,
                               order_type, order_duration, order_qualifier, position_src,account_id=account_id)


def credit_repay_share_by_buying_share(symbol, volume, price, order_type=OrderType_Limit,
                                       order_duration=OrderDuration_Unknown,
                                       order_qualifier=OrderQualifier_Unknown, account_id='', sno=''):
    # type: (Text, int, float, OrderType, OrderDuration, OrderQualifier, Text, Text) -> Dict[Text, Any]
    """
    买券还券
    :param symbol:              标的
    :param volume:              数量
    :param price:               委托价格
    :param order_type:          委托订单类型
    :param order_duration:      委托时间属性
    :param order_qualifier:     委托成交属性
    :param account_id:          账号id
    :param sno:                 合约编号
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_RSBBS, symbol, volume, price,
                               order_type, order_duration, order_qualifier, account_id=account_id, sno=sno)


def credit_repay_cash_by_selling_share(symbol, volume, price, order_type=OrderType_Limit,
                                       order_duration=OrderDuration_Unknown,
                                       order_qualifier=OrderQualifier_Unknown, account_id='', sno=''):
    # type: (Text, int, float, OrderType, OrderDuration, OrderQualifier, Text, Text) -> Dict[Text, Any]
    """
    卖券还款
    :param symbol:              标的
    :param volume:              数量
    :param price:               委托价格
    :param order_type:          委托订单类型
    :param order_duration:      委托时间属性
    :param order_qualifier:     委托成交属性
    :param account_id:          账号id
    :param sno:                 合约编号
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_RCBSS, symbol, volume, price,
                               order_type, order_duration, order_qualifier, account_id=account_id, sno=sno)


def credit_buying_on_collateral(symbol, volume, price,
                                order_type=OrderType_Limit,
                                order_duration=OrderDuration_Unknown,
                                order_qualifier=OrderQualifier_Unknown, account_id=''):
    # type: (Text, int, float, OrderType, OrderDuration, OrderQualifier, Text) -> Dict[Text, Any]
    """
    担保品买入
    :param symbol:              标的
    :param volume:              数量
    :param price:               委托价格
    :param order_type:          委托订单类型
    :param order_duration:      委托时间属性
    :param order_qualifier:     委托成交属性
    :param account_id:          账号id
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_BOC, symbol, volume, price,
                               order_type, order_duration, order_qualifier, account_id=account_id)


def credit_selling_on_collateral(symbol, volume, price,
                                 order_type=OrderType_Limit,
                                 order_duration=OrderDuration_Unknown,
                                 order_qualifier=OrderQualifier_Unknown, account_id=''):
    # type: (Text, int, float, OrderType, OrderDuration, OrderQualifier, Text) -> Dict[Text, Any]
    """
    担保品卖出
    :param symbol:              标的
    :param volume:              数量
    :param price:               委托价格
    :param order_type:          委托订单类型
    :param order_duration:      委托时间属性
    :param order_qualifier:     委托成交属性
    :param account_id:          账号id
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_SOC, symbol, volume, price,
                               order_type, order_duration, order_qualifier, account_id=account_id)


def credit_repay_share_directly(symbol, volume, account_id='', sno=''):
    # type: (Text, int, Text, Text) -> List[Dict[str, Any]]
    """
    直接还券
    :param symbol:              标的
    :param volume:              数量
    :param account_id:          账号id
    :param sno:                 合约编号
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_DRS, symbol, volume, price=0, account_id=account_id, sno=sno)


def credit_collateral_in(symbol, volume, account_id=''):
    # type: (Text, int, Text) -> List[Dict[str, Any]]
    """
    担保品转入
    :param symbol:              标的
    :param volume:              数量
    :param account_id:          账号id
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_CI, symbol, volume, price=0, account_id=account_id)


def credit_collateral_out(symbol, volume, account_id=''):
    # type: (Text, int, Text) -> List[Dict[str, Any]]
    """
    担保品转出
    :param symbol:              标的
    :param volume:              数量
    :param account_id:          账号id
    :return:
    """
    return _credit_place_order(OrderBusiness_CREDIT_CO, symbol, volume, price=0, account_id=account_id)


def _credit_place_order(order_business, symbol, volume, price, order_type=OrderType_Limit,
                        order_duration=OrderDuration_Unknown, order_qualifier=OrderQualifier_Unknown,
                        position_src=PositionSrc_Unknown, account_id='', sno=''):
    # type: (OrderBusiness ,Text, int, float, OrderType, OrderDuration, OrderQualifier, PositionSrc, Text, Text) -> List[Dict[str, Any]]
    o = Order()
    o.position_src = position_src
    o.symbol = symbol
    o.volume = volume
    o.price = price
    o.order_type = order_type
    o.order_business = order_business
    o.order_qualifier = order_qualifier
    o.order_duration = order_duration
    o.account_id = account_id
    if sno != '':
        if o.properties is None:
            o.properties = {'debtsno': sno}
        else:
            o.properties['debtsno'] = sno


    return _inner_place_order(o)
