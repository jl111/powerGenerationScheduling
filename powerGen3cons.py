from collections import defaultdict
import random



def is_on(status):
	#status is a string
	if status > 0:
		return 1
	else: 
		return 0

#holds profit
M = defaultdict(lambda : defaultdict(int))
#hold number of starts
D = defaultdict(lambda : defaultdict(int))


MIN_OFF = 1
MIN_ON = 1
MAX_STARTS = 2
HOURS = 10
START = 200
S = list(range(-MIN_OFF, MIN_ON + 1))
S.remove(0)
H = list(range(0, HOURS))
H.remove(HOURS - 1)
H.reverse()



P = defaultdict(int)

for x in range(0, HOURS):
 	P[x] = random.randint(-100,100)

end = HOURS - 1

for s in S:
	if 0 < s and s < MIN_ON:
		
		M[end][s] = P[end]
		D[end][s] += 1

	if -MIN_OFF < s and s < 0:

		M[end][s] = 0

	if s == MIN_ON:

		if P[end] >= 0:
			M[end][s] = P[end]
			D[end][s] += 1
		else:
			M[end][s] = 0
	
	if s == -MIN_OFF:
		if P[end] < START:
			M[end][s] = 0
		else:
			M[end][s] = P[end] - START
			D[end][s] += 1
#print(M)

for h in H:
	for s in S:
		D[h][s] = D[h + 1][s]
		if 0 < s and s < MIN_ON:
			M[h][s] = M[h + 1][s + 1] + P[ h ]

		if -MIN_OFF < s and s < 0:
			M[h][s] = M[h + 1][s - 1]

		if s == MIN_ON:
			if D[h][s] == MAX_STARTS:
				M[h][s] = M[h + 1][s] + P[ h ]
			else:	
				M[h][s] = max(M[h + 1][s] + P[ h ], M[h + 1][-1])	
				if M[h][s] == M[h + 1][-1]:
					D[h][s] += 1

		if s == -MIN_OFF:
			M[h][s] = max(M[h + 1][1] + P[h] - START, M[h + 1][s])	
#print(M)
print(" ")

s_prime = max(M[0], key=M[0].get)

max_profit = M[0][s_prime]

print(D[0][s_prime])

V = []
V.append(is_on(s_prime))
H = list(range(1, HOURS))

for h in H:
	if 0 < s_prime and s_prime < MIN_ON:

		s_prime += 1

	elif -MIN_OFF < s_prime and s_prime < 0:

		s_prime -= 1

	elif s_prime == MIN_ON:

		if M[h-1][s_prime] == M[h][-1]:
			s_prime = -1

	elif s_prime == -MIN_OFF:

		if M[h-1][s_prime] + START - P[h-1] == M[h][1]:
			s_prime = 1
	else:
		s_prime = s_prime


	V.append(is_on(s_prime))

print("NUM STARTS")

print('SCHEDULE')
print(V)
print("MAX STARTS")
print(D)












