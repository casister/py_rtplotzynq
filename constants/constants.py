from enum import Enum
from PyQt5 import QtWidgets, QtGui


class PlotConstants:
    """
    ----    Common constants used in the different Py modules   ---- 
    ---- That are part of the Real Time Plot Interface for Zynq ----
    ----          Based Data Acquisition Systems                ----
    """
    app_title = "RT Plot for Zynq SoPC"
    app_version = '0.1'
    app_export_path = "log"  # data"
    app_sources = ["Serial", "UDP", "Simulator"]
    app_encoding = "utf-8"

    plot_update_us = 200

    plot_x_label = "Voltage"
    plot_x_label_unit = "V"
    plot_y_label = "Time"
    plot_y_label_unit = "us"

    plot_signal_colors = ['#0072bd', '#d95319', '#edb120', '#7e2f8e', '#77ac30', '#4dbeee', '#a2142f']
    plot_max_num_signals = len(plot_signal_colors)

    # process_join_timeout_ms = 1000

    argument_default_samples = 500

    serial_default_speed = 115200
    serial_timeout_ms = 0.5
    # time in miliseconds between reads used to set the timer timeout
    t_bt_samples: int = 40\

    max_num_channels = 32
    # -------- dictionary to define plot color per each channel ------ #
    # https://www.rapidtables.com/web/color/RGB_Color.html
    plot_colors = {
        's1': QtGui.QColor(255, 255, 255),      # white     #FFFFFF
        's2': QtGui.QColor(255, 0, 0),          # red       #FF0000
        's3': QtGui.QColor(0, 255, 0),          # lime      #00FF00
        's4': QtGui.QColor(0, 0, 255),          # blue      #0000FF
        's5': QtGui.QColor(255, 255, 0),        # yellow    #FFFF00
        's6': QtGui.QColor(0, 255, 255),        # cyan      #00FFFF
        's7': QtGui.QColor(255, 0, 255),        # magenta   #FF00FF
        's8': QtGui.QColor(210, 105, 30),       # chocolate #D2691E
        's9': QtGui.QColor(188, 143, 143),      # rosy brown#BC8F8F
        's10': QtGui.QColor(128, 128, 0),       # olive     #808000
        's11': QtGui.QColor(0, 128, 0),         # green     #008000
        's12': QtGui.QColor(128, 0, 128),       # purple    #800080
        's13': QtGui.QColor(0, 128, 128),       # teal      #008080
        's14': QtGui.QColor(47, 79, 79),        # dark slate gray #2F4F4F
        's15': QtGui.QColor(255, 165, 0),       # orange    #FFA500
        's16': QtGui.QColor(210,180,140),       # tan       #D2B48C
    }
    class SocketClient:
        timeout = 0.01
        host_default = "localhost"
        port_default = [5555, 8080, 9090]
        buffer_recv_size = 1024

    simulator_default_sample_period = 0.002

    csv_default_filename = "%Y-%m-%d_%H-%M-%S"
    csv_delimiter = ","
    csv_file_extension = "csv"

    parser_timeout_ms = 0.005
    process_join_timeout_ms = 1000

    # log file constants
    log_filename = "{}.log".format(app_title)
    log_max_bytes = 5120
    log_default_level = 1
    log_default_console_log = False


class SourceType(Enum):
    """
    Enum for the types of sources. Indices MUST match app_sources constant.
    """
    simulator = 1
    serial = 0
    SocketClient = 2


"""
class Constants:
   # 
   # Common constants for the application.
   # 
    app_title = "Zynq_RT_Plot"
    app_version = '0.3.1'
    app_export_path = "log"
    app_sources = ["Serial", "Simulator", "Socket Client"]
    app_encoding = "utf-8"

    plot_update_ms = 16
    plot_xlabel_title = "Time"
    plot_xlabel_unit = "s"
    plot_colors = ['#0072bd', '#d95319', '#edb120', '#7e2f8e', '#77ac30', '#4dbeee', '#a2142f']
    plot_max_lines = len(plot_colors)

    process_join_timeout_ms = 1000

    argument_default_samples = 500

    serial_default_speed = 115200
    serial_timeout_ms = 0.5

    class SocketClient:
        timeout = 0.01
        host_default = "localhost"
        port_default = [5555, 8080, 9090]
        buffer_recv_size = 1024

    simulator_default_speed = 0.002

    csv_default_filename = "%Y-%m-%d_%H-%M-%S"
    csv_delimiter = ","
    csv_extension = "csv"

    parser_timeout_ms = 0.005

    log_filename = "{}.log".format(app_title)
    log_max_bytes = 5120
    log_default_level = 1
    log_default_console_log = False
"""


class MinimalPython:
    """
    Specifies the minimal Python version required.
    """
    major = 3
    minor = 2
    release = 0

# ---------------------------------- EoF ---------------------------------- #
