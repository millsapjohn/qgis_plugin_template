from qgis.core import QgsApplication
from qgis.PyQt.QtWidgets import QDockWidget, QMainWindow
from qgis.PyQt.QtCore import Qt
from qgis.utils import iface
import os

class FlyoutDocksPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.instance = QgsApplication.instance()

    def initGui(self):
        # TODO: get list of docks in each DockWidgetArea
        # TODO: for each widget, resize and move to the size of a button
        # TODO: overlay with the button
        # TODO: on button press, expand to full dimensions of DockWidgetArea
        # TODO: keep button in place, press again to minimize
        # TODO: enable a keyboard shortcut for minimizing the current widget
        # TODO: ensure that it skips the CivilTools command line
        pass

    def unload(self):
        # TODO: restore all docks to their previous configuration(?)
        pass
