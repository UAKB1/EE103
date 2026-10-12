x = float(input("What x to find the square root of? "))
guess = float(input("What guess to start with? "))

print("Current estimate square:", guess ** 2)

f_guess = guess ** 2 - x
f_prime_guess = 2 * guess
next_guess = guess - f_guess / f_prime_guess

print("Next guess:", next_guess)
