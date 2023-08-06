"""AGM simulation module."""

from pathlib import Path

from .api import agm_api
from .results import AGMResults


def agm_simulation(metakernel, ptr, endpoint, cache=True) -> AGMResults:
    """ESA Attitude Generator Module simulation.

    Parameters
    ----------
    metakernel: str
        Metakernel id.
    ptr: str or pathlib.Path
        Pointing Timeline Request content or file.
    endpoint: str, optional
        AGM endpoint simulator. It can be an explicit API URL endpoint
        or an implicit API keyword, eg. ``'JUICE_API'``.
    cache: bool, optional
        Use cache the result of the simulation.

    Note
    ----
    Currently, AGM API requests is supported. Usage of locally installed AGM instance
    is envision in the future.

    See Also
    --------
    ptr.agm.api.agm_api, ptr.agm.AGM_CACHE

    """
    ptr_content = str(ptr).strip()

    if not ptr_content.startswith('<'):
        ptr_content = Path(ptr).read_text(encoding='utf-8').strip()

    return agm_api(metakernel, ptr_content, endpoint, cache=cache)
