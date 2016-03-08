import random
import math


def iround(x):
    """iround(number) -> integer
    Round a number to the nearest integer."""
    return int(round(x) - .5) + (x > 0)

def Kinhsh():
	f=0
	while f==0:
		move=raw_input("IN WHICH DIRECTION WILL YOU MOVE?")
		if move == "w":
			f=1
		elif move == "a":
			f=1
		elif move == "s":
			f=1
		elif move == "d":
			f=1
		elif move == "show me":
			Show_Stage(stage)
		else:
			print "!!!WRONG MOVE!!!"
	return move 


def Show_Stage(stage):
	print keno
	print keno

	print stage[0],stage[1],stage[2],stage[3],stage[4],stage[5],stage[6],stage[7],stage[8],stage[9]
	print stage[10],stage[11],stage[12],stage[13],stage[14],stage[15],stage[16],stage[17],stage[18],stage[19]
	print stage[20],stage[21],stage[22],stage[23],stage[24],stage[25],stage[26],stage[27],stage[28],stage[29]
	print stage[30],stage[31],stage[32],stage[33],stage[34],stage[35],stage[36],stage[37],stage[38],stage[39]
	print stage[40],stage[41],stage[42],stage[43],stage[44],stage[45],stage[46],stage[47],stage[48],stage[49]
	print stage[50],stage[51],stage[52],stage[53],stage[54],stage[55],stage[56],stage[57],stage[58],stage[59]
	print stage[60],stage[61],stage[62],stage[63],stage[64],stage[65],stage[66],stage[67],stage[68],stage[69]
	print stage[70],stage[71],stage[72],stage[73],stage[74],stage[75],stage[76],stage[77],stage[78],stage[79]
	print stage[80],stage[81],stage[82],stage[83],stage[84],stage[85],stage[86],stage[87],stage[88],stage[89]
	print stage[90],stage[91],stage[92],stage[93],stage[94],stage[95],stage[96],stage[97],stage[98],stage[99]

	print keno
	print keno

def Count_The_Distance(stage):

	player=stage.index(1)
	treasure=stage.index(2)
	
	
	
	player=player*1.0
	player=player/10
	playerx, playery = divmod(player, 1)
	
	playery = playery*10.0
	
	
	playerx=iround(playerx)
	playery=iround(playery)
	
	
	
	
	treasure=treasure*1.0
	treasure=treasure/10
	treasurex, treasurey = divmod(treasure,1)
	
	treasurey = treasurey*10.0
	
	
	treasurex=iround(treasurex)
	treasurey=iround(treasurey)
	
	D = ( treasurex - playerx )**2 + ( treasurey - playery )**2 
	distance=math.sqrt(D)
	print "The distance is:", distance
	


	







def Move_Around_The_Board(stage,move,spot):
	keno=" "
	if move == "w":
		if spot-10 < 0:
			print keno
			print "YOU HAVE REACHED THE NORTH SIDE OF THE BOARD"
			print keno
		else:
			stage[spot]=0
			stage[spot-10]=1
	elif move == "s":
		if spot+10 >= 100:
			print keno
			print "YOU HAVE REACHED THE SOUTH SIDE OF THE BOARD"
			print keno
		else:
			stage[spot]=0
			stage[spot+10]=1
	elif move == "a":
		oldspot=(spot/10.0)//1
		newspot=((spot-1)/10.0)//1
		if oldspot > newspot:
			print keno
			print "YOU HAVE REACHED THE WEST SIDE OF THE BOARD"
			print keno
		else:
			stage[spot]=0
			stage[spot-1]=1
	elif move == "d":
		oldspot=(spot/10.0)//1
		newspot=((spot+1)/10.0)//1
		if oldspot < newspot:
			print keno
			print "YOU HAVE REACHED THE EAST SIDE OF THE BOARD"
			print keno
		else:
			stage[spot]=0
			stage[spot+1]=1	
	return stage


#Synarthseis teleiwnoun edw ^



keno = " "

stage=[]
for i in range(98):
	stage.append(0)
stage.append(1)
stage.append(2)





random.shuffle(stage)



print "Instructions:"
print keno
print "In this maze like game the only hint you get, about where"
print "you are, will be the distance between you and the treasure"
print "you seek!"
print "Move your player around by using the WASD keys."

print "         W   " 
print "        A D  "
print "         S   "

print "Type 'show me' if you want to see the stage." 
print "Make sure you have Caps Lock OFF!"


print "================================================================"


firsttime=0
GAME="ON"
while GAME=="ON":
	if firsttime==0:
		Count_The_Distance(stage)
		firsttime=1
	
	

	#Show_Stage(stage)


	spot=stage.index(1)
	
	
	


	move=Kinhsh()


	stage=Move_Around_The_Board(stage,move,spot)
	
	if stage.count(2)==0:
		GAME="OVER"
	else:
		Count_The_Distance(stage)
print keno
print "!!!!!THE GAME IS OVER!!!!!"	
	
	
	
	
	
	








