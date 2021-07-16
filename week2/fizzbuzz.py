# write a program that prints the numbers from 1 to 100
# but for multiple of 3, print "Fizz" instead of the number
# and for multiple of 5, print "Buzz"
# for multiles of both 3 and 5, print "FizzBuzz"

# Hint: % (modulo) tells you remainder of a division

for n in range (1, 101):
    if not n % 15:  print("FizzBuzz")
    elif not n % 3: print("Fizz")
    elif not n % 5: print("Buzz")
    else:           print(n)
