"""PTR blocks utils module."""

from functools import wraps

from .block import BlockOverlapError, ElementBlock


def is_block(func):
    """Check if an element is an element block."""
    @wraps(func)
    def wrap(self, element):
        """Wrapped function."""
        if not isinstance(element, ElementBlock):
            raise TypeError(f'`{element}` is not an ElementBlock.')
        return func(self, element)
    return wrap


def after(latest, new_block) -> bool:
    """Check if the new block is after the latest one."""
    if latest.end <= new_block.start:
        return True

    raise BlockOverlapError(f'New block:\n{new_block}\n\nshould start after:\n\n{latest}')


def before(first, new_block) -> bool:
    """Check if the new block is before the first one."""
    if new_block.end <= first.start:
        return True

    raise BlockOverlapError(f'New block:\n{new_block}\n\nshould end before:\n\n{first}')


def between(block_1, block_2, new_block) -> bool:
    """Check if the new block is between 2 blocks."""
    return after(block_1, new_block) and before(block_2, new_block)


def gap(block_1, block_2) -> bool:
    """Check if 2 blocks have a gap between them."""
    return block_1.end < block_2.start or block_1.start > block_2.end


def insort(blocks: list, new_block):
    """Insert a new block in chronological order without overlap."""
    if not blocks:
        blocks.append(new_block)

    elif blocks[-1].start <= new_block.start and after(blocks[-1], new_block):
        blocks.append(new_block)

    else:
        for i in range(len(blocks) - 2, -1, -1):
            if blocks[i].start <= new_block.start:
                if between(blocks[i], blocks[i + 1], new_block):
                    blocks.insert(i + 1, new_block)
                    break
        else:
            if before(blocks[0], new_block):
                blocks.insert(0, new_block)
