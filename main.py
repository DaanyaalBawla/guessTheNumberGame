#import random
#special_num= random.randrange(1,10)
#uI = 0
#while int(uI) != int(special_num) :
#  uI = input("Guess a number between 1 and 10: ")
#  if int(uI) > int(special_num): 
#    print("Your Guess is too high")
#  elif int(uI) < int(special_num): 
#    print("Your guess is too low")
#else:
#  print("That's the number! Good job! :D")
import random
special_num= random.randrange(1,10)
while True :
  try:
    user_guess = int(input("Guess a number between 1 and 10: "))
  except ValueError:
    print("That's not a number.")
    user_guess = input("Guess a number between 1 and 10: ")   
  else:
    if int(user_guess) > special_num:
      print("Your Guess is too high")
    elif int(user_guess) < special_num:
      print("Your Guess is too low")
    else:
      print("That's the number! Good job! :D")     
      quit()
  