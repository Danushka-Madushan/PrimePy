''' In the tuple below, the first is the start and the second is the end
If you want to find prime numbers between 1 and 100 set to the following variable to rng = (1, 100) '''
rng = (1, 10)

nums = []
for x in range(rng[0], rng[1]+1):
	e = {}
	e.setdefault(x, [])
	for a in range(rng[0], rng[1]+1):
		if x == a:
			pass
		elif x%a == 0:
			e[x].append(a)
	nums.append(e)

primes = [x+1 for x in set([nums.index(nums[i]) if len(nums[i][i+1]) == 1 else 0 for i in range(len(nums))])]
primes.sort()

print(primes)

# output = [1, 2, 3, 5, 7]