import os
import time

from helios.defaults import DEFAULT_HS_API_ENDPOINT
HS_API_ENDPOINT = os.environ.get('HS_API_ENDPOINT') or DEFAULT_HS_API_ENDPOINT


def encode_id_as_hex_string(id: int, length: int = 16) -> str:
    return id.to_bytes(length=length, byteorder="big", signed=False).hex()


def get_trace_vis_url(trace_id, source, span_id='') -> str:
    url = f'{HS_API_ENDPOINT}?actionTraceId={trace_id}'
    if bool(source):
        url += f'&source={source}'

    if bool(span_id):
        url += f'&spanId={span_id}'

    current_timestamp = int(round(time.time() * 1000))
    url += f'&timestamp={current_timestamp}'

    return url
