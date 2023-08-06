import httpx

from .._exception import TiebaServerError
from .._helper import pack_form_request, parse_json, raise_for_status, url


def pack_request(client: httpx.AsyncClient, tbs: str, fname: str, user_id: int) -> httpx.Request:

    data = [
        ('tbs', tbs),
        ('user_id', user_id),
        ('word', fname),
        ('ie', 'utf-8'),
    ]

    request = pack_form_request(
        client,
        url("http", "tieba.baidu.com", "/bawu2/platform/addBlack"),
        data,
    )

    return request


def parse_response(response: httpx.Response) -> None:
    raise_for_status(response)

    res_json = parse_json(response.content)
    if code := int(res_json['errno']):
        raise TiebaServerError(code, res_json['errmsg'])
