# -*- coding: utf-8 -*-
"""
@author: Paweł Pęksa
"""
import logging
import sys
import ntpath

script_name = sys.argv[0]
(head, tail) = ntpath.split(script_name)
script_name = tail


class Configuration:
    """Class containing configuration constants"""
    def __init__(self):
        pass

    # launch options
    ARG_NET = "-n"
    ARG_NET_HELP = "Log netwrok information"

    ARG_CPU = "-c"
    ARG_CPU_HELP = "Log CPU information"

    ARG_MEM = "-m"
    ARG_MEM_HELP = "Log memory information"

    ARG_START = "start"
    ARG_STOP = "stop"
    ARG_RESTART = "restart"
    # bash commands

    TRIM_ENTER_COMMAND = "| tr \"\n\" \" \""
    CPU_COMMAND = "top -bn1 | grep \"Cpu(s)\"" + TRIM_ENTER_COMMAND
    MEM_COMMAND = "top -bn1 | grep \"Mem:\"" + TRIM_ENTER_COMMAND
    NET_COMMAND = "{ echo \"Recived data and send data\" ; dstat --net 1 1 | tail -n 1; }" + TRIM_ENTER_COMMAND

    # path to pid file
    PID_FILE_PATH = '/tmp/systemMonitorDaemon.pid'

    # logging configuration
    LOGGING_PATH = "systemMonitor.log"
    LOGGING_FORMAT = "%(asctime)s %(levelname)s %(message)s "
    LOGGING_LEVEL = logging.INFO

    # strings
    USAGE = "usage: {0} start|stop|restart [OPTIONS]".format(script_name)

    OPTIONS_DESC = "Options description:\n"
    OPTIONS_DESC += "c  ,CPU\n"
    OPTIONS_DESC += "n  ,NETWORK\n"
    OPTIONS_DESC += "m  ,memory\n"
    OPTIONS_DESC += "Example:\n"
    OPTIONS_DESC += "{0} start cn\n".format(script_name)
