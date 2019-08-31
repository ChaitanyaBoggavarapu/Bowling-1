#This program calculates the bowling score when entered the number of pins hit on each turns
print('BOWLING SCORE CALCULATOR \n')

frames =[] #Variable to store the score
points = 0 #Variable to keep track of score

def strike(l):
	#Calculates the score for a STRIKE
	m = 0
	m = int(l[0]) + int(l[1])
	return m

def strike2(l1, l2):
	m = int(l1[0]) + int(l2[0])
	return m

def spare(l):
	#Calculates the score for a SPARE
	m = 0
	m = m + int(l[0])
	return m

#For loop for getting input from the user (Bowling score)
for i in range(10):

	turns = []
	te = 0
	for j in range(2):
		n = input ('Enter the score for the ' + str (i+1) + ' th frame and ' + str(j+1) +' th turn : ')
		turns.append(n)
		su = 0

		if i+1 == 10 and int(n) == 10:
			for k in range(2):
				n = input ('Enter the score for the ' + str (i+1) + ' th frame and ' + str(j+k+1) +' th turn (strike): ')
				turns.append(n)
			break
		
		elif i+1 == 10 and int(n) != 10:
			for x in turns:
				su = su + int(x)
			if su == 10:
				n = input ('Enter the score for the ' + str (i+1) + ' th frame and ' + str(j+2) +' th turn (spare): ')
				turns.append(n)

		if int(n) == 10: break
	print('\n')
	for x in turns:
		te = te + int(x)
		if te > 10 and i+1 != 10:
			print('PLEASE ENTER A VALID SCORE')

	frames.append(turns)

#Printing the input as list of lists
print('BOWLING SCORE INPUT:\n')
print(frames, '\n')

#For loop to calculate the score
c = 0
for turn in frames:
	#Iterates through each frame (ie: 10 in total)
	sum = 0
	for j in turn:
		#Iterates through each turn in a frame
		if c == 9:
			#Special case: last frame
			points = points + int(j)

		if int(j) == 10 and c!= 9:
			#Special case if there is a STRIKE in a non last frame
			if len(frames[c+1])>=2:
				fc = strike(frames[c+1])
			else:
				fc = strike2(frames[c+1], frames[c+2])

			points = points + 10 + fc	
			break

		elif c!=9 and int(j)!= 10:
			#Normal case: If there is no strike and it is not the last frame
			sum = sum + int(j)

	if sum == 10:
		#Checking sum of the particular frame for a SPARE
		fg = spare(frames[c+1])
		points = points + 10 + fg 

	else:
		#Condition for No SPARE
		points = points + sum

	print('Score for '+ str(c+1) + 'th turn: ', points)
	#sum = sum + 1
	c = c + 1

print('\nTotal points scored: ', points)
x = input('\nPress any key to exit...')
