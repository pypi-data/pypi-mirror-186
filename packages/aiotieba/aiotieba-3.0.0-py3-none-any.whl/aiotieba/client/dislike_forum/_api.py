import time

import httpx

from .._classdef.core import TiebaCore
from .._exception import TiebaServerError
from .._helper import APP_BASE_HOST, pack_form_request, parse_json, raise_for_status, sign, url


def pack_request(client: httpx.AsyncClient, core: TiebaCore, fid: int) -> httpx.Request:

    data = [
        ('BDUSS', core.BDUSS),
        ('_client_version', core.main_version),
        (
            'dislike',
            f"""[{{"tid": 1, "dislike_ids": 7, "fid": {fid}, "click_time": {int(time.time() * 1000)}}}]""",
        ),
        ('dislike_from', "homepage"),
    ]

    request = pack_form_request(
        client,
        url("http", APP_BASE_HOST, "/c/c/excellent/submitDislike"),
        sign(data),
    )

    return request


def parse_response(response: httpx.Response) -> None:
    raise_for_status(response)

    res_json = parse_json(response.content)
    if code := int(res_json['error_code']):
        raise TiebaServerError(code, res_json['error_msg'])
