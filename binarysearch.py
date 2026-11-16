import random
import time
array = []
for i in range(50):
    array.append(random.randint(0,50))
    
array.sort() 
print(array)

high = len(array) - 1
print(high)
low = 0
sV = int(input("Input: "))



while True:
    mid = (low + high) // 2
    print(mid)
    time.sleep(1)
    if array[mid] == sV:
        print(f"Value found at index {mid}, number: {sV}")
        break
    
    elif array[mid] <= sV:
        low = mid
        
    elif array[mid] >= sV:
        high = mid




