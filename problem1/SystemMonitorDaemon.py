""" System monitor deamon """

from Daemon import Daemon

class SystemMonitorDaemon(Daemon):
    def run(self,mode,sleepTime):
	    with open('systemMonitor.log','r') as logFile:
		logFile.write('aaaa')
            	while True:
                	    time.sleep(sleepTime)


