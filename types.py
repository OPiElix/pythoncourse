#5th python code as part of course (made on 26.08.2022)
#scope : python types

#python has a function that gives you the type of the variable
sth = input("enter something:")
print("entered: ", sth)
type_sth = type(sth)
print(type_sth)

#here a few examples for type()
anint = 45 #an integer
print("example: '", anint, "' is ", type(anint))
afloat = 34.64 #a float (floating-point number)
print("example: '", afloat, "' is ", type(afloat))
astring = "a s t r i n g" #a string (character string)
print("example: '", astring, "' is ", type(astring))

#so, if we want a string, for example a input, to be a int
#we can use int(), the wrapper function of the Integer class
number = input("enter a number:") #here is the input a string
entered_number = int(number) #now, the input string is a int
print("entered: ", entered_number) # and now we print a integer
print(type(entered_number)) #to be sure is works, we show the type

#now if we want a string, for example a input, to be a float
#we can use float(), the wrapper function of the Float class
numberF = input("enter a number:") #here is the input a string
entered_numberF = float(numberF) #now, the input string is a float
print("entered: ", entered_numberF) # and now we print a float
print(type(entered_numberF)) #to be sure is works, we show the type
