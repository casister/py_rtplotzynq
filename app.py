# from multiprocessing import freeze_support
import sys

from PyQt5 import QtWidgets
from py_ui import mainWindow
from common.architecture import Architecture
from common.cl_arguments import *
from common.logger import Logger as Log
from constants.constants import PlotConstants
from constants.constants import MinimalPython

TAG = "RTAcqPlot"


class RTAcqPlot:
    def __init__(self, argv=sys.argv):
        # freeze_support()
        self._args = self._init_logger()
        # #self._app = QtGui.QApplication(argv)
        # self._app = QtGui.QApplication(argv)
        self._app = QtWidgets.QApplication(sys.argv)

    def run(self):
        if Architecture.is_python_version(MinimalPython.major, minor=MinimalPython.minor):
            Log.i(TAG, "Starting RT Plot for Zynq")
            win = mainWindow.MainWindow()
            win.setWindowTitle("{} - {}".format(PlotConstants.app_title, PlotConstants.app_version))
            # win.show()
            self._app.exec()

            Log.i(TAG, "Finishing RTGraph\n")
            win.close()
        else:
            self._fail()
        self.close()

        # self.plot = MainWindow()
        # # win = mainWindow.MainWindow()
        # #     win.setWindowTitle("{} - {}".format(Constants.app_title, Constants.app_version))
        # self.plot.show()
        # self._app.exec()

        #           win = mainWindow.MainWindow()
        # win.show()

        # self.plot_view = QtWidgets.QWidget()
        # self.ui = Ui_plot_view()
        # self.ui.setupUi(self.plot_view)
        # self.plot_view.show()
        #           self._app.exec()

    # plot_view = QtWidgets.QWidget()
    # ui = Ui_plot_view()
    # ui.setupUi(plot_view)
    # plot_view.show()

    def close(self):
        self._app.exit()
        Log.close()
        sys.exit()

    @staticmethod
    def _init_logger():
        args = Arguments()
        args.create()
        args.set_user_log_level()
        return args

    @staticmethod
    def _fail():
        txt = str("RTGraph requires Python {}.{} to run"
                  .format(MinimalPython.major, MinimalPython.minor))
        Log.e(TAG, txt)


if __name__ == '__main__':
    RTAcqPlot().run()
