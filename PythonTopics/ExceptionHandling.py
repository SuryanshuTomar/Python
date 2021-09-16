# while(True):
#     print("Press q to quit")
#     a = input("Enter number : ")
#     if a == 'q':
#         break
#     try:
#         print("checking....")
#         a = int(a)
#         if a > 6:
#             print("You entered a number greater than 6")
#         else:
#             print("You entered a number lesser than 6")
#
#     except Exception as e:
#         print(f"You input resulted in an error -> {e}")
#
# print("Thanks for playing this game !")

try:
    ip = int(input("Enter any number: "))
    cal = 1 / ip
    print(cal)

except ValueError as e:
    print("Please enter a valid value !")

except ZeroDivisionError as e:
    print("Don't divide the number by 0")

except Exception as e:
    print(e)
else:
    print("Code")

print("Sayonara !!!")
