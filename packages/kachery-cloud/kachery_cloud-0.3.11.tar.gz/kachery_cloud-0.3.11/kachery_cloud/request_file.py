from typing import Union
from dataclasses import dataclass
import os
import requests
from .load_file import load_file_info, load_file_local
from ._kachery_gateway_request import _kachery_gateway_request

@dataclass
class RequestFileResult:
    found: Union[None, bool] = None
    queued: Union[None, bool] = None
    completed: Union[None, bool] = None
    running: Union[None, bool] = None
    local: bool = False
    errored: bool = False
    error_message: str = ''
    size: Union[None, int] = None
    bytes_uploaded: Union[None, int] = None

def request_file(uri: str, *, resource: str, timeout_sec: float, ignore_local: bool=False) -> RequestFileResult:
    if not ignore_local:
        a0 = load_file_local(uri)
        if a0 is not None:
            return RequestFileResult(
                found=True,
                size=os.path.getsize(a0),
                local=True
            )
    x0 = load_file_info(uri)
    if (x0 is not None) and (x0['found']):
        return RequestFileResult(
            found=True,
            size=x0['size'],
            completed=True
        )
    proxy_url = _get_proxy_url_for_resource(resource)
    req = {
        'type': 'requestFromClient',
        'resourceName': resource,
        'request': {
            'type': 'fileUpload',
            'uri': _remove_query_string_from_uri(uri)
        },
        'timeoutMsec': timeout_sec * 1000
    }
    resp = requests.post(proxy_url + '/api', json=req)
    if resp.status_code != 200:
        raise Exception(f'Error in requestFromClient: ({resp.status_code}) {resp.reason}: {resp.text}')
    response = resp.json()
    if response['type'] != 'responseToClient':
        raise Exception('Unexpected response to requestFromClient')
    if response.get('error', ''):
        raise Exception(f'Error requesting file: {response["error"]}')
    rr = response['response']
    if rr['type'] != 'fileUpload':
        raise Exception('Unexpected fileUpload response')
    status = rr['status']
    status_str = status['status'] # 'not-found' | 'queued' | 'running' | 'completed' | 'error'
    size = status.get('size', None)
    bytes_uploaded = status.get('bytesUploaded', None)
    error_str = status.get('error', '')
    return RequestFileResult(
        found = status_str in ['queued', 'running', 'completed'],
        queued = status_str == 'queued',
        completed = status_str == 'completed',
        running = status_str == 'running',
        errored = status_str == 'error',
        error_message = error_str,
        size = size,
        bytes_uploaded = bytes_uploaded
    )

_global = {
    'proxy_urls': {}
}

def _remove_query_string_from_uri(uri: str):
    i = uri.find('?')
    if i < 0: return uri
    return uri[:i]

def _get_proxy_url_for_resource(resource: str):
    if resource in _global['proxy_urls']:
        return _global['proxy_urls'][resource]
    kachery_zone = os.environ.get('KACHERY_ZONE', 'default')
    resp = _kachery_gateway_request({
        'type': 'getResourceInfo',
        'resourceName': resource,
        'zone': kachery_zone
    })
    found = resp['found']
    if not found:
        raise Exception(f'Resource not found in zone: {resource}')
    proxy_url = resp['resource']['proxyUrl']
    _global['proxy_urls'][resource] = proxy_url
    return proxy_url
