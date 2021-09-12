
# Solution with additional datastructure
from collections import Counter
def solve(s):
	if len(s) > 26:
		return False

	counts = Counter(s)
	for v in counts.values():
		if v > 1:
			return False

	return True

print(solve("asadbek"))  # False
print(solve("asl"))		 # True		

# Time complexity : O(N)
# Space complexity : O(N) -> We used hash table that's why space is O(N) 