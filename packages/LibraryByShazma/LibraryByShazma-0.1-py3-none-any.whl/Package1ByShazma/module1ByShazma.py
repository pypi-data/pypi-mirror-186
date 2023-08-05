DEVELOPER = "Shazma Noor"
MENTOR = 'Dr. Arif Butt'
moduleNo = 1

#=====================+Help+====================
def help():
  print("This module# %d\nDeveloped By: %s\nPurpose: Basic Calculator\nMentor: %s" % (moduleNo,DEVELOPER, MENTOR) )

#===================+Calculator+================

#------------------Addition------------------
def myAddition(op1, op2):
  return op1+op2

#------------------Subtraction---------------
def mySubtraction(op1, op2):
  return op1-op2

#------------------Multiplication-------------
def myMultiplication(op1, op2):
  return op1*op2

#------------------Division-------------------
def myDivision(op1, op2):
  if op2 != 0:
    return op1/op2
  else:
    return "Divisor cannot be a 0"

#------------------Remainder------------------
def myModulo(op1, op2):
  return op1%op2