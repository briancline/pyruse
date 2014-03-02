from __future__ import print_function
from pyruse.versions import (all_releases, all_versions, last_release,
                             last_version, series_versions, series_releases,
                             PYTHON_DOWNLOAD_URL)
from argparse import ArgumentParser


def versions_main():
    parser = ArgumentParser(
        description='Outputs the latest version of Python, or the latest in a '
                    'specific series or set of series.')
    parser.add_argument('series', nargs='*',
                        help='the version series (e.g., 2, 2.7, 3.3, etc.)')
    parser.add_argument('-d', '--dev', dest='dev', action='store_true',
                        help='include dev versions')
    parser.add_argument('-a', '--all', dest='all', action='store_true',
                        help='show all rather than just the latest')
    parser.add_argument('-i', '--ignore-unknown', dest='ignore_unknown',
                        action='store_true',
                        help='ignore unknown series (otherwise outputs None)')
    parser.add_argument('-u', '--source-urls', dest='source_urls',
                        action='store_true',
                        help='outputs source tarball URLs for each known '
                             'version (assumes --ignore-unknown, ignores '
                             ' --dev)')

    args = parser.parse_args()

    ## TODO: REWRITE THIS CONTEMPTABLE MESS. NO MORE LIES.

    results = []

    if not args.series and not args.dev:
        results.append(last_release() if not args.all else all_releases())

    elif not args.series:
        results.append(last_version() if not args.all else all_versions())

    elif args.all:
        for s in args.series:
            vers = series_versions(s) if args.dev else series_releases(s)

            if not vers and args.ignore_unknown:
                continue

            results.append(vers)

    else:
        for s in args.series:
            ver = last_version(s) if args.dev else last_release(s)

            if not ver and args.ignore_unknown:
                continue

            results.append(ver)

    line = '%(v)s'
    if args.source_urls:
        line = PYTHON_DOWNLOAD_URL

    for result in results:
        if isinstance(result, str):
            print(line % {'v': result})
        elif not result and not (args.ignore_unknown or args.source_urls):
            print(None)
        else:
            print('\n'.join([line % {'v': r} for r in result]))
