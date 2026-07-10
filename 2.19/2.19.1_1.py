#19.1
#Exercise: Defining a variable and printing values
#Max score: 1
#The first exercise in this chapter is an easy warm-up exercise to get things rolling. The objective is to create a variable by giving it the correct name, and assign it the string "string-type content" as a value. Then insert this variable into a print command so that the program prints out following text:

#Our variable has a value which is string-type content. Isn't that nice?
#The trailing period can be added easily by editing the print command parameter sep. Other changes, such as the situation with the aposthrope can be done in the string given to the print command.

#Example output:
#Our variable has a value which is string-type content. Isn't that nice?


variable = "string-type content"
print("Our variable has a value which is", variable, ". Isn't that nice?", sep="")





#19.2
#Exercise: Counting with variables
#Max score: 1
#The second exercise continues with the basics of using variables. In this exercise, define two variables and assign them values of 1000 and 24. After this, make the interpreter do the calculation number1+number2+15 and then take the 2nd exponent (**2) of the result. Save this final result to a new variable, and make the program print the result in the following way:

#The final results of the calculation was: 1079521

#Example output:
#The final results of the calculation was: 1079521

number1 = 1000
number2 = 24
result = (number1 + number2 + 15) ** 2
print("The final results of the calculation was:", result)





#19.3
#Exercise: Type Conversions
#Max score: 1
#In this exercise the aim is to try out different datatypes. Start by defining two variables, and assign the first variable the float value 10.6411. The second variable gets a string "Stringline!" as a value.

#Convert the first variable to an integer, and multiply the variable with the string by 2. After this, finalize the program to print out the results in the following way:

#Integer conversion cannot do roundings: 10
#Multiplying strings also causes trouble: Stringline!Stringline!
#Example output:
#Integer conversion cannot do roundings: 10
#Multiplying strings also causes trouble: Stringline!Stringline!



var_float = 10.6411
var_string = "Stringline!"

print("Integer conversion cannot do roundings:", int(var_float))
print("Multiplying strings also causes trouble:", var_string * 2)




#19.4
#Exercise: Using layout characters
#Max score: 1
#In this program the objective is to understand how the layout-characters (\t and \n} and print in general works. By using only the print command, make the interpreter to print out the following text:

#This here is divided to several lines:
#I am still in the same print-command.
#	Name:	Peter
#	Job:	Babysitter
#With the first two lines it is possible to just use the line break. On the latter two tabulation is also needed.

#Example output:
#This here is divided to several lines:
#I am still in the same print-command.
# #Name:	Peter
# #Job:	Babysitter

print("This here is divided to several lines:\nI am still in the same print-command.")
print("\tName:\tPeter")
print("\tJob:\tBabysitter")







#19.5
#Exercise: Calculator, taking an input
#Max score: 1
#In this exercise, the objective is to try taking input for the first time. The idea is to create a simple program which takes two numbers and perfoms an addition. So, take two numbers from the user with input(), calculate the result and make the program present the result in the following way:

#Calculator
#Give the first number: 100
#Give the second number: 25
#The result is: 125
#In this exercise it is OK to expect that the user wont give faulty inputs, such as strings or something else non-calculatable. This exercise is also the starting point for the course's two "on-going" exercises, meaning that this code will be supplemented with new features in the future. Therefore it may be worthwhile to start commenting the source code.

#Example output:
#Calculator
#Give the first number: 6
#Give the second number: 7
#The result is: 13


# Starting the calculator program
print("Calculator")
num1 = input("Give the first number: ")
num2 = input("Give the second number: ")

# Convert input to integer before addition
result = int(num1) + int(num2)
print("The result is:", result)



#19.6
#Exercise: String slices
#Max score: 1
#The last exercise in this chapter focuses on string slices. Define a variable and assign it a string "desserts" as a value. Then create three new variables, and assign them values by slicing the A) first 4 characters B the last 4 characters and C the entire string backwards as given values. Then make the program print the answers in the following way:

#The first 4 characters were: dess
#The last 4 characters were: erts
#The string backwards was: stressed
#Example output:
#The first 4 characters were: dess
#The last 4 characters were: erts
#The string backwards was: stressed


word = "desserts"

# A) First 4 characters
part1 = word[:4]
# B) Last 4 characters
part2 = word[-4:]
# C) Entire string backwards
part3 = word[::-1]

print("The first 4 characters were:", part1)
print("The last 4 characters were:", part2)
print("The string backwards was:", part3)
