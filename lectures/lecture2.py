r =5
pi = 3.14
volume_of_sphere = 4/3 * pi * r**3
print(volume_of_sphere)

first = "Hello"
second = "World"
print(first+second)

print("Ho"*5)

coverPrice_discounted = 24.95*0.6
copy = 60
shipping = 3 + (copy-1)*0.75
totalCost = (coverPrice_discounted*copy)+shipping
print(totalCost)


#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?●(Write using input function!)

coverPrice =2495
discount = 0.4
shipping_first_book = 300
shipping_additional = 75
copies = 60
costBooks = coverPrice*(1-discount)*copies
costShipping = shipping_first_book + (copies-1)*shipping_additional
costTotal = costBooks + costShipping
print("The total wholesale cost for 60 copies is " , costTotal , " cents.")

#coverPrice = int(input("Please input the cover price as cents:" ))
#discount = float(input("Please input the discount rate:"))
#shipping_first_book = int(input("Please input the shipping cost of the first book as cents:"))
#shipping_additional = int(input("Please input the shipping cost of additional books as cents:"))
#copies = int(input("Please input the number of copies you would like to get:"))
costBooks = coverPrice*(1-discount)*copies
costShipping = shipping_first_book + (copies-1)*shipping_additional
costTotal = costBooks + costShipping
#print("The total wholesale cost for 60 copies is " , costTotal , " cents.")



#A book club promises to send 8 books for $1, if you join the club.
# After you receive the first 8 books, you may select more books at a rate of $19.99 per book.
# If you spend a total of $80.96, how many extra books did you purchase?

price_of_first_8_books = 100
price_of_the_rest = 1999
total_spent = 8096
number_of_extra_books = (total_spent-price_of_first_8_books)/price_of_the_rest
print("You purchased" , number_of_extra_books , " extra books.")


#If I leave my house at 6:52 am and run 1 mile at an easy pace (8 minutes per mile),
# then 3 miles at tempo (6 minutes per mile) and 2 mile at easy pace again,
# what time do I get home for breakfast?

from datetime import datetime
from datetime import timedelta
easy_pace_time = (1+2)*8
tempo_time = 3*6
total_time = int(easy_pace_time+tempo_time)
#time = "06:52"
#start_time =
#breakfast_time = start_time + timedelta(minutes=total_time)
#print("You will get home at" , breakfast_time , " for breakfast.")
print("You will get home at " , "07:" , total_time-8 , " for breakfast.")