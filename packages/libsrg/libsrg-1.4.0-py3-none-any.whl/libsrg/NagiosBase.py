#!/usr/bin/env  python3

import sys, logging
# from optparse import OptionParser
import argparse

from enum import Enum
import libsrg
from libsrg import LoggingAppBase



class NagiosReturn(Enum):
    NOCALL = -1
    OK = 0
    WARNING = 1
    CRITICAL = 2
    UNKNOWN = 3


class NagiosBase(libsrg.LoggingAppBase):

    def __init__(self):

        super(NagiosBase, self).__init__()

        self.curReturn = NagiosReturn.NOCALL
        self.curReturnStr = "nocall?"
        self.defReturn = NagiosReturn.UNKNOWN
        self.defReturnStr = "no status reported?"
        try:
            self.createParser()
            self.runTest()
        except:
            self.logger.critical("Unexpected error: %s", sys.exc_info()[0])
        finally:
            self.report()

    def createParser(self):
        usage = "usage: %prog [options]"
        self.parser = argparse.ArgumentParser(usage)
        self.parser.add_argument("-H", "--hostaddress",
                                 action="store", dest="host", default="nas0.home.goncalo.name",
                                 help="FQDN or IP of host to check via ssh")
        self.parser.add_argument("-U", "--user",
                                 action="store", dest="user", default="root",
                                 help="username at hostaddress")
        self.parser.add_argument('-v', '--verbose', help='enable verbose output', dest='verbose', action='store_true',
                                 default=False)
        self.parser.add_argument('--log-file', nargs=1, help='file to log to (default = stdout)', dest='logfile',
                                 type=str, default=None)

        self.extendParser()
        self.perform_parse()

        #FIXME old name was options
        self.options = self.args


    def nocallResult(self, retCode, retStr):
        self.defReturn = retCode
        self.defReturnStr = retStr

    def setResult(self, retCode, retStr):
        if retCode.value > self.curReturn.value:
            self.curReturn = retCode
            self.curReturnStr = retStr

    def report(self):
        if self.curReturn == NagiosReturn.NOCALL:
            self.logger.error("using nocall result")
            self.curReturn = self.defReturn
            self.curReturnStr = self.defReturnStr
        self.logger.info(f"{self.curReturn.name}={self.curReturn.value} {self.curReturnStr}")
        print(self.curReturn.name, " - ", self.curReturnStr)
        sys.exit(self.curReturn.value)

    ############### these need to be overriden in the subclass
    def extendParser(self):
        self.logger.error("createSubclassParser should be overridden in Subclass")

    def runTest(self):
        self.logger.error("runTest should be overridden in Subclass")


if __name__ == '__main__':
    print("This module cannot be run standalone")
    sys.exit(-1)
