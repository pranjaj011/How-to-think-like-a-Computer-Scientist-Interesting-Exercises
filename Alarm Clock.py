time_now = int(input("What is the time right now(in hours)?"))
time_wait = int(input("How many hours should I wait before the alarm?"))
TwentyFour = (time_now+time_wait)%24
print("It is", TwentyFour, "when the alarm goes off")
