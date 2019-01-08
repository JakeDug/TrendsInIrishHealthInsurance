from graph import createPlotGraph
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b_createGraph = QPushButton(win)
   b_createGraph.setText("Create Graph")
   b_createGraph.move(50,20)
   b_createGraph.clicked.connect(b_createGraph_clicked)


   win.setGeometry(100,100,200,100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

def b_createGraph_clicked():
   createPlotGraph('VhiJan2018.csv')

if __name__ == '__main__':
   window()
