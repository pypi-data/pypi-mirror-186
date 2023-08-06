# standard imports
import sys
import argparse
import logging

# local imports
from piknik import Basket
from piknik import Issue
from piknik.store import FileStoreFactory
from piknik.crypto import PGPSigner

logging.basicConfig(level=logging.DEBUG)

next_i = 1
def next_message_arg():
    global next_i

    r = sys.argv[next_i]

    if r[0] != '-':
        next_i += 1
        return None

    if r[1] not in ['r', 'i', 't', 'f']:
        next_i += 1
        return None

    v = sys.argv[next_i+1]
    next_i += 2
    return (r[1], v,)


argp = argparse.ArgumentParser()
argp.add_argument('-d', type=str, help='Data directory')
argp.add_argument('-s', '--sign-as', dest='s', type=str, help='PGP fingerprint of key to sign issue update with')
argp.add_argument('-r', type=str, action='append', default=[], help='Add literal message text')
argp.add_argument('-f', type=str, action='append', default=[], help='Add arbitrary file as content')
argp.add_argument('issue_id', type=str, help='Issue id to modify')
arg = argp.parse_args(sys.argv[1:])

signer = PGPSigner(default_key=arg.s, use_agent=True)
store_factory = FileStoreFactory(arg.d)
basket = Basket(store_factory, message_wrapper=signer.sign)


def main():
    messages = []
    while True:
        try:
            r = next_message_arg()
        except IndexError:
            break
        if r == None:
            continue

        if r[0] == 'r':
            messages.append('s:' + r[1])
        elif r[0] == 'f':
            messages.append('f:' + r[1])

    basket.msg(arg.issue_id, *messages)

if __name__ == '__main__':
    main()
