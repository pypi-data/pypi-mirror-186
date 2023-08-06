import sys
from typing import Dict
from datetime import datetime, timedelta, timezone

from gm.utils import gmsdklogger
from gm.csdk.c_sdk import gmi_get_ext_errormsg
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.message import Message
from google.protobuf.pyext._message import (
    RepeatedCompositeContainer,
    RepeatedScalarContainer,
    ScalarMapContainer,
)


def invalid_status(status: int) -> bool:
    if status == 0:
        return False

    errmsg = gmi_get_ext_errormsg().decode("utf8")
    msg = "func={}, status={}, msg={}".format(
        sys._getframe().f_back.f_code.co_name,
        status,
        errmsg,
    )
    gmsdklogger.warning(msg)
    return True


def timestamp_to_str(timestamp):
    # type: (Timestamp) -> str
    begin = datetime(1970, 1, 1, 8, 0, tzinfo=PRC_TZ)
    date = begin + timedelta(seconds=timestamp.seconds+timestamp.nanos)
    return date.strftime("%Y-%m-%d")


# 需要四舍五入的字段
_round_fields = {
    ("Tick", "open"),
    ("Tick", "high"),
    ("Tick", "low"),
    ("Tick", "price"),
    ("Quote", "bid_p"),
    ("Quote", "ask_p"),
    ("Bar", "open"),
    ("Bar", "high"),
    ("Bar", "low"),
    ("Bar", "close"),
    ("Bar", "pre_close"),
    ("Order", "price"),
    ("ExecRpt", "price"),
    ("Position", "vwap_diluted"),
    ("Position", "vwap"),
    ("Position", "vwap_open"),
    ("Position", "price"),
}


PRC_TZ = timezone(timedelta(hours=8), name="Asia/Shanghai")  # 东八区, 北京时间
TIMESTAMP_NONE = Timestamp()


def timestamp_to_datetime(ts):
    # type: (float) -> datetime
    begin = datetime(1970, 1, 1, 8, 0, tzinfo=PRC_TZ)
    return begin + timedelta(seconds=ts)


def pb_to_dict(pb, convert_to_date_str=True, include_default_value=True):
    # type: (Message, bool, bool) -> Dict
    def convert(pb, field, value):
        if isinstance(value, Timestamp):
            if value == TIMESTAMP_NONE:
                return None
            d = timestamp_to_datetime(value.seconds + value.nanos / 1e9)
            if convert_to_date_str:
                d = d.strftime("%Y-%m-%d")
            return d
        elif isinstance(value, Message):
            return pb_to_dict(value,
            convert_to_date_str=convert_to_date_str,
            include_default_value=include_default_value,
            )
        if isinstance(value, ScalarMapContainer):
            return dict(value)
        elif isinstance(value, RepeatedScalarContainer):
            return [i for i in value]
        elif isinstance(value, RepeatedCompositeContainer):
            return [convert(pb, field, i) for i in value]
        elif isinstance(value, float) and (pb.DESCRIPTOR.name, field.name) in _round_fields:
            return round(value, 4)
        else:
            return value
    result = {}
    if include_default_value:
        for field in pb.DESCRIPTOR.fields:
            value = getattr(pb, field.name)
            result[field.name] = convert(pb, field, value)
    else:
        for field, value in pb.ListFields():
            result[field.name] = convert(pb, field, value)
    return result
