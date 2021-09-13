
# Solution with additional datastructure
from collections import Counter
def solve(s):
	if len(s) > 128:
		return False

	counts = Counter(s)
	for v in counts.values():
		if v > 1:
			return False

	return True

print(solve("asadbek"))  # False
print(solve("asl"))		 # True		

# Time complexity : O(N)
# Space complexity : O(1) -> Because loop never iterate more than 128 characters 

def solve_2(s):
	checker = 0
	for i in s:
		val = ord(i) - ord('a')
		if (checker & (1 << val) > 0):
			return False

		checker |= (1 << val)
	return True
	
print(solve_2('asad'))
print(solve_2('asd'))			