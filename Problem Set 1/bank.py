#ask for greeting
#m = input("Hello!" )
#account for case insensitive answers
#i = m.lower()
#if greeting starts with h, return 20 bucks
#if i = "hello" 
 # print("$0")
#if greeting is hello return nothing
#elif m.startswith("h") 
 # print("$20")
#else, return 100 bucks
#else:
 # print("$100)

#alternative for checking for h answer
#elif h == i[0] 

#take 2
user_input = input().lower()
if user_input.startswith("hello"):
  print("$0")
elif user_input.startswith("h"): 
  print("$20")
else:
  print("$100")

