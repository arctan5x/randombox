import random
import math
import time

def estimate_pi(sim_num=10000):
	coords_in_circle = 0
	for i in range(sim_num):
		x, y = random.random(), random.random()
		if (x**2 + y**2) < 1:
			coords_in_circle += 1
	return 4 * coords_in_circle / sim_num

start_time = time.time()
pi = estimate_pi()
print(f"Estimated pi is {pi}")
end_time = time.time()
print(f"Elapsed_time is {end_time - start_time}")



