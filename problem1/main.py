import sys, time, subprocess
from Daemon import Daemon
 
class SystemMonitorDaemon(Daemon):
	def run(self):
		while True:
			time.sleep(1)
			logState()

	"""log current state of system"""
	def logState(self):
		logFile = super().logFile
		logFile.write('logging')
		
	"""set mode for system monitor c=CPU,n=NETWORK,m=MEMORY"""	
	def setMode(self,mode):
		self._cpu = True if 'c' in mode else False
		self._netowrk = True if 'n' in mode else False
		self._memory = True if 'm' in mode else False
  

def badUsageHandler():
	print('usage: %s start|stop|restart [OPTIONS]' % sys.argv[0])
	print('Options description:')
	print('c  ,CPU')
	print('n  ,NETWORK')
	print('m  ,memory')
	print('Example:')
	print('main.py start cn')
	sys.exit(2)


if __name__ == "__main__":
	daemon = SystemMonitorDaemon('/tmp/systemMonitorDaemon.pid')
	argLen = len(sys.argv)
	if argLen == 2:
		if 'start' == sys.argv[1]:
			print('Starting daemon in default mode (Network+Memory+Cpu)')
			daemon.setMode('cnm')
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
	elif argLen == 3:
		if 'start' == sys.argv[1]:
			daemon.setMode(sys.argv[2])
			print('Starting daemon in mode:%s' % sys.argv[2])
			daemon.start()
		else:
			badUsageHandler()
	else:
		badUsageHandler()
