import time

initial = time.time()
print(initial)

k = 0
while (k < 10):
    print("DeathSlayer")
    k += 1

print("While loop time duration", time.time() - initial, "Seconds")

print()

for i in range(10):
    print("Alex Mercer")

initial2 = time.time()
print("For loop time duration", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
