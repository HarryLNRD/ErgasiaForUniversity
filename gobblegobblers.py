mikra=[1,1]
mesaia=[2,2]
megala=[3,3]

megethi=mikra+mesaia+megala

omades=["red","blue"]


paikths1=[]
for j in megethi:
	paikths1.append([omades[0],j])
print paikths1

		
paikths2=[]
for j in megethi:
	paikths2.append([omades[1],j])
print paikths2

pista=[]
for i in range(9):
	pista.append(["keno"]) 

print pista[0],pista[1],pista[2]
print pista[3],pista[4],pista[5]
print pista[6],pista[7],pista[8]


pista[0].insert(0,"PA")
pista[1].insert(0,"PM")
pista[2].insert(0,"PD")
pista[3].insert(0,"MA")
pista[4].insert(0,"MM")
pista[5].insert(0,"MD")
pista[6].insert(0,"KA")






pista[7].insert(0,"KM")
pista[8].insert(0,"KD")

print pista[0],pista[1],pista[2]
print pista[3],pista[4],pista[5]
print pista[6],pista[7],pista[8]



move=raw_input("pou tha baleis pioni")
epilogh=raw_input("ti megethos?(1,2,3?)")


if move == "PA" :
	kinplace=0
elif move == "PM":
	kinplace=1
elif move == "PD":
	kinplace=2
elif move == "MA":
	kinplace=3
elif move == "MM":
	kinplace=4
elif move == "MD":
	kinplace=5
elif move == "KA":
	kinplace=6
elif move == "KM":
	kinplace=7
elif move == "KD":
	kinplace=8
else:
	print "Lathos Kinhsh"

pista[kinplace].pop()

pista[kinplace].insert(1,epilogh)

if epilogh == 1:
	paikths1.pop(1)
elif epilogh == 2:
	paikths1.remove(2)
elif epilogh == 3:
	paikths1.remove(3)


print pista[0],pista[1],pista[2]
print pista[3],pista[4],pista[5]
print pista[6],pista[7],pista[8]


print paikths1

