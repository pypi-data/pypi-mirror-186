import glob
import os

from qtpy import QtGui

ICONS = {}
def load_icons():
    icons = glob.glob(os.path.join(os.path.dirname(__file__),"*.png"))
    for icon in icons:
        basename = os.path.splitext(os.path.basename(icon))[0]
        ICONS[basename] = QtGui.QIcon(icon)