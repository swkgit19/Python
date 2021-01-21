
#  Variable
print("\nVariable:")

print("\nString:")
greeting = "Hello World"
greeting1 = greeting.split(" ")[0]
greeting2 = greeting.split(" ")[1]
greeting3 = greeting1 + " Nick"
greeting4 = greeting1 + " Mary"
greeting5 = greeting1 , "Tom"
greeting6 = greeting5[0]
greeting7 = greeting5[1]

print("greeting = Hello World, Output = " , greeting)
print("greeting1 = greeting.split(" ")[0], Output = " , greeting1)
print("greeting2 = greeting.split(" ")[1], Output = " , greeting2)
print("greeting3 = greeting1 + \" Nick\", Output = " , greeting3)
print("greeting4 = greeting1 + \" Mary\", Output = " , greeting4, "\n")
print("greeting5 = greeting1 , \"Tom\", Output = " , greeting5)
print("greeting6 = greeting5[0], Output = " , greeting6)
print("greeting7 = greeting5[1], Output = " , greeting7, "\n")

print("\nNumber:")
number1 = 1
number2 = 20
number3 = 30

total = number1 * number2 + number2 * number3

print("number1 = ", number1)
print("number2 = ", number2)
print("number3 = ", number3)
print("number1 * number2 + number2 * number3 = ", total, "\n")

print("\nHexadecimal:")
hexa1 = 0x01
hexa2 = 0x0A
hexa3 = 0x14

total = hexa1 * hexa2 + hexa2 * hexa3

print("hexa1 = 0x01, Output = ", hexa1)
print("hexa2 = 0x0A, Output = ", hexa2)
print("hexa3 = 0x14, Output = ", hexa3)
print("hexa1 * hexa2 + hexa2 * hexa3 = ", total, "\n")

print("\nBinary:")
binary1 = 0b0001
binary2 = 0b1010
binary3 = 0b1111

total = binary1 * binary2 + binary2 * binary3

print("binary1 = 0b0001, Output = ", binary1)
print("binary2 = 0b1010, Output = ", binary2)
print("binary3 = 0b1111, Output = ", binary3)
print("binary1 * binary2 + binary2 * binary3 = ", total, "\n")

print("\nDecimal:")
# To do, Set the precision to 6 number.
deci1 = 1
deci2 = 7
Divide = deci1 / deci2
print("deci1 = 1, Output = ", deci1)
print("deci2 = 7, Output = ", deci2)
print("Divide = deci1 / deci2, Output = ", Divide)
print("Divide = deci1 / deci2, Output = ", round(Divide,3) , " Rounded to 3 decimal place. \n")

