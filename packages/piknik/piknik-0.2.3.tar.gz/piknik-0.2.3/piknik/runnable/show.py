# standard imports
import io
import os
import sys
import argparse
import logging
import tempfile
from base64 import b64decode
from email.utils import parsedate_to_datetime
import importlib

# local imports
from piknik import Basket
from piknik import Issue
from piknik.store import FileStoreFactory
from piknik.crypto import PGPSigner

logging.basicConfig(level=logging.WARNING)
logg = logging.getLogger()

argp = argparse.ArgumentParser()
argp.add_argument('-d', type=str, help='Data directory')
argp.add_argument('-f', '--files', dest='f', action='store_true', help='Save attachments to filesystem')
argp.add_argument('-o', '--files-dir', dest='files_dir', type=str, help='Directory to output saved files to')
argp.add_argument('-r', '--renderer', type=str, default='default', help='Renderer module for output')
argp.add_argument('-s', '--state', type=str, action='append', default=[], help='Limit results to state(s)')
argp.add_argument('--show-finished', dest='show_finished', action='store_true', help='Include finished issues')
#argp.add_argument('--reverse', action='store_true', help='Sort comments by oldest first')
argp.add_argument('issue_id', type=str, nargs='?', default=None, help='Issue id to show')
arg = argp.parse_args(sys.argv[1:])

store_factory = FileStoreFactory(arg.d)
basket = Basket(store_factory)

gpg_home = os.environ.get('GPGHOME')

renderer_s = arg.renderer
if renderer_s == 'default':
    renderer_s = 'piknik.render.plain'
elif renderer_s == 'html':
    renderer_s = 'piknik.render.html'

m = None
try:
    m = importlib.import_module(renderer_s)
except ModuleNotFoundError:
    renderer_s = 'piknik.render.' + renderer_s
    m = importlib.import_module(renderer_s)

accumulator = None
accumulator_f = None

def set_accumulator(issue_id=None):
    global accumulator_f
    global accumulator
    global m
    if arg.files_dir != None:
        fb = None
        if issue_id == None:
            fb = 'index.html'
        else:
            fb = issue_id + '.html'
        fp = os.path.join(arg.files_dir, fb)
        accumulator_f = open(fp, 'w')
        accumulator = m.Accumulator(w=accumulator_f)
        return accumulator.add
    return None


def reset_accumulator():
    global accumulator_f
    global accumulator
    if accumulator_f != None:
        accumulator_f.close()
        accumulator_f = None
        issues = accumulator.issues
        accumulator = None
        return issues
    return []


def main():
    issues = []
    if arg.issue_id:
        issues.append(arg.issue_id)

    if arg.issue_id == None:
        accumulator = set_accumulator()
        renderer = m.Renderer(basket, accumulator=accumulator)
        renderer.apply()
        issues = reset_accumulator()

    for issue_id in issues:
        accumulator = set_accumulator(issue_id=issue_id)
        issue = basket.get(issue_id)
        tags = basket.tags(issue_id)
        state = basket.get_state(issue_id)
        verifier = PGPSigner(home_dir=gpg_home, skip_verify=False)
        renderer = m.Renderer(basket, wrapper=verifier, accumulator=accumulator)

        renderer.apply_begin()
        renderer.apply_issue(state, issue, tags)
        renderer.apply_end()
        
        reset_accumulator()
    

if __name__ == '__main__':
    main()
