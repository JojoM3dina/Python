# Program that displays the amount of calories burned per minute
# 20190319
# CTI-110 P4HW1 - Calories Burned
# Joe Medina
#Multiply the number of minutes by 5(the calories burned per minute)
#Calculate how many calories are burned after 20,35,45 minutes
#Display how many calories are burned after 20,35,45

for NumberOfMinutes in ( 20, 35, 45):
    CaloriesBurned = NumberOfMinutes * 5
    print( "You will burn", CaloriesBurned,"calories in",\
           NumberOfMinutes,"minutes")


