from PyQt6 import uic, QtWidgets
from F import LIST, DICT, RE
from F.CLASS import FairClass
from .FTemplates import DEFAULT_TEMPLATE

"""
 -> Everything/Widget should be named exactly the name
    : QtDesigner -> btnSearch
    : Class Variable -> btnSearch
    : Action Function -> onClick_btnSearch
"""

VIEW_ELEMENTS = ["Button", "List", "CheckBox", "Edit", ""]
LISTENER_TYPES = {
    "onClick_": "clicked",
    "onDoubleClick_": "itemDoubledClicked",
    "onReleased_": "released",
    "onToggled_": "toggled",
    "onStateChanged": "stateChanged",
    "onTextChanged_": "textChanged",
    "onValueChanged": "valueChanged"
}


def launchUI(windowObj):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = windowObj()
    sys.exit(app.exec())


LISTENER = lambda listenerType, funcName: f"{listenerType}{funcName}"


class FairDialog(QtWidgets.QDialog, FairClass):
    ui = None

    def __init__(self):
        super(FairDialog, self).__init__()

    def bind_ui(self, uiFilePath=DEFAULT_TEMPLATE):
        self.ui = uic.loadUi(uiFilePath, self)
        self.binder()

    """ Core View Bindings """

    def binder(self):
        """ AutoMagically binds View Elements from ui file. """
        for item in DICT.yieldThis(self.ui.__dict__):
            viewName = LIST.get(0, item)
            viewObj = LIST.get(1, item)
            viewType = type(viewObj)
            # -> Variable Bindings
            setattr(self, viewName, self.findChild(viewType, viewName))
            # -> Action Bindings
            """ We don't want to bind actions to everything. """
            if RE.contains_any(VIEW_ELEMENTS, str(viewType)):
                self._set_actions(viewName)

    def _set_actions(self, viewName):
        for listener in DICT.yieldThis(LISTENER_TYPES):
            funcName = LIST.get(0, listener)
            connectType = LIST.get(1, listener)
            attrVar = self.get_attribute(viewName)
            onFunction = self.get_func(f"{funcName}{viewName}")
            if not onFunction:
                continue
            try:
                if connectType == "clicked":
                    attrVar.clicked.connect(onFunction)
                elif connectType == "itemDoubledClicked":
                    attrVar.itemDoubleClicked.connect(onFunction)
                elif connectType == "toggled":
                    attrVar.toggled.connect(onFunction)
                elif connectType == "released":
                    attrVar.released.connect(onFunction)
                elif connectType == "textChanged":
                    attrVar.textChanged.connect(onFunction)
                elif connectType == "valueChanged":
                    attrVar.valueChanged.connect(onFunction)
                elif connectType == "stateChanged":
                    attrVar.stateChanged.connect(onFunction)
            except:
                continue

    """ Action Examples """

    def onClick_ButtonName(self, item):
        """ onClick_ButtonName(item) """
        pass

    def onDoubleClick_ListName(self, item):
        """ onDoubleClick_ListName(item) """
        pass

    def onToggled_toggleName(self, item):
        """ onToggled_toggleName(item) """
        pass

    def onTextChanged_editName(self, item):
        """ onTextChanged_editName(item) """
        pass