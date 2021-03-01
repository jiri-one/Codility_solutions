def solution(A, K):
	dict_A = dict(enumerate(A))
	moved_dict_A = {}
	for _ in range(K):
		# if you want move to the left
		#for index, value in dict_A.items():
			#if index == len(dict_A)-1:
				#moved_dict_A[len(dict_A)-1] = dict_A[0]			
			#else:
				#moved_dict_A[index] = dict_A[index+1]
		
		# if you want move to the left
		for index, value in dict_A.items():
			if index == 0:
				moved_dict_A[0]	= dict_A[len(dict_A)-1]	
			else:
				moved_dict_A[index] = dict_A[index-1]		
		dict_A = moved_dict_A.copy()
	return list(dict_A.values())
# test
print(solution([1, 2, 3, 4, 5], 2))