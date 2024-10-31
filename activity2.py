try:
   num1,num2=eval(input("Enter two numbers sepeared by comma"))
   print("Result is ",num1/num2)
except ZeroDivisionError as ex:
   print("Division error",ex)
except SyntaxError as ex:
   print("Syntax error",ex)
except ValueError as ex:
   print("Exception",ex)
else:
   print("No exceptions or errors")
finally:
   print("Operation is complete")