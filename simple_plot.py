import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np

#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

x = np.random.normal(size=1000)
y = np.random.normal(size=1000)

p1 = win.addPlot(title="Basic array plotting", x=x, y=y, pen=None, symbol='d')


# pg.plot(x, y, pen=None, symbol='o')  ## setting pen=None disables line drawing

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
