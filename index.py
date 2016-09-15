# My first python program
# Learn the basics of pyhton program

fName = "Princess Bini"
lName = "E.O\t" #/t adds a white space to the lName variable
age = 16
programOwner = fName + " " + lName + "sweet-" +str(age) #+ is to concatenate and str is to read an int as a string

#how to use list in python
treasures = ['family', 'God', 'love', 'peace', 'happiness']
treasures.append('faith') #adds an item to the end of the list
#print (programOwner + " I believe in " + treasures[1].upper() + ".")
#print ("My life treasures are:")
#print ((treasures))

#Learning loops
print ("Loop testing->")
for treasure in treasures:
    print ("\nTreasure is: " + treasure)

#print a range of numbers

for value in range(1,4):
    print ("\nRange of value is: " + str(value))

#make a list
valueList = list(range(1,4))
print(valueList)

#learn how to slice a list
valueList2 = ["Iria", "Val", "Ab","test"]
valueSlice = valueList2[:1]
print (valueSlice)