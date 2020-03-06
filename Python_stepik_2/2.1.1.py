try:
	foo()
except (AssertionError, ZeroDivisionError﻿) as e:
	print(type(e).__name__)
except	ArithmeticError as e:
	print('ArithmeticError')




# except Exception as e:
	# print(str(type(e))[8:-2])
	# print(type(e).__name__)
# 	if 'ZeroDivisionError' in str(type(e)):
# 		print("ZeroDivisionError")
# 	elif 'ArithmeticError' in str(type(e)):
# 		print("ArithmeticError")
# except AssertionError as e:
# 	print(type(e).__name__)
# print(type(AssertionError()))
# print(str(type(AssertionError()))[8:-2])