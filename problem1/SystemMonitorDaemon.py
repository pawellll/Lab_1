#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""

import time
import logging
import os
import subprocess
from Daemon import Daemon
from Configuration import Configuration as Conf


class SystemMonitorDaemon(Daemon):
    """Daemon class providing system monitoring for cpu, memory and network"""
    def __init__(self, pidfile):
        Daemon.__init__(self, pidfile)
        self._cpu = False
        self._network = False
        self._memory = False

    def run(self):
        while True:
            if self._cpu:
                self._log_state(Conf.CPU_COMMAND)

            if self._memory:
                self._log_state(Conf.MEM_COMMAND)

            if self._network:
                self._log_state(Conf.NET_COMMAND)

            time.sleep(1)

    def _log_state(self,command):
        logging.info(self._run_bash(command))

    """set mode for system monitor c=CPU,n=NETWORK,m=MEMORY"""
    def set_mode(self, mode):
        self._setup_logging(Conf.LOGGING_PATH, Conf.LOGGING_LEVEL, Conf.LOGGING_FORMAT)
        self._cpu = True if 'c' in mode else False
        self._network = True if 'n' in mode else False
        self._memory = True if 'm' in mode else False

    """Run bash command"""
    @staticmethod
    def _run_bash(command):
        call_bash = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
        return call_bash.communicate()[0]

    """Setup logging for class"""
    @staticmethod
    def _setup_logging(log_path, logging_level, logging_format):
        # remove log file if exists
        try:
            os.remove(log_path)
        except OSError:
            pass

        logging.basicConfig(filename=log_path, level=logging_level, format=logging_format)
        logging.info("Logging has been initialised")