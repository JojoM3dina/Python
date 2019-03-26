# Program calculates the total amount of bugs collected throughout 5 days.
# 20190319
# CTI-110 P4T2 - Bug Collector
# Joe Medina
#set total= 0
#for each of days:
        #input bugs collected for a day
        #add bugs collected to total
#Display Total
#Initalize the accumulator.
total = 0

#Get th bugs collected for each day.
for day in range(1, 5):
    print('Enter the bugs collected on day', day)
    
    bugs = int(input())
    total = total + bugs

#Display the total bugs.
print('You collected a total of ', total, 'bugs.')
