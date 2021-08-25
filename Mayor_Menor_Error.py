largest = None
smallest = None
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp)
    except:
        print ("Invalid input")
    else:
        # This block will execute if no exception is caught.
        if smallest is None: #first number!
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print ("Maximum is", largest)
print ("Minimum is", smallest)
