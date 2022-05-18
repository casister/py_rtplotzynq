# from random import randint
# import pyqtgraph as pg
import numpy as np
from PyQt5 import QtWidgets, QtCore
from common.cl_arguments import *
from common.logger import Logger as Log
from constants.constants import PlotConstants
from py_ui.plot_cs import Ui_plot_view
from ZedBoardRdWrSerial.ZedRdWrS import Controller

# from run_processes import Worker

TAG = "MainWindow"


class MainWindow(QtWidgets.QMainWindow):  # MainWindow(QtGui.QMainWindow):
    """
    Handles the ui elements and connects to worker service to execute processes.
    """

    def __init__(self):  # , port=None, bd=115200, samples=500):
        """
        Initializes values for the UI.
        :param port: Default port name to be used. It will also disable scanning available ports.
        :type port: str.
        :param bd: Default baud rate to be used. It will be added to the common baud rate list if not available.
        :type bd: int.
        :param samples: Default samples per second to be shown in the plot.
        :type samples: int.
        """
        # QtGui.QMainWindow.__init__(self)
        QtWidgets.QMainWindow.__init__(self)

        # self.app = QtWidgets.QApplication(sys.argv)
        # self.ZedRWS = Ui_plot_view() # ZedRdWrS.Controller(Ui_plot_view)

        self.ptr = None
        self.main_window = QtWidgets.QWidget()
        self.ui = Ui_plot_view()
        self.tet = Controller(self.ui)
        self.ui.setupUi(self.main_window)
        self.zedcontroller = Controller(self.ui)
        self.main_window.show()

        # configures
        # self.ui.cBox_Source.addItems(Constants.app_sources)
        self._configure_plot()

        # enable ui
        self._enable_ui(True)

        self._configure_timers()
        self._connect_signals_to_methods()

        # self.ui = Ui_plot_view()
        # self.ui.setupUi(self.plot_view)
        # signals to plot
        self.x1 = list(range(100))
        self.x2 = list(range(100))
        self.sensor1 = np.random.normal(size=100)  # list(range(100))
        self.sensor2 = np.random.normal(size=100)  # list(range(100))
        self.sensor3 = np.random.normal(size=100)  # list(range(100))
        self.sensor4 = np.random.normal(size=100)  # list(range(100))
        self.sensor5 = np.random.normal(size=100)  # list(range(100))
        self.sensor6 = np.random.normal(size=100)  # list(range(100))
        self.sensor7 = np.random.normal(size=100)  # list(range(100))
        self.sensor8 = np.random.normal(size=100)  # list(range(100))
        self.sensor9 = np.random.normal(size=100)  # list(range(100))
        self.sensor10 = np.random.normal(size=100)  # list(range(100))
        self.sensor11 = np.random.normal(size=100)  # list(range(100))
        self.sensor12 = np.random.normal(size=100)  # list(range(100))
        self.sensor13 = np.random.normal(size=100)  # list(range(100))
        self.sensor14 = np.random.normal(size=100)  # list(range(100))
        self.sensor15 = np.random.normal(size=100)  # list(range(100))
        self.sensor16 = np.random.normal(size=100)  # list(range(100))

        self.data_sensor1 = self.ui.graphComponent.plot(pen='w')
        self.data_sensor2 = self.ui.graphComponent.plot(pen='r')
        self.data_sensor3 = self.ui.graphComponent.plot(pen='g')
        self.data_sensor4 = self.ui.graphComponent.plot(pen='w')
        self.data_sensor5 = self.ui.graphComponent.plot(pen='r')
        self.data_sensor6 = self.ui.graphComponent.plot(pen='g')
        self.data_sensor7 = self.ui.graphComponent.plot(pen='w')
        self.data_sensor8 = self.ui.graphComponent.plot(pen='r')
        self.data_sensor9 = self.ui.graphComponent.plot(pen='g')
        self.data_sensor10 = self.ui.graphComponent.plot(pen='w')
        self.data_sensor11 = self.ui.graphComponent.plot(pen='r')
        self.data_sensor12 = self.ui.graphComponent.plot(pen='g')
        self.data_sensor13 = self.ui.graphComponent.plot(pen='w')
        self.data_sensor14 = self.ui.graphComponent.plot(pen='r')
        self.data_sensor15 = self.ui.graphComponent.plot(pen='w')
        self.data_sensor16 = self.ui.graphComponent.plot(pen='r')

    # if __name__ == "__main__":
    #     import sys
    #     app = QtWidgets.QApplication(sys.argv)
    #     plot_view = QtWidgets.QWidget()
    #     ui = Ui_plot_view()
    #     ui.setupUi(plot_view)
    #     plot_view.show()
    #     sys.exit(app.exec_())

    def _configure_plot(self):
        """
        - setup specific elements of the PyQtGraph plot
        - no return
        """
        # self.ui.plt.setBackground(background=None)
        # self.ui.plt.setAntialiasing(True)
        # self._plt = self.ui.plt.addPlot(row=1, col=1)
        # self._plt.setLabel('bottom', Constants.plot_xlabel_title, Constants.plot_xlabel_unit)

        # title
        self.ui.graphComponent.setTitle(PlotConstants.app_title, size='16pt', color='#FFFFFF', bold=True)

        # -- axi labels
        # X Label
        self.ui.graphComponent.setLabel('left', PlotConstants.plot_x_label, PlotConstants.plot_x_label_unit,
                                        color='white', size=40)
        # Y label
        self.ui.graphComponent.setLabel('bottom', PlotConstants.plot_y_label, PlotConstants.plot_y_label_unit,
                                        color='white', size=40)

    def _enable_ui(self, enabled):
        """
        - enables/ disables the UI elements of the window.
        - param enabled: The value to be set at the enabled characteristic of the UI elements.
        - type enabled: bool
        - no return
        """
        self.ui.pButton_Stop.setEnabled(enabled)
        self.ui.pButton_Start.setEnabled(enabled)

        self.ui.chBox_1.setEnabled(enabled)   # not enabled
        self.ui.chBox_2.setEnabled(enabled)  # not enabled
        self.ui.chBox_3.setEnabled(enabled)  # not enabled
        self.ui.chBox_4.setEnabled(enabled)  # not enabled
        self.ui.chBox_5.setEnabled(enabled)  # not enabled
        self.ui.chBox_6.setEnabled(enabled)  # not enabled
        self.ui.chBox_7.setEnabled(enabled)  # not enabled
        self.ui.chBox_8.setEnabled(enabled)  # not enabled
        self.ui.chBox_9.setEnabled(enabled)  # not enabled
        self.ui.chBox_10.setEnabled(enabled)  # not enabled
        self.ui.chBox_12.setEnabled(enabled)  # not enabled
        self.ui.chBox_13.setEnabled(enabled)  # not enabled
        self.ui.chBox_14.setEnabled(enabled)  # not enabled
        self.ui.chBox_15.setEnabled(enabled)  # not enabled
        self.ui.chBox_16.setEnabled(enabled)  # not enabled

    def _connect_signals_to_methods(self):
        """
        - make up the connections between signals and UI elements
        - no return
        """
        self.ui.pButton_Start.clicked.connect(self.start_acq)
        self.ui.pButton_Stop.clicked.connect(self.stop_acq)
        self.ui.sendButton.clicked.connect(self.wr2led_button_clicked)

        # self.ui.sBox_Samples.valueChanged.connect(self._update_sample_size)
        # self.ui.cBox_Source.currentIndexChanged.connect(self._source_changed)

    def _configure_timers(self):
        """
        Configures specific elements of the QTimers.
        :return:
        """
        self._timer_plot = QtCore.QTimer(self)
        self._timer_plot.timeout.connect(self._update_plot)

    def wr2led_button_clicked(self):
        """
        send 8-bits to LEDs on ZedBoard
        """
        Log.i(TAG, "Send 8-Bits to LEDs on ZedBoard")
        self.zedcontroller.led_button_clicked()

    def start_acq(self):
        """
        - start the acquisition of data
        - associated to the 'Start' button.
        - no return
        """

        Log.i(TAG, "Clicked start button...")
        # self.worker = Worker(port=self.ui.cBox_Port.currentText(),
        #                      speed=float(self.ui.cBox_Speed.currentText()),
        #                      samples=self.ui.sBox_Samples.value(),
        #                      source=self._get_source(),
        #                      export_enabled=self.ui.chBox_export.isChecked())
        # if self.worker.start():
        # self._timer_plot.start(plot_constants.plot_update_ms)
        #     self._enable_ui(False)
        # else:
        #     Log.i(TAG, "Port is not available")
        #     PopUp.warning(self, Constants.app_title, "Selected port \"{}\" is not available"

        # self.ui.graphComponent.clear()
        # # first signal values generation
        # self.x1 = list(range(100))  # 100 time points
        # self.sensor1 = [randint(0, 100) for _ in range(100)]  # 100 data points
        # # self.sensor1 = np.sin(np.linespace(0, 4 * np.pi, 100))
        #
        # # second signal values generation
        # # self.x2 = list(range(100))  # 100 time points
        # self.sensor2 = [randint(0, 100) for _ in range(100)]  # 100 data points
        #
        # #
        # self.sensor3 = np.random.normal(size=100)
        #
        # #
        # # self.data4 = np.sin(np.linspace(0, 4 * np.pi, 100))
        #
        # self.pen1 = pg.mkPen(color=(255, 255, 255))
        # self.pen2 = pg.mkPen(color=(23, 255, 0))
        # # self.data_sensor1 = self.ui.graphComponent.plot(self.x1, self.sensor1, pen=self.pen1)
        # # self.data_sensor2 = self.ui.graphComponent.plot(self.x1, self.sensor2, pen=self.pen2)
        # self.data_sensor1 = self.ui.graphComponent.plot(self.sensor1, pen=self.pen1)
        # self.data_sensor2 = self.ui.graphComponent.plot(self.sensor2, pen=self.pen2)
        #
        # self.data_sensor3 = self.ui.graphComponent.plot(self.sensor3, pen=self.pen2)
        # # self.data_line4 = self.ui.graphComponent.plot(self.data4, pen=self.pen1)
        print("starting...")
        self.ui.pButton_Status.setStyleSheet("background-color: green")
        self.ptr = 0
        self._timer_plot.start(PlotConstants.plot_update_us)

    def stop_acq(self):
        """
        Stops the acquisition of the selected serial port.
        This function is connected to the clicked signal of the Stop button.
        :return:
        """
        Log.i(TAG, "Clicked stop button...")
        print("stopping...")
        # self.graphicsView.stop()

        self.ui.pButton_Status.setStyleSheet("background-color: red")
        self._timer_plot.stop()
        self._enable_ui(True)
        # self.Worker.stop()

    def _update_plot(self):
        """
        - plots the input signals, and update them with a new value every s and redraws the graphics in the plot.
        - self._timer_plot.timeout.connect(self._update_plot) time
        - no return
        """
        # self.worker.consume_queue()
        #
        # # plot data
        # self._plt.clear()
        # for idx in range(self.worker.get_lines()):
        #     self._plt.plot(x=self.worker.get_time_buffer(),
        #                    y=self.worker.get_values_buffer(idx),
        #                    pen=Constants.plot_colors[idx])
        # signal 1
        # self.x1 = self.x1[1:]  # Remove the first y element.
        # self.x1.append(self.x1[-1] + 1)  # Add a new value 1 higher than the last.

        # self.sensor1 = self.sensor1[1:]  # Remove the first
        # self.sensor1.append(randint(0, 100))  # Add a new random value.
        # # self.sensor1[-1]=(np.sin(np.linspace(0, 4 * np.pi, 1)))
        #
        # # self.data_sensor1.setData(self.x1, self.sensor1)  # Update the data.
        # self.data_sensor1.setData(self.sensor1)  # Update the data.
        #
        # signal 1

        #    self.data_sensor1 = self.ui.graphComponent.plot(pen='w')
        #else:
        #    self.data_sensor1 = self.ui.graphComponent.plot(pen='b')

        # signal 1
        self.sensor1[:-1] = self.sensor1[1:]
        self.sensor1[-1] = np.random.normal()
        if self.ui.chBox_1.isChecked():
            self.data_sensor1.setData(self.sensor1, pen=PlotConstants.plot_colors['s1'])
            self.data_sensor1.setPos(self.ptr, 0)
        else:
            self.data_sensor1.setData(self.sensor1, pen=None)
            self.data_sensor1.setPos(self.ptr, 0)
        # signal 2
        self.sensor2[:-1] = self.sensor2[1:]
        self.sensor2[-1] = np.random.normal()
        if self.ui.chBox_2.isChecked():
            self.data_sensor2.setData(self.sensor2, pen=PlotConstants.plot_colors['s2'])
            self.data_sensor2.setPos(self.ptr, 0)
        else:
            self.data_sensor2.setData(self.sensor2, pen=None)
            self.data_sensor2.setPos(self.ptr, 0)
        #    self.sensor1.clear()
        #    self.data_sensor1.setPos(self.ptr, 0)
            #self.sensor1[:-1] = self.sensor1[1:]
            #self.sensor1[-1] = np.random.normal()
            #self.data_sensor1.setData(self.sensor1)
        # signal 3
        self.sensor3[:-1] = self.sensor3[1:]
        self.sensor3[-1] = np.random.normal()
        if self.ui.chBox_3.isChecked():
            self.data_sensor3.setData(self.sensor3, pen=PlotConstants.plot_colors['s3'])
            self.data_sensor3.setPos(self.ptr, 0)
        else:
            self.data_sensor3.setData(self.sensor4, pen=None)
            self.data_sensor3.setPos(self.ptr, 0)
        # signal 4
        self.sensor4[:-1] = self.sensor4[1:]
        self.sensor4[-1] = np.random.normal()
        if self.ui.chBox_4.isChecked():
            self.data_sensor4.setData(self.sensor4, pen=PlotConstants.plot_colors['s4'])
            self.data_sensor4.setPos(self.ptr, 0)
        else:
            self.data_sensor4.setData(self.sensor4, pen=None)
            self.data_sensor4.setPos(self.ptr, 0)
        # signal 5
        self.sensor5[:-1] = self.sensor5[1:]
        self.sensor5[-1] = np.random.normal()
        if self.ui.chBox_5.isChecked():
            self.data_sensor5.setData(self.sensor5, pen=PlotConstants.plot_colors['s5'])
            self.data_sensor5.setPos(self.ptr, 0)
        else:
            self.data_sensor5.setData(self.sensor5, pen=None)
            self.data_sensor5.setPos(self.ptr, 0)
        # signal 6
        self.sensor6[:-1] = self.sensor6[1:]
        self.sensor6[-1] = np.random.normal()
        if self.ui.chBox_6.isChecked():
            self.data_sensor6.setData(self.sensor6, pen=PlotConstants.plot_colors['s6'])
            self.data_sensor6.setPos(self.ptr, 0)
        else:
            self.data_sensor6.setData(self.sensor6, pen=None)
            self.data_sensor6.setPos(self.ptr, 0)
        # signal 7
        self.sensor7[:-1] = self.sensor7[1:]
        self.sensor7[-1] = np.random.normal()
        if self.ui.chBox_7.isChecked():
            self.data_sensor7.setData(self.sensor7, pen=PlotConstants.plot_colors['s7'])
            self.data_sensor7.setPos(self.ptr, 0)
        else:
            self.data_sensor7.setData(self.sensor2, pen=None)
            self.data_sensor7.setPos(self.ptr, 0)
        # signal 8
        self.sensor8[:-1] = self.sensor8[1:]
        self.sensor8[-1] = np.random.normal()
        if self.ui.chBox_8.isChecked():
            self.data_sensor8.setData(self.sensor8, pen=PlotConstants.plot_colors['s8'])
            self.data_sensor8.setPos(self.ptr, 0)
        else:
            self.data_sensor8.setData(self.sensor8, pen=None)
            self.data_sensor8.setPos(self.ptr, 0)
        # signal 9
        self.sensor9[:-1] = self.sensor9[1:]
        self.sensor9[-1] = np.random.normal()
        if self.ui.chBox_9.isChecked():
            self.data_sensor9.setData(self.sensor9, pen=PlotConstants.plot_colors['s9'])
            self.data_sensor9.setPos(self.ptr, 0)
        else:
            self.data_sensor9.setData(self.sensor9, pen=None)
            self.data_sensor9.setPos(self.ptr, 0)
        # signal 10# signal 10
        self.sensor10[:-1] = self.sensor10[1:]
        self.sensor10[-1] = np.random.normal()
        if self.ui.chBox_10.isChecked():
            self.data_sensor10.setData(self.sensor10, pen=PlotConstants.plot_colors['s10'])
            self.data_sensor10.setPos(self.ptr, 0)
        else:
            self.data_sensor10.setData(self.sensor10, pen=None)
            self.data_sensor10.setPos(self.ptr, 0)
        # signal 10# signal 11
        self.sensor11[:-1] = self.sensor11[1:]
        self.sensor11[-1] = np.random.normal()
        if self.ui.chBox_11.isChecked():
            self.data_sensor11.setData(self.sensor11, pen=PlotConstants.plot_colors['s11'])
            self.data_sensor11.setPos(self.ptr, 0)
        else:
            self.data_sensor11.setData(self.sensor11, pen=None)
            self.data_sensor11.setPos(self.ptr, 0)
        # signal 10# signal 12
        self.sensor12[:-1] = self.sensor12[1:]
        self.sensor12[-1] = np.random.normal()
        if self.ui.chBox_12.isChecked():
            self.data_sensor12.setData(self.sensor12, pen=PlotConstants.plot_colors['s12'])
            self.data_sensor12.setPos(self.ptr, 0)
        else:
            self.data_sensor12.setData(self.sensor12, pen=None)
            self.data_sensor12.setPos(self.ptr, 0)
        # signal 10# signal 13
        self.sensor13[:-1] = self.sensor13[1:]
        self.sensor13[-1] = np.random.normal()
        if self.ui.chBox_13.isChecked():
            self.data_sensor13.setData(self.sensor13, pen=PlotConstants.plot_colors['s13'])
            self.data_sensor13.setPos(self.ptr, 0)
        else:
            self.data_sensor13.setData(self.sensor13, pen=None)
            self.data_sensor13.setPos(self.ptr, 0)
        # signal 10# signal 14
        self.sensor14[:-1] = self.sensor14[1:]
        self.sensor14[-1] = np.random.normal()
        if self.ui.chBox_14.isChecked():
            self.data_sensor14.setData(self.sensor14, pen=PlotConstants.plot_colors['s14'])
            self.data_sensor14.setPos(self.ptr, 0)
        else:
            self.data_sensor14.setData(self.sensor14, pen=None)
            self.data_sensor14.setPos(self.ptr, 0)
        # signal 10# signal 15
        self.sensor15[:-1] = self.sensor15[1:]
        self.sensor15[-1] = np.random.normal()
        if self.ui.chBox_15.isChecked():
            self.data_sensor15.setData(self.sensor15, pen=PlotConstants.plot_colors['s15'])
            self.data_sensor15.setPos(self.ptr, 0)
        else:
            self.data_sensor15.setData(self.sensor15, pen=None)
            self.data_sensor15.setPos(self.ptr, 0)
        # signal 10# signal 16
        self.sensor16[:-1] = self.sensor16[1:]
        self.sensor16[-1] = np.random.normal()
        if self.ui.chBox_16.isChecked():
            self.data_sensor16.setData(self.sensor16, pen=PlotConstants.plot_colors['s16'])
            self.data_sensor16.setPos(self.ptr, 0)
        else:
            self.data_sensor16.setData(self.sensor16, pen=None)
            self.data_sensor16.setPos(self.ptr, 0)


        self.ptr += 1
