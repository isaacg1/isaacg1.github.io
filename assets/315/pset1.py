import random
random.seed(0)
trials = 1_000_000
u1_list = [random.random() for _ in range(trials)]
u2_list = [random.random() for _ in range(trials)]
s_list = [u1 + u2 for (u1, u2) in zip(u1_list, u2_list)]
d_list = [u1 - u2 for (u1, u2) in zip(u1_list, u2_list)]
es = sum(s_list) / trials
ed = sum(d_list) / trials

sd_list = [s * d for (s, d) in zip(s_list, d_list)]
esd = sum(sd_list)/trials
print("E[S]:", es, "E[D]:", ed, "E[SD]:", esd)

cov = esd - es * ed
print("Cov(S, D):", cov)
