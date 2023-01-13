from FQt import FairUI


class FQtBaseApp(FairUI):

    def __init__(self, uiFile):
        super(FQtBaseApp, self).__init__()
        self.bind_ui(uiFilePath=uiFile)
        self.init()
        self.do_refresh()
        self.show()

    def init(self):
        """ Overwrite Method for 'init' Flow """
        pass

    def do_refresh(self):
        pass
