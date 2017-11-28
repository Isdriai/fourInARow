class Protocole(object):

	RUN="run"

	def send(numPlayer, x, y):
		if numPlayer < 0 or x < 0 or y < 0:
			raise

		return str(numPlayer)+' '+str(x)+' 'str(y)

	def receive(message)
		rec = message.split(' ')
		if receive != 3:
			raise

		receive = [int(x) for x in rec]

		for info in receive:
			if info < 0:
				raise

		return message.split(' ')