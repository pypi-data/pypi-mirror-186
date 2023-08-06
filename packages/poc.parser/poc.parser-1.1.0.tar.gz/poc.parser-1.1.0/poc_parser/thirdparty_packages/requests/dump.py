from .compat import urlparse

__all__ = ('dump_response', 'dump_request')

HTTP_VERSIONS = {
    9: b'0.9',
    10: b'1.0',
    11: b'1.1',
}


def _get_proxy_information(response):
    if getattr(response.connection, 'proxy_manager', False):
        proxy_info = {}
        request_url = response.request.url
        if request_url.startswith('https://'):
            proxy_info['method'] = 'CONNECT'

        proxy_info['request_path'] = request_url
        return proxy_info
    return {}


def _coerce_to_bytes(data):
    if not isinstance(data, bytes) and hasattr(data, 'encode'):
        data = data.encode('utf-8')
    # Don't bail out with an exception if data is None
    return data if data is not None else b''


def _format_header(name, value):
    return (_coerce_to_bytes(name) + b': ' + _coerce_to_bytes(value) +
            b'\r\n')


def _build_request_path(url, proxy_info):
    uri = urlparse(url)
    proxy_url = proxy_info.get('request_path')
    if proxy_url is not None:
        request_path = _coerce_to_bytes(proxy_url)
        return request_path, uri

    request_path = _coerce_to_bytes(uri.path)
    if uri.query:
        request_path += b'?' + _coerce_to_bytes(uri.query)

    return request_path, uri


def dump_request(response):
    request_headers = bytearray()
    request = response.request
    proxy_info = _get_proxy_information(response)

    method = _coerce_to_bytes(proxy_info.pop('method', request.method))
    request_path, uri = _build_request_path(request.url, proxy_info)

    request_headers.extend(method + b' ' + request_path + b' HTTP/1.1\r\n')

    headers = request.headers.copy()
    host_header = _coerce_to_bytes(headers.pop('Host', uri.netloc))
    request_headers.extend(b'Host: ' + host_header + b'\r\n')

    for name, value in headers.items():
        request_headers.extend(_format_header(name, value))

    request_headers = request_headers.decode("utf-8")
    return f"{request_headers}\r\n{request.body if request.body else ''}"


def dump_response(response):
    response_headers = bytearray()
    raw = response.raw

    version_str = HTTP_VERSIONS.get(raw.version, b'?')

    response_headers.extend(b'HTTP/' + version_str + b' ' +
                str(raw.status).encode('ascii') + b' ' +
                _coerce_to_bytes(response.reason) + b'\r\n')

    headers = raw.headers
    for name in headers.keys():
        for value in headers.getlist(name):
            response_headers.extend(_format_header(name, value))

    response_headers = response_headers.decode("utf-8")
    return f"{response_headers}\r\n{response.text}"


def dump_all(response):
    data = ""
    history = list(response.history[:])
    history.append(response)
    for res in history:
        data += dump_request(res)
        data += "\r\n"
        data += dump_response(res)
        data += "\r\n"
    return data