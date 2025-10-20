import random, math

random.seed(0)

def sample():
    time_so_far = 0
    gotten_heads = False
    while not gotten_heads:
        time_so_far += random.expovariate(1)
        gotten_heads = random.random() < 0.5
    return time_so_far

num_samples = 1_000_000
samples = [sample() for _ in range(num_samples)]

counts = [0, 0, 0, 0]
for sample in samples:
    for (i, cutoff) in enumerate([1, 2, 3, 4]):
        if sample >= cutoff:
            counts[i] += 1

print("Part (a):", [count/num_samples for count in counts])
print("Part (b):")
total_ratio = 0
for i in [1, 2, 3]:
    print(i, ":", counts[i]/counts[i-1])
    total_ratio += counts[i]/counts[i-1]

average_ratio = total_ratio/3
print("Average ratio:", average_ratio)
print("Lambda estimate:", -math.log(average_ratio))

