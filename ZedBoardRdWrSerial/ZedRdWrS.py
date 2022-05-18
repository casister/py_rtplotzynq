import numpy as np
import serial
from PyQt5 import QtWidgets, QtCore
from py_ui.plot_cs import Ui_plot_view

TAG = "ZedBoard Serial Read/Write"


class ZedboardController:
    def __init__(self, transceiver):
        self.transceiver = transceiver

    def setGPIOS(self, value):
        str_value = format(value, '03d')
        self.transceiver.write('wr_leds{}\n'.format(str_value).encode())
        self.transceiver.flushOutput()

    def read_temperature_sensor(self, num_samples):
        to_return = []
        for i in range(num_samples):
            self.transceiver.write("rd_temp\n".encode())
            self.transceiver.flushOutput()
            data = self.transceiver.read(6) # 6=number of bytes/Related to: printf("%2.4f", temperature);
            to_return.append(float(data.decode()))

        return to_return


class Controller:
    def __init__(self, interface):
        self.interface = interface
        self.transceiver = serial.Serial('/dev/ttyACM0', baudrate=115200)
        self.zedboard = ZedboardController(self.transceiver)
        #self.connect_signals_to_methods()
        self.dataY = np.zeros(500)
        #self.line = self.interface.graphComponent.plot()

    def connect_signals_to_methods(self):
        self.interface.sendButton.clicked.connect(self.led_button_clicked)
        #self.interface.start.clicked.connect(self.start_button_clicked)
        #self.interface.stop.clicked.connect(self.stop_button_clicked)

    def led_button_clicked(self):
        leds = [self.interface.led8_2,
                self.interface.led7_2,
                self.interface.led6_2,
                self.interface.led5_2,
                self.interface.led4_2,
                self.interface.led3_2,
                self.interface.led2_2,
                self.interface.led1_2]
        position = 0
        result = 0
        for led in leds:
            if led.isChecked():
                result += 2 ** position

            position += 1

        self.interface.ledInformation.append('<h1>Leds changed: {}</h1>'.format(result))

        self.zedboard.setGPIOS(result)

    def start_button_clicked(self):
        self.interface.status.setStyleSheet("background-color: green")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.plot_timeout_reached)
        self.timer.start(33)

    def stop_button_clicked(self):
        if self.timer:
            self.interface.status.setStyleSheet("background-color: red")
            self.timer.stop()

    def plot_timeout_reached(self):
        received = self.zedboard.read_temperature_sensor(1)
        self.dataY[:-1] = self.dataY[1:]
        self.dataY[-1] = received[0]
        self.line.setData(self.dataY)
        self.interface.lcd.display(received[0])


def main():
    qt_app = QtWidgets.QApplication([])
    main_window = QtWidgets.QWidget()
    my_interface = Ui_plot_view()
    my_interface.setupUi(main_window)
    c = Controller(my_interface)
    main_window.show()
    qt_app.exec_()


if __name__ == '__main__':
    main()