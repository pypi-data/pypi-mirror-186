import httpx

from .._exception import TiebaServerError
from .._helper import pack_form_request, parse_json, raise_for_status, url


def pack_request(
    client: httpx.AsyncClient, tbs: str, fname: str, fid: int, tid: int, pid: int, is_hide: bool
) -> httpx.Request:

    data = [
        ('tbs', tbs),
        ('fn', fname),
        ('fid', fid),
        ('tid_list[]', tid),
        ('pid_list[]', pid),
        ('type_list[]', '1' if pid else '0'),
        ('is_frs_mask_list[]', int(is_hide)),
    ]

    request = pack_form_request(
        client,
        url("https", "tieba.baidu.com", "/mo/q/bawurecoverthread"),
        data,
    )

    return request


def parse_response(response: httpx.Response) -> None:
    raise_for_status(response)

    res_json = parse_json(response.content)
    if code := res_json['no']:
        raise TiebaServerError(code, res_json['error'])
