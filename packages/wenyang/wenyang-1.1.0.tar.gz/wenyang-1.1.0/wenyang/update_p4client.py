#!/usr/bin/env python3

'''
create or update p4 client spec according to given mappings

reference:
    * perforce view syntax: https://www.perforce.com/perforce/doc.091/manuals/cmdref/o.views.html
'''

import functools
import itertools
import re
import subprocess
import logging
import sys

# ==========================================================================
# helpers
# ==========================================================================
P4_CMD_TIMEOUT = 5 # in second
run = functools.partial(subprocess.run, timeout=P4_CMD_TIMEOUT, check=True, stdout=subprocess.PIPE, universal_newlines=True)

def _get_view_maps_start_index(lines):
    if 'View:' in lines:
        return lines.index('View:') + 1
    return 0

def _get_view_maps(spec_content):
    # strip trailing spaces
    all_lines = (line.rstrip() for line in spec_content.splitlines())
    # remove comments and empty lines
    valid_lines = [line for line in all_lines if line and not line.startswith('#')]
    # get view maps
    return valid_lines[_get_view_maps_start_index(valid_lines):]

def _get_client_name(view_map_line):
    for name in re.finditer(r'(?<=\s//)(.+?)/', view_map_line):
        name = name.group(1)
        if name != 'depot':
            return name

# ==========================================================================
# API: update_p4_client(client_name, template_spec_content)
# ==========================================================================
def _metadata(client_name):
    cmd = ('p4', 'client', '-o', client_name)
    spec_lines = run(cmd).stdout.splitlines()
    if 'View:' not in spec_lines:
        raise RuntimeError("Fail to locate 'View:' in original client spec")
    return iter(spec_lines[:spec_lines.index('View:') + 1])

def _view_maps(new_client_name, spec_content):
    view_maps = _get_view_maps(spec_content)
    client_name = _get_client_name(view_maps[0])
    logging.info(f'original client name: {client_name}')
    logging.info(f'new client name: {new_client_name}')
    for view_map in view_maps:
            line = ('\t' + re.sub(r'(?<=\s//)'+re.escape(client_name), new_client_name, view_map))
            yield line

def _update_client(spec_content):
    cmd = ('p4', 'client', '-i')
    proc = run(cmd, input=spec_content)
    print(proc.stdout)

def update_p4_client(client_name, spec_content):
    'update p4 client with given spec'
    metadata = _metadata(client_name)
    view_maps = _view_maps(client_name, spec_content)
    final_spec_content = '\n'.join(itertools.chain(metadata, view_maps))
    return final_spec_content

# ==========================================================================
# API: get_file_content(file_path)
# ==========================================================================
def _get_depot_file_content(depot_file_path):
    cmd = ('p4', 'print', '-q', depot_file_path)
    return run(cmd).stdout

def _get_local_file_content(local_file_path):
    return open(local_file_path).read()

def get_file_content(file_path):
    '''
    fetch content of a file specified with either:
        local path or
        depot path in form of //depot/path/to/file
    '''
    if file_path.startswith('//depot/'):
        return _get_depot_file_content(file_path)
    return _get_local_file_content(file_path)

# ==========================================================================
# COMMAND LINE INTERFACE
# ==========================================================================
def _get_args_from_cmdline():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', default=False, action='store_true')
    parser.add_argument('--dry-run', dest='commit', default=True, action='store_false', help='do not commit the change')
    parser.add_argument('client_name', help='P4 client name')
    parser.add_argument('client_spec_path',
                        help='path to client spec file; could be either local path or depot path as //depot/path/to/your/specfile')
    return parser.parse_args()

def main():
    'command line interface'
    args = _get_args_from_cmdline()
    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.ERROR
    logging.basicConfig(level=log_level, format='[%(asctime)s - %(levelname)s] %(message)s')

    final_spec_content = update_p4_client(args.client_name, get_file_content(args.client_spec_path))

    if args.commit:
        _update_client(final_spec_content)

    if args.verbose:
        print(final_spec_content)

if __name__ == '__main__':
    
    main()
