"""AGM cache module."""

import re
from pathlib import Path
from tempfile import gettempdir

from .hash import md5_hash
from .results import AGMResults


class Cache:
    """AGM cache folder.

    Parameters
    ----------
    cache: str or pathlib.Path
        Cache folder name.

    """

    def __init__(self, cache):
        self.cache = Path(cache)
        self.cache.mkdir(parents=True, exist_ok=True)

    def __str__(self):
        return str(self.cache)

    def __repr__(self):
        n = len(self)

        if n == 0:
            n_files = 'empty'
        else:
            n_files = f'{n} entr' + ('ies' if n > 1 else 'y') + ':\n - '
            n_files += '\n - '.join([
                f.stem for f in self.content
            ])

        return f'<{self.__class__.__name__}> {self} | {n_files}'

    def __call__(self, metakernel, ptr, endpoint, ext='json'):
        return self.cache / f'{md5_hash(metakernel, ptr, endpoint)}.{ext}'

    def __len__(self):
        return len(self.content)

    def __iter__(self):
        return iter(self.content)

    def __contains__(self, key):
        return (self.cache / f'{key}.json').exists()

    def __getitem__(self, key):
        if key not in self:
            raise KeyError(key)
        return self.inspect(key)

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        self.remove(key)

    @property
    def content(self):
        """List CK and NPY files in AGM cache"""
        return sorted(
            f for f in self.cache.glob('*.json')
            if re.match(r'^[a-f\d]{32}$', f.stem)
        )

    def inspect(self, md5):
        """Inspect cached file."""
        return AGMResults(self.cache / f'{md5}.json')

    def remove(self, md5):
        """Remove the file from the cache."""
        (self.cache / f'{md5}.json').unlink(missing_ok=True)
        (self.cache / f'{md5}.ck').unlink(missing_ok=True)

    def purge(self):
        """Purge all AGM cache"""
        for fname in self:
            self.remove(fname.stem)


AGM_CACHE = Cache(Path(gettempdir()) / 'esa-ptr')
