#Mixing primary colors to form secondary colors.
#CTI-110
# P3HW1 - Color Mixer
# Joe Medina
# 20190228
#Input the two primary colors.
#Calculate which secondary color is formed from the two primary colors.
#Display the formed secondary color.
primaryColor1 = input("Enter primary color 1:")
primaryColor2 = input("Enter primary color 2:")
if primaryColor1 == "red" and primaryColor2 == "blue" or \
   primaryColor1 == "blue" and primaryColor2 == "red":
    print( primaryColor1 + " mixed with " + primaryColor2 + " is purple ")
elif primaryColor1 == "red" and primaryColor2 == "yellow" or \
     primaryColor1 == "yellow" and primaryColor2 == "red":
    print( primaryColor1 + " mixed with " + primaryColor2 + " is orange ")
elif primaryColor1 == "blue" and primaryColor2 == "yellow" or \
     primaryColor1 == "yellow" and primaryColor2 == "blue":
    print( primaryColor1 + " mixed with " + primaryColor2 + " is green ")
     
