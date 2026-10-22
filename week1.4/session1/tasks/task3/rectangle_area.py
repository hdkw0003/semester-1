
# function implementation

def rectangle_area( ):  # define suitable input data
    # ...               # implement the function
    return              # return an appropriate value


def rectangle_area( ):
    length = int(input("Please enter the length of the rectangle. "))
    width = int(input("Please enter the width of the rectangle. "))
    rectangle_area = ((length) * (width))
    return rectangle_area

rectangle_area = rectangle_area( )


# testing the function

   # provide suitable data matching your inputs


def even_values_printer():
    maxvalue = int(input("Please enter a value. "))
    x = 0
    while x < maxvalue:
        x = x + 1
        if x % 2 == 0:
            print (x)
        if x % 2 == 1:
            continue
        if x == maxvalue:
            break

def numbermeans():
    numberlist = (input("Please enter a list of numbers separated by spaces. "))
    numbers = {int(x) for x in numberlist.split()}
    numbers = sorted(numbers)
    print(numbers)
    numbermean = (sum(numbers) / len(numbers))
    print (numbermean)

print(f"Area is {rectangle_area}cm")

even_values_printer()

numbermeans()
