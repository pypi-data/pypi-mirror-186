"""AGM hashing module."""

import json
from hashlib import md5


def md5_hash(metakernel: str, ptr: str, endpoint: str) -> str:
    """MD5 inputs hashing method."""
    return md5(json.dumps({
        'endpoint': endpoint,
        'metakernel': metakernel,
        'ptr': str(ptr).strip(),
    }).encode('utf-8')).hexdigest()
