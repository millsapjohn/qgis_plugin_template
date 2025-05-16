from .flyoutdocks import FlyoutDocksPlugin

def ClassFactory(iface):
    return FlyoutDocksPlugin(iface)
