#ask for input
expression = input("Give me math! ")
#format as x y z
x, y, z = expression.split(" ")
#turn input into float
x_final = float(x)
z_final = float(z)
#interpret numbers
if y == "+":
  result = x_final + z_final
if y == "-":
  result = x_final - z_final
if y == "*":
  result = x_final*y_final
if y == "/":
  result = x_final/y_final
print(result)
