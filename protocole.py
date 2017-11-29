class Protocole(object):

	RUN="Run"
	INIT="Init"

	def sendMove(numPlayer, x, y):
		if(numPlayer < 0 or x < 0 or y < 0):
			raise

		return str(numPlayer)+' '+str(x)+' 'str(y)

	def sendAddPlayer(num):
		return "Add " + str(num)

	def sendEndInit():
		return INIT

	def sendRun():
		return RUN

	def receiveEndInit(message):
		if(message == INIT):
			return True
		else:
			return False

	def receiveRun(message):
		if(message == RUN):
			return True
		else:
			return False

	def receiveAddPlayer(message):
		rec = message.split(' ')
		if(len(rec) != 2):
			raise
		if(rec[0] != "Add"):
			raise

		if(!rec[1].isDigit()):
			raise

		return int(rec[1])

	def receiveMove(message)
		rec = message.split(' ')
		if(len(receive) != 3):
			raise

		receive = [int(x) for x in rec]

		for info in receive:
			if info < 0:
				raise

		return message.split(' ')

	