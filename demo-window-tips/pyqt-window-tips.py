import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class ToolTip(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('WIZ')

		self.setToolTip('This is a Widget')
		QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish',10))

app = QtGui.QApplication(sys.argv)
tooltip = ToolTip()
tooltip.show()
sys.exit(app.exec_())

