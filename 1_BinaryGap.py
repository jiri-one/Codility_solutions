def solution(N):
	string_of_bin = str(bin(N))[2:].split("1")
	if "0" in string_of_bin[-1]:
		string_of_bin.pop(-1)
	zeros = [x for x in string_of_bin if x]
	if len(zeros) == 0:
		return 0
	zeros.sort(key=len, reverse=True)
	return len(zeros[0])

# test
print(solution(51712))