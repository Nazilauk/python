#----------------------------------------------------------------------------------------
# this code, first initializes two variables sum and count to zero
# then enter a while loop that continues until the user enters -1. Inside the loop,
#  we get a number from the user and add it to the sum. We also increment the count.
# After the loop finishes, prints the average by dividing sum/count
#----------------------------------------------------------------------------------------

count = 0    # initializing three variables: count, total, and num.
total = 0  # count and total are used to calculate the average
num = 0  # num is used to store the number entered by the user.

while (num != -1):  # create a while loop to keep asking the user for a number until they enter -1
    num = int(input("Enter a number (Enter -1 to stop): "))
    if (num != -1):  # check if the number is not -1. If it's not,
        count += 1       # increment the count variable
        total += num     # add a number to total variable


if (count > 0):
    average = total / count
    print("The average of the numbers entered is:", average)
else:
    print("break, stop  requesting number from user: ")
