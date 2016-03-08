keno=" "
#^mia metablhth gia na ksexwrizoun ta sxhmata metaksy tous


file_in=open("CustomTetrisPiece.txt","r")
x=[]
for line in file_in:
	for i in line:
		x.append(i)

file_in.close()




for i in range(7):
	x.remove("\n")
#^edw afairw apo th lista ta dedomena "\n" pou dhlwnan alagh grammhs



def show_shape(x):
	print x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]
	print x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15]
	print x[16],x[17],x[18],x[19],x[20],x[21],x[22],x[23]
	print x[24],x[25],x[26],x[27],x[28],x[29],x[30],x[31]
	print x[32],x[33],x[34],x[35],x[36],x[37],x[38],x[39]
	print x[40],x[41],x[42],x[43],x[44],x[45],x[46],x[47]
	print x[48],x[49],x[50],x[51],x[52],x[53],x[54],x[55]
	print x[56],x[57],x[58],x[59],x[60],x[61],x[62],x[63]


#H lista x einai to aplo sxhma pou dothike sto arxeio txt
show_shape(x)

print keno
print keno


y=[]
for i in range(64):
	y.append(x[63-i])
#h Lista y einai to sxhma gyrismeno 180 moires

show_shape(y)

print keno
print keno

z=[]
for i in range(56,64):
	for j in range(8):
		z.append(x[i-8*j])
#h lista z einai h x gyrismenh 90 moires

show_shape(z)


print keno
print keno

w=[]
for i in range(56,64):
	for j in range(8):
		w.append(y[i-8*j])
#h lista w einai h y gyrismenh 90 moires

show_shape(w)







