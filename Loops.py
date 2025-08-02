while True:
    try:
        n = int(input("What is X?"))
    except ValueError:
        print("X must be an integer.")
        continue
    if n < 0:
        print("X must be a non-negative integer.")
        continue
    else:
     break
for _ in range(n):
   print("wow \n",end="") 

