import math

y = float(input("Enter a number : "))

def prove_round(y):

	y_image = str(y)
	pos = y_image.index('.')
	pos1 = str(pos)
	pos2 = list(y_image)
	pos3 = int(pos)
	pos4 = pos3 + 2
	pos5 = pos2[:pos4]
	pos6 = ''.join(pos5)
	pos7 = float(pos6)
	
	z1 = str(pos6)
	z2 = list(z1)
	z3 = len(z2) - 2
	z4 = z2[z3::]
	z5 = int(z4[1])

	if z5 >= 5 and z5 < 9:
		z6 = 1
	elif z5 == 9:
		z6 = 1
	else:
		z6 = 0

	if z6 == 1:
		pos7 += 1
	else:
		pos7 += 0

	z7 = ''.join(z2[0:z3])
	z8 = len(z7) - 1
	z9 = z7[z8]
	z10 = float(z7)

	if z6 == 1:
		z10 += 1
	else:
		z10 += 0

	print(z10)

prove_round(y)
