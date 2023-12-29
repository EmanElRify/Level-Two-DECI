# What is the expected output for the following piece of code
#ما هو الخرج المتوقع من الكود الاتي 
for i in range(2, 10, 2):
   print(i)
   # 2,4,6,8,10

# Write a piece of code that stars from a certain point to the
# end of it, and identify in a print statement if a number is even or odd
# اكتب كود يبدأ من نقطة وينتهي عند نقطة ويطبع اذا كان الاعداد بين النقطتين زوجية ام فرديا 
start = 0
stop = 10
odd_number = []
even_number = []

for i in range(start,stop):
   if i % 2 == 0:
      print("Even number: ", i)
      even_number.append(i)
   else:
      print("Odd number: ", i)
      odd_number.append(i)
print("odd numbers are: ",odd_number)
print("even numbers are: ",even_number)
name = 5
print(f"My name is {name} ")

      
      

