import finalResult
import time
def print_dots_with_delay(count, delay):
    for _ in range(count):
        print(".", end="", flush=True)  
        time.sleep(delay)  
    print() 

result = finalResult.keys.lower()
# print(result)
if(result == "u got the treassure"):
    print("You are too close to the treassure",end="")
    print_dots_with_delay(3, 1)
    print("One step away", end="")
    print_dots_with_delay(3, 1)
    print("Oh my god you got the treassure. Its 10kg's of Gold")
    time.sleep(2)
    print("Congragulations you have cleared all the rounds")
else:
    print("Please give the keys correctly")