balance=0
rate=0
year=0

while True:
    balance=float(input("enter a total balance you have:$"))
    if balance<0:
        print("balance cann't be a less then 0 ")
    else:
            break
while True:
    rate=float(input("enter a rate % :"))
    if rate<0:
        print("rate cann't be a less then 0 ")
    else:
            break
while True:
    year=int(input("enter a time in years:"))
    if year<0:
        print("years cann't be a less then 0 ")
    else:
            break
total= balance *(1+rate/100)**year)
print(f"balance after {year}year/s:${total:.2f}")
