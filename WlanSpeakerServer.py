import pygame
import sys
import socket

HOST = ''
PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print 'Socket created'

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'

#s.listen(10)
print 'Socket now listening'

pygame.mixer.init()
#pygame.mixer.music.load("/home/pi/Music/Tetris.mp3")


while 1:
	data, addr = s.recvfrom(1024)
	print 'Connection address:', addr
	
	print 'received data:', data
	
	strData = data.strip()
	try:
		if data.strip() == 'play':
			print 'Play'
			pygame.mixer.music.play()
		if data.strip() == 'pause':
			print 'Pause'
			pygame.mixer.music.pause()
		if data.strip() == 'unpause':
			print 'Replay'
			pygame.mixer.music.unpause()
		if data.strip() ==  'stop':
			print 'Stop'
			pygame.mixer.music.stop()
		if data.strip() == 'exit':
			print 'Beende Server'
			break
		if strData[0:4] == 'load':
			print 'load new File'
			pygame.mixer.music.load("/home/pi/Music/"+strData[5:])
			print 'succsessfull load'
	except RuntimeError:
			print 'error catchted'

s.close()
