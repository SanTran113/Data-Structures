height = input("What is your height in centimeters? ")
cost = input ("How much can you pay? ")

if int(height) > 137 and int(cost) > 10:
    print("Enjoy the ride!")
elif int(height) > 137 and int(cost) < 10:
    print("You are not tall enough to ride")
elif int(height) < 137 and int(cost) > 10:
    print("You do not have enough credits")
else:
    print("You have not met either requirement")