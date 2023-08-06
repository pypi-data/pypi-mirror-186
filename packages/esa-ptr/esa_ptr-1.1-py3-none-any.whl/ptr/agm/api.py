"""AGM API module."""

import json
from datetime import datetime
from urllib import request

from .cache import AGM_CACHE
from .results import AGMResults


AGM_URL_ENDPOINTS = {
    'JUICE_API': 'https://juicept.esac.esa.int/agm',
}


def agm_api(metakernel, ptr, url, cache=True):
    """Call AGM through a REST API.

    Parameters
    ----------
    metakernel: str
        Metakernel id.
    ptr: str
        Pointing Timeline Request.
    url: str, optional
        Explicit AGM URL endpoint. You can also use the mission
        name listed in ``AGM_URL_ENDPOINTS`` like ``'JUICE_API'``.
    cache: bool, optional
        Use cache the response if present locally.

    Raises
    ------
    ValueError
        If the URL endpoint is unknown.

    """
    if url in AGM_URL_ENDPOINTS:
        endpoint = AGM_URL_ENDPOINTS[url]
    elif '://' in url:
        endpoint = url
    else:
        raise ValueError(f'Unknown URL: {url}')

    fname = AGM_CACHE(metakernel, ptr, endpoint)

    if cache and fname.exists():
        return AGMResults(fname)

    payload = json.dumps({
        'metakernel': metakernel,
        'ptr_content': str(ptr),
    }).encode('utf-8')

    req = request.Request(endpoint, data=payload)

    with request.urlopen(req) as resp:
        results = {
            'endpoint': endpoint,
            'metakernel': metakernel,
            'ptr': str(ptr).strip(),
            'results': json.load(resp),
            'created': datetime.now().isoformat(timespec='seconds'),
            'cache': {
                'location': str(AGM_CACHE),
                'md5_hash': fname.stem,
            } if cache else False,
        }

    if cache:
        with fname.open('w', encoding='utf-8') as f:
            json.dump(results, f)

    return AGMResults(results)
