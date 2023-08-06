import sys
import argparse
import logging

from piknik import Basket
from piknik import Issue
from piknik.store import FileStoreFactory

logging.basicConfig(level=logging.DEBUG)
logg = logging.getLogger()


argp = argparse.ArgumentParser()
argp.add_argument('-d', type=str, help='Data directory')
argp.add_argument('--accept', action='store_true', help='Accept proposed issue')
argp.add_argument('--block', action='store_true', help='Set issue as blocked')
argp.add_argument('--unblock', action='store_true', help='Set issue as unblocked')
argp.add_argument('--finish', action='store_true', help='Set issue as finished (alias of -s finish)')
argp.add_argument('-s', '--state', type=str, help='Move to state')
argp.add_argument('-t', '--tag', type=str, action='append', default=[], help='Add tag to issue')
argp.add_argument('-u', '--untag', type=str, action='append', default=[], help='Remove tag from issue')
#argp.add_argument('-f', '--file', type=str, action='append', help='Add message file part')
#argp.add_argument('-m', '--message', type=str, action='append', default=[], help='Add message text part')
argp.add_argument('-a', '--assign', type=str, action='append', default=[], help='Assign given identity to issue')
argp.add_argument('--unassign', type=str, action='append', default=[], help='Unassign given identity from issue')
argp.add_argument('-o', '--owner', type=str, help='Set given identity as owner of issue')
argp.add_argument('--dep', action='append', default=[], type=str, help='Set issue dependency')
argp.add_argument('--undep', action='append', default=[], type=str, help='Remove issue dependency')
argp.add_argument('issue_id', type=str, help='Issue id to modify')
arg = argp.parse_args(sys.argv[1:])

store_factory = FileStoreFactory(arg.d)
basket = Basket(store_factory)


def main():
    o = basket.get(arg.issue_id)

    if arg.block:
        basket.block(arg.issue_id)
    elif arg.unblock:
        basket.unblock(arg.issue_id)

    if arg.state != None:
        m = getattr(basket, 'state_' + arg.state)
        m(arg.issue_id)
    elif arg.finish:
        basket.state_finish(arg.issue_id)
    elif arg.accept:
        if basket.get_state(arg.issue_id) != 'PROPOSED':
            raise ValueError('Issue already accepted')
        basket.advance(arg.issue_id)

    for v in arg.tag:
        basket.tag(arg.issue_id, v)

    for v in arg.untag:
        basket.untag(arg.issue_id, v)

    for v in arg.unassign:
        basket.unassign(arg.issue_id, v)

    for v in arg.assign:
        basket.assign(arg.issue_id, v)
 
    for v in arg.undep:
        basket.undep(arg.issue_id, v)

    for v in arg.dep:
        basket.dep(arg.issue_id, v)

    if arg.owner:
        basket.owner(arg.issue_id, arg.owner)


if __name__ == '__main__':
    main()
