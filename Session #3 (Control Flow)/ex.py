# Write a program that takes an input number and checks whether it's a multiple of 3, 5, or both.
# If it's a multiple of both, print "Divisible by both 3 and 5", if it's only a multiple of 3, print
# "Divisible by 3", if it's only a multiple of 5, print "Divisible by 5".
# If it's not a multiple of either, print "Not divisible by 3 or 5".
# اكتب برنامجًا يأخذ رقمًا مُدخلًا ويتحقق مما إذا كان من مضاعفات الرقم 3 أو 5 أو كليهما.
# إذا كان مضاعفًا لكليهما، فاطبع "قابل للقسمة على 3 و5"، وإذا كان مضاعفًا للرقم 3 فقط، فاطبع
# "القسمة على 3"، إذا كان فقط من مضاعفات 5، فاطبع "القسمة على 5".
# إذا لم يكن من مضاعفات أي منهما، فاطبع "غير قابل للقسمة على 3 أو 5".
z = int(input("Enter an integer: "))
if z % 3 == 0 and z % 5 == 0:
    print("Divisible by both 3 and 5")
elif z % 5 == 0:
    print("Divisible by 5")
elif z % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3 or 5")

# i = int(input("Enter a number : "))
# if i%3 == 0 and i%5 == 0:
#     print(i ," is divisble by 3 and 5")
# elif i%3 == 0  :
#     print(i ," is divisble by 3")
# elif  i%5 == 0 :
#     print(i ," is divisble by 5")
# else:
#     print(i, "isn't divisble by 3 or 5")

if z % 3 == 0:
    if z % 5 == 0:
        print("Divisible by both 3, 5")
    else:
        print("Divisible by 3")
elif z % 5 == 0:
        print("Divisible by 5")
else:
         print("Not Divisible by neither 5 nor 3")
         


    
# Create a program that prompts the user to enter a character and checks if it's
# a vowel (a, e, i, o, u), a consonant, or neither.
# قم بإنشاء برنامج يطلب من المستخدم إدخال حرف والتحقق مما إذا كان 
# حرف متحرك (a، e، i، o، u)
# ، أو حرف ساكن، أو لا شيء.

