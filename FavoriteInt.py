print("What is your favorite integer?")
favIntStng = input()

try:
  favInt = int(favIntStng)
  if favInt%2 == 0:
    print(favInt, "is even")
  else:
    print(favInt, "is odd")

except:
  print("That is not a number")