def merge_sort(C, D):
	A = []
	N = len(C) + len(D)
	i = 0; j = 0
	for k in range(N):
		print(k)
		if i < len(C) and C[i] < D[j]:
			A.append(C[i])
			i += 1
		elif j < len(D) and i != len(C) and j != len(D):
			A.append(D[j])
			j += 1
		elif i == len(C):
			A.extend(D[j:])
			#print (A)
			break
		elif j == len(D):
			A.extend(C[i:])
			#print(A)
			break
	return A

C = [1, 3, 5]; D= [2, 4, 6, 7, 8]
print(merge_sort(C, D))
