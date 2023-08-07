"""
Function Loader
"""
from rias.compimg import *
from rias.compvideo import *


# Loader
def loader(content="None") -> None:
    options = {
        "compimg": compimg,
        "compvid": compvideo,
        "compvideo": compvideo
        }
    (lambda: None if content not in options else options[content])()
