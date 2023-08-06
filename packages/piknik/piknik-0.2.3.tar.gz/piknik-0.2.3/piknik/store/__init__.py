# standard imports
import os
import uuid

# external imports
from shep.store.file import SimpleFileStoreFactory
from shep.persist import PersistedState
from leveldir.hex import HexDir


def default_formatter(hx):
    return hx.lower()


class MsgDir(HexDir):

    def __init__(self, root_path):
        super(MsgDir, self).__init__(root_path, 16, levels=2, prefix_length=0, formatter=default_formatter)


    def __check(self, key, content, prefix):
        pass


    def get(self, k):
        u = uuid.UUID(k)
        fp = self.to_filepath(u.hex)
        f = None
        f = open(fp, 'rb')
        r = f.read()
        f.close()
        return r


    def key_to_string(self, k):
        u = uuid.UUID(bytes=k)
        return u.bytes.hex()


    def put(self, k, v):
        u = uuid.UUID(k)
        print('putting {}'.format(u.bytes.hex()))
        return self.add(u.bytes, v)


class FileStoreFactory:

    def __init__(self, directory=None):
        if directory == None:
            directory = os.path.join('.', '.piknik')
        self.directory = directory


    def create_states(self, logger=None, default_state=None, verifier=None):
        factory = SimpleFileStoreFactory(self.directory).add
        return PersistedState(factory, 6, logger=logger, verifier=verifier, default_state=default_state)

    
    def create_tags(self, logger=None, default_state=None, verifier=None):
        directory = os.path.join(self.directory, '.tags')
        os.makedirs(directory, exist_ok=True)
        factory = SimpleFileStoreFactory(directory)
        state = PersistedState(factory.add, 0, logger=logger, check_alias=False, default_state='untagged')
        aliases = []
        for k in factory.ls():
            if k == 'UNTAGGED':
                continue
            elif k[0] == '_':
                aliases.append(k)
                continue
            state.add(k)

        for v in aliases:
            s = state.from_elements(v)
            state.alias(v, s)
                
        return state


    def create_messages(self):
        d = os.path.join(self.directory, '.msg')
        return MsgDir(d)
