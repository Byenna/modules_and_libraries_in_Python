
# 1. Start by importing the math module at the beginning of your code. You can do this by including the line `import math`.
import math
# 2. To calculate the square root of a given number, you can use the `math.sqrt()` function. Replace `number` with the desired number in the following line of code: `sqrt_of_number = math.sqrt(number)`. This will assign the square root of `number` to the variable `sqrt_of_number`.
sqrt_number = int(input("Van welk getal wil je de wortel weten? "))
sqrt_of_number = math.sqrt(sqrt_number)
# 3. To calculate the factorial of a number using the math module, you can use the `math.factorial()` function. Replace `number` with the desired number in the following line of code: `factorial_of_number = math.factorial(number)`. This will assign the factorial of `number` to the variable `factorial_of_number`.
fac_number = int(input("Van welk getal wil je de faculteit weten? "))
factorial_of_number = math.factorial(fac_number)
# 4. To calculate the value of pi using the math module, you can simply access the `math.pi` constant. For example, you can assign the value of pi to the variable `pi_value` with the following line of code: `pi_value = math.pi`.
pi_value = math.pi

print(f"De wortel van {sqrt_number} is: {sqrt_of_number}. De faculteit van {fac_number} is: {factorial_of_number} en de waarde van pi is {pi_value}.")
