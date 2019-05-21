P = 10000
n = 12
r = 0.08
t = int(input("How many years before you take the money out?"))
A = P*(1+(r/n))**(n*t)
print("your money after", t, "years is", A)
