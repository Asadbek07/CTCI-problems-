from collections import Counter

def solve(s1, s2):
	s1 = s1.translate({ord(' ') : ''}).lower()
	s2 = s2.translate({ord(' ') : ''}).lower()
	counts1 = Counter(s1)
	counts2 = Counter(s2)
	counts = counts1 - counts2
	for v in counts.values():
		if v != 0:
			return False
	return True
	
print(solve('asad', 'Asad '))			

# Time : O(N)
# Space : O(N) since we used hash table 