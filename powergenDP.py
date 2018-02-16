from collections import defaultdict
import random


def is_on(status):
	#status is a string
	if status > 0:
		return 1
	else: 
		return 0

M = defaultdict(lambda : defaultdict(int))

MIN_OFF = 2
MIN_ON = 3
HOURS = 6
START = 200
S = list(range(-MIN_OFF, MIN_ON + 1))
S.remove(0)
H = list(range(0, HOURS))
H.remove(HOURS - 1)
H.reverse()



P = defaultdict(int)
P[0] = 200
P[1] = -200
P[2] = -300
P[3] = 700
P[4] = -400
P[5] = 100

# for x in range(0, HOURS):
# 	P[x] = random.randint(-40,100)

end = HOURS - 1

for s in S:
	if 0 < s and s < MIN_ON:
		
		M[end][s] = P[end]

	if -MIN_OFF < s and s < 0:

		M[end][s] = 0

	if s == MIN_ON:

		if P[end] >= 0:
			M[end][s] = P[end]
		else:
			M[end][s] = 0
	
	if s == -MIN_OFF:
		if P[end] < START:
			M[end][s] = 0
		else:
			M[end][s] = P[end] - START
#print(M)

for h in H:
	for s in S:
		if 0 < s and s < MIN_ON:
			M[h][s] = M[h + 1][s+1] + P[h]

		if -MIN_OFF < s and s < 0:
			M[h][s] = M[h+1][s-1]

		if s == MIN_ON:
			M[h][s] = max(M[h + 1][s] + P[h], M[h + 1][-1])	
		
		if s == -MIN_OFF:
			M[h][s] = max(M[h + 1][1] + P[h] - START, M[h + 1][s])
				
print(M)
print(" ")

s_prime = 3#max(M[0], key=M[0].get)
print("S': " + str(s_prime))
max_profit = M[0][s_prime]
print("Max Profit: " + str(max_profit))

V = []
V.append(is_on(s_prime))
H = list(range(1, HOURS))

for h in H:
	print(" ")
	if 0 < s_prime and s_prime < MIN_ON:
		print("0 < s_prime and s_prime < MIN_ON")
		print("hours: " + str(h))
		print(s_prime)
		s_prime += 1
	elif -MIN_OFF < s_prime and s_prime < 0:
		print("-MIN_OFF < s_prime and s_prime < 0")
		print("hours: " + str(h))
		print(s_prime)
		s_prime -= 1
	elif s_prime == MIN_ON:
		print("s_prime == MIN_ON")
		print("hours: " + str(h))
		print(s_prime)
		#if M[h-1][s_prime] - P[h-1] == M[h][s_prime]
		if M[h-1][s_prime] == M[h][-1]:
			s_prime = -1
	elif s_prime == -MIN_OFF:
		print("s_prime == -MIN_OFF")
		print("hours: " + str(h))
		print(s_prime)
		if M[h-1][s_prime] + START == M[h][1]:
			s_prime = 1
	else:
		print("hours: " + str(h))
		print(s_prime)
		s_prime = s_prime

	V.append(is_on(s_prime))
print(V)






