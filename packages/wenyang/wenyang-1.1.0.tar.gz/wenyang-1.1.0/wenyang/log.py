import argparse
import collections
import json

from urllib.error import HTTPError
from urllib.request import Request, urlopen

import enum

class StatusEnum(enum.IntEnum):
    PASS = 0
    FAIL = 1
    UNKNOWN = 2

def _parse_args():

    def enum_help_string(enum_class):
        data = dict((entry.name, entry.value) for entry in enum_class.__members__.values())
        return 'int value representing one of %s' % str(data)

    def StatusEnumType(value):
        value = int(value)
        StatusEnum(value)
        return value

    Version = collections.namedtuple('Version', ['major', 'minor', 'maintenance', 'build'])
    def VersionType(value):
        Version(*map(int, value.split('.')))
        return value

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--project', required=True)
    parser.add_argument('--version', required=True, type=VersionType, help='version in form of %s, where every field is an integer value' % '.'.join(Version._fields))
    parser.add_argument('--category', required=True)
    parser.add_argument('--status', default=0, type=StatusEnumType, help=enum_help_string(StatusEnum))
    return parser.parse_args()

def post_data(url, **data):
    params = json.dumps(data).encode('utf8')
    request = Request(url, data=params, headers={'Content-Type': 'application/json; charset=utf-8'})
    try:
        return urlopen(request).read().decode()
    except HTTPError as e:
        return json.dumps(dict(status='error', message=e.read().decode()))

def main():
    'command line interface'
    args = _parse_args()
    print(post_data(args.url, project=args.project, version=args.version, category=args.category, status=args.status))

if __name__ == '__main__':
    main()
