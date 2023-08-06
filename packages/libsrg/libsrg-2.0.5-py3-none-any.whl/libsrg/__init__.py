# manually ordered to prevent loops
from logging import getLevelName
from importlib.metadata import version

from .LevelBanner import LevelBanner
from .LoggerGUIProxy import GUI_CONFIGURE, GUI_NEW_LINE, GUI_FREEZE_LINE
from .LoggerGUIProxy import LoggerGUIProxy
from .LoggingCounter import LoggingCounter
from .LoggingWatcher import LoggingWatcher
from .Runner import Runner
from .Runner2 import Runner2

# middle layer
from .LoggingAppBase import LoggingAppBase
from .LoggingAppBase import SampleApp
from .NagiosBase import NagiosBase, NagiosReturn

# top layer
from .ReZFS import ReZFS
from .Stage0 import Stage0
from .LoggerGUI import LoggerGUI

# from .Info import Info

def version():
   ver = version('libsrg')
   print(f"In version {ver} {__file__} ")

def level2str(lev) -> str:
    if not isinstance(lev, str):
        lev = getLevelName(lev)
    return lev


def level2int(lev) -> int:
    if isinstance(lev, str):
        lev = getLevelName(lev)
    return lev
