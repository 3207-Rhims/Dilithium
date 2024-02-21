from dilithium import Dilithium5


pk, sk = Dilithium5.keygen()
msg = b'OSHA'


#sig = Dilithium3.sign(sk, msg)
#assert Dilithium2.verify(pk, msg, sig)

# Verification will fail with the wrong msg or pk
#assert not Dilithium2.verify(pk, b"", sig)
pk_new, sk_new = Dilithium5.keygen()
#assert not Dilithium2.verify(pk_new, msg, sig)

import time
import subprocess

# Your function to generate hash values
def generate_hash():
    start = time.time()
    result = pk, sk = Dilithium5.keygen()
    print(pk,sk)
    end = time.time()
    return end - start
    #print(result)
'''
# Record the start time
start_time = time.time()

# Call your function to generate hash values
for _ in range(1000):
  num = generate_hash()

# Record the end time
end_time = time.time()

# Calculate the time taken3
time_taken = end_time - start_time

print(f"Time taken: {time_taken * 1000:.2f} milliseconds")'''


import time
from dilithium import Dilithium3
import statistics

# Store the time values for each iteration
time_values = []

# Generate hash values and record the time for each iteration
for _ in range(1000):
    time_taken = generate_hash()
    time_values.append(time_taken)

# Calculate the median time
median_time = statistics.median(time_values)
time_taken = generate_hash()
print(f"Median time taken: {median_time * 1000:.2f} milliseconds")



#Use cProfile to profile the function
import cProfile

profile = cProfile.Profile()
profile.enable()

# Call your function to generate hash values
generate_hash()

# Disable profiling and print the results
profile.disable()
profile.print_stats(sort='cumulative')



'''
import timeit

print(timeit.timeit(generate_hash, globals=globals(), number=10)) '''




