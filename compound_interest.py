principle = 0
rate = 0
time = 0



while True:  
  principle = float(input("enter the principle amount : "))
  if principle <= 0:
    print("principle can't be less than or equal to zero")
  else:
    break
    

while True:
  rate = float(input("enter the rate amount : "))
  if rate < 0:
    print("rate can't be less than or equal to zero")
  else:
    break  

while True:
  time = float(input("enter the time amount : "))
  if time < 0:
    print("time can't be less than or equal to zero")
  else:
    break

total = principle * pow((1+rate/100), time)

print(f"Balance after {time} years : ${total}")
