from collections import Counter
def solve(s):
	if len(s) > 26:
		return False

	counts = Counter(s)
	for v in counts.values():
		if v > 1:
			return False

	return True

print(solve("asadbek"))
print(solve("asl"))				
