from qtpy import QtWidgets

class InspectDataDialog(QtWidgets.QDialog):

    def __init__(self,data_info,parent):
        """
        """
        super(InspectDataDialog,self).__init__(parent)

        self._build()

        self.setWindowTitle(data_info["variable"])

    def _build(self):
        """
        """
