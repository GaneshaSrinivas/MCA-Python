try:
	f=open('D:/File/voice.mp3','rb')
	f1=open('D:/Dest/audiocopy.mp3','wb')
	bytes=f.read()
	print('File copied into D/Dest:')
	f1.write(bytes)
	f.close()
	f1.close()


except FileNotFoundError:
	print('Specified input file not found!')
