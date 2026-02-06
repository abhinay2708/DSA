n=int(input("Enter a Number:"))
num=n

while num>0:
    last_digit=num%10
    print(last_digit)
    num//=10

