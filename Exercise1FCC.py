'''Exercise of  loops from free code camp'''

print("->Enter any number\n\n"
      "->once you entered your numbers just type Done\n\n"
      
      "->And it will calculate the count of numbers ,Sum and Average\n")
count = 0
sum = 0

while True:
    user = (input('Enter a number :'))
    if user == 'done' :
       break
    # Using exception handling to give error
    try:
        fuser = float(user)

    except ValueError:
        print("Invalid Input enter any integar or just write done if you want to end the calculations")
        continue

    count = count + 1
    sum = sum + fuser

print(f"Total numbers are {count}")
print(f"Sum of the numbers is :{sum}")

print("Average is", sum / count)
print("All done")

# fuser = float(user)
# print(fuser)



