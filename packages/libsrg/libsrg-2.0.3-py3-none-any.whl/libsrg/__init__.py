# manually ordered to prevent loops
from logging import getLevelName
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
from .Info import Info
from .Stage0 import Stage0
from .LoggerGUI import LoggerGUI


def level2str(lev) -> str:
    if not isinstance(lev, str):
        lev = getLevelName(lev)
    return lev


def level2int(lev) -> int:
    if isinstance(lev, str):
        lev = getLevelName(lev)
    return lev
