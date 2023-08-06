"""PTR Command Line Interface module."""

import sys
from argparse import ArgumentParser
from pathlib import Path

from .agm import agm_simulation


def cli_juice_agm(argv=None):
    """CLI JUICE PTR validation with AGM.

    By default, the metakernel used by AGM is ``juice_crema_5_0b23_1``.
    You can change this parameter with ``--mk`` flag.

    AGM produced CK file are cached but you can download
    it explicitly if you want with a ``--ck`` flag.

    """
    parser = ArgumentParser(description='Check ESA/JUICE PTR validity with AGM.')
    parser.add_argument('ptr', help='PTR/PTX input file.')
    parser.add_argument('--mk', metavar='METAKERNEL', default='juice_crema_5_0',
                        help='Metakernel to use with AGM (default: `juice_crema_5_0`).')
    parser.add_argument('--endpoint', metavar='URL', default='JUICE_API',
                        help='AGM API endpoint URL (default: `JUICE_API`).')
    parser.add_argument('--quaternions', action='store_true',
                        help='Display computed quaternions (optional).')
    parser.add_argument('--ck', metavar='FILENAME',
                        help='CK output filename (optional).')
    parser.add_argument('--log', action='store_true',
                        help='Display AGM log (optional).')
    parser.add_argument('--no-cache', action='store_false',
                        help='Disable cache (optional).')

    args, _ = parser.parse_known_args(argv)

    # check if the file exists
    if not Path(args.ptr).exists():
        sys.stderr.write(f'PTR not found: {args.ptr}\n')
        sys.exit(1)

    # Start AGM simulation
    res = agm_simulation(args.mk, args.ptr, args.endpoint, cache=args.no_cache)
    sys.stdout.write(f'AGM simulation: {res.status}\n')

    if res.success:
        if args.log:
            sys.stdout.write('Log:\n' + repr(res.log) + '\n')

        if args.quaternions:
            sys.stdout.write(f'Quaternions:\n{repr(res.quaternions)}\n')

        if args.ck:
            res.ck.save(args.ck)
            sys.stdout.write(f'AGM CK saved in `{args.ck}`.\n')
    else:
        sys.stderr.write('Log:\n' + repr(res.log) + '\n')
        sys.exit(1)
