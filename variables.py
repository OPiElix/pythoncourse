#third python code as part of course (made on 25.08.2022)
#scope :  python variables

#a variable stores a value (content), in our case, a string
city = "Walldorf"
#this print() will print the value of the 'city' variable, which is "Walldorf"
print(city) #response : Walldorf

#as in the last part, if the city variable gets quotated, it isnt anymore a variable, but a string
print("city") #response : city

#now we will change the variable:
city = "Dudweiler"
print(city) #response : Dudweiler

#now we will make another variable
destination_city = "Walldorf"
#and replace the value of 'city' with the value of 'destination_city'
city = destination_city
#and now print it
print(city) #response : Walldorf

#the print() function can print more than one value!
print(1, 3.5, city, "string") #response : 1 3.5 Walldorf string