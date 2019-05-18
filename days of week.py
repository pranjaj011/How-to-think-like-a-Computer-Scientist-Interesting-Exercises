starting_day = int(input("What is your starting day from 0-6?"))
length_stay = int(input("How many nights are you planning to stay?"))
return_day = (starting_day + length_stay)%7
print("You return on", starting_day)
