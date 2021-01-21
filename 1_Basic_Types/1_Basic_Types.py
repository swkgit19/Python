
# Number
print("\nNumber:")
y = 5 + 5
print("5 + 5 = ", y)
y = int('5') + int('6')
print("int('5') + int('6') = ", y, "\n")

# Float
print("Float:")
y = float(5.115) + float(7.755)
#x = float("{0:.3f}".format(y)) # Set float precision to 3 decimal place.
print("float(5.115) + float(7.755) = ", round(y,3), " using 3 decimal place precision\n")

# Complex Number
print("Complex Number:")
print("1 + 2j = ", 1 + 2j, "\n")

#  String
print("String:")
y = "Hello World!!"
print("Hello World !! = ", y)

y = str(5) + str(6)
print("str(5) + str(6) = ", y, "\n")
# Answer = '56'

#  String Manipulation
print("String Manipulation(Using Split):")
y = "Mary:John:Mike"
print("String is ", y)
print("My name is", y.split(":")[0])
print("My name is", y.split(":")[1])
print("My name is", y.split(":")[2], "\n")

#  Boolean
print("Boolean:")
print("True =               " , True)
print("False =              " , False)
print("5 == 5               ", 5 == 5)
print("5 == 6               ", 5 == 6)
print("True is True =       " , True is True)
print("True is not True =   " , True is not True)
print("False is True =      " , False is True)
print("False is False =     " , False is False)
print("\'True\' == True =     " , 'True' == True) # Warning message with 'True' is True
print("'This' == 'This' =   " , 'This' == 'This', "\n") # Warning message with 'This' is 'This'

#  Tuple
print("Tuple:")
y = (1, 2, 3)
print("(1,2,3) = " , y)
print("(1,2,3)[0] = " , y[0])
print("(1,2,3)[1] = " , y[1])
print("(1,2,3)[2] = " , y[2], "\n")

#  Set
print("Set:")
y = {'red', 'green', 'blue'}
print("{'red', 'green', 'blue'} = " , y, "Random arrangement of letter.")
print("{'red', 'green', 'blue'} = " , y, "Random arrangement of letter.")
print("{'red', 'green', 'blue'} = " , y, "Random arrangement of letter.\n")
