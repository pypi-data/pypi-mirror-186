import logging
import datetime
import os


class Logger(object):
    __msgfmt = '%(asctime)s.%(msecs)03d | %(filename)s:%(funcName)s[%(lineno)d] | %(levelname)s : %(message)s'
    __datefmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self, filename=None):
        if filename is None:
            filename = ''
        logname = '{:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())+filename
        self.logger = logging.getLogger(logname)
        self.__checkFilePath(filename)
        self.__setupFileLog(filename)
        self.__setupConsoleLog()

    def __setupFileLog(self, file):
        if file is None or len(file) == 0:
            return
        formatter = logging.Formatter(self.__msgfmt)
        formatter.datefmt = self.__datefmt
        file_handler = logging.FileHandler(file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
        self.logger.addHandler(file_handler)

    def __setupConsoleLog(self):
        formatter = logging.Formatter(self.__msgfmt)
        formatter.datefmt = self.__datefmt
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(console_handler)

    def __checkFilePath(self, filename):
        arr = filename.split('/')
        if len(arr) == 1:
            return
        makeFilePath(filename)

    def d(self, *args):
        msg = ' '.join(['%s'%i for i in args])
        self.logger.debug(msg, stacklevel=2)

    def i(self, *args):
        msg = ' '.join(['%s'%i for i in args])
        self.logger.info(msg, stacklevel=2)

    def w(self, *args):
        msg = ' '.join(['%s'%i for i in args])
        self.logger.warning(msg, stacklevel=2)

    def e(self, *args):
        msg = ' '.join(['%s'%i for i in args])
        self.logger.error(msg, stacklevel=2)

    def exc(self, *args):
        msg = ' '.join(['%s'%i for i in args])
        self.logger.exception(msg, stacklevel=3)

    def x(self, *args):
        msg = ' '.join(['%s'%i for i in args])
        self.logger.critical(msg, stacklevel=2)


def makeFilePath(path):
    arr = path.split('/')
    if len(arr) == 1:
        return
    filepath = os.path.join(*arr[:-1])
    if os.path.exists(filepath):
        return
    paths = filepath.split('/')
    for i in range(len(paths)):
        folder = '/'.join(paths[:i + 1])
        if not os.path.exists(folder):
            os.mkdir(folder)
    return filepath

import json
def test():
    log = Logger()
    log.d('debug', 1, 'a', {'k':'v'})
    log.i('info', 'some info')
    log.w('warning', 'some warning', json.dumps({'hello':{'key':'world'}}))
    log.e('error', 123, 3*5)
    try:
        a = 1/0
        log.d(a)
    except:
        log.exc('做除法的时候出错')
    log.x('critical', -1, json.dumps([1,2,3]))
    pass


if __name__ == '__main__':
    test()
