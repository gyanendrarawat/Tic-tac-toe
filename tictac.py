curr_game=[['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]

turn=0 
status=False
win=""


# Print tictactoe
def showGame():

	for i in range(0,3):

		print(end=" ")
	
		for j in range(0,3):
			if j<2:
				print(curr_game[i][j], end="|")
			
			else:
				print(curr_game[i][j], end=" ")
		print()
	
		print(end=" ")
		if i<2:
			for j in range(0,3):
				if j<2:
					print("___",end="|")	
			
				else:
					print("___",end=" ")
			
			print()
	
		else:
			for j in range(0,3):
				if j<2:
					print("   ",end="|")
			
				else:
					print("   ",end=" ")
			
			print()
		
	print()
	
	
# Game Start
	
print()
showGame()

while True:
	
	turn=turn+1
	
	if(turn==10):
		filedata=open("record.txt",'a')
		filedata.write("Draw"+'\n')
		print("Game-Over: DRAW")
		break
		
			
		
	elif turn&1 == 1:
		win="Player-1"
		sign=' X '
		
	else :
		win="Player-2"
		sign=' O '	
	
	x,y=input(win+" to choose ").split()
	print()
	
	
	
	if int(x) > 3 or int(y) >3:
		print("Error: Choose a Valid and an unoccupied cell ")
		print()
		turn=turn-1
		continue
		
	elif curr_game[int(x)-1][int(y)-1]!='   ':
		print("Error: Choose a Valid and an unoccupied cell ")
		print()
		turn=turn-1
		continue
		
	
	curr_game[int(x)-1][int(y)-1]= sign	
		
	showGame()
		
	print()
		
		
	#rows checking
	for i in range(0,3):
		if curr_game[i][0]!='   ' and curr_game[i][0]==curr_game[i][1] and curr_game[i][0]==curr_game[i][2]:
			status = True
			print("Game-Over: "+ "Congrats " + win +" won the game")
			break
				
	if status==True:
		filedata=open("record.txt","a")
		filedata.write(win+"\n")
		break
			
	#column checking
	for j in range(0,3):
		if curr_game[0][j]!='   ' and curr_game[0][j]==curr_game[1][j] and curr_game[0][j]==curr_game[2][j]:
			status = True
			print("Game-Over: "+"Congrats " + win +" won the game")
			break
				
	if status==True:
		filedata = open("record.txt","a")
		filedata.write(win+"\n")
		break
			
	#diagnol checks
	if curr_game!='   ' and curr_game[0][0]==curr_game[1][1] and curr_game[1][1]==curr_game[2][2]:
		filedata=open("record.txt","a")
		filedata.write(win+"\n")
		print("Game-Over: "+"Congrats " + win +" won the game")
		break
			
			
	elif curr_game[0][2]!='   ' and curr_game[0][2]==curr_game[1][1] and curr_game[2][0]==curr_game[1][1]:
		filedata=open("record.txt","a")
		filedata.write(win+"\n")
		print("Game-Over: "+"Congrats " + win +" won the game")
		break	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
						
				
