"""PTR SLEW block."""

from ..element import Element


# An attitude slew is implemented by inserting a slew block in the PTR.
# A slew block must be placed in between two observation blocks.
# The duration of slew blocks is defined implicitly by the end time
# of the previous observation block and the start time of the following
# observation block. A slew block has the syntax: `<block ref="SLEW" />`
SLEW_BLOCK = Element('block', ref='SLEW')
SLEW_BLOCK.freeze()
