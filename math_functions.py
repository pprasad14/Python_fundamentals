import math

#ceiling
print(math.ceil(3.4)) # 4

#floor
print(math.floor(9.9)) # 9

#fabs, returns a floating ablsolute value
print(math.fabs(-10))  #10
print(math.fabs(-234.56))

#copysign(x,y), returns x with the sign of y
print(math.copysign(10,-5))  # -10
print(math.copysign(-10,5))

#factorial
print(math.factorial(4)) # 24

#fmod(x,y), returns remainder when x is divided by y
print(math.fmod(23,3))  # 2

#fsum(), returns floating point sum of values in an iterable
print(math.fsum([1,2.3,4,5.6]))

#isfinite()
print(math.isfinite(23))

#pow()
print(math.pow(2,3))  #8.0

#sqrt()
print(math.sqrt(34))

