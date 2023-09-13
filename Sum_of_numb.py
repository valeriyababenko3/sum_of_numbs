#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum_list_numbers(input_list):
    total = 0
    for num in input_list:
        total += num
    return total

my_list = [8, 2, 3, 0, 7]


result = sum_list_numbers(my_list)
print("Summary of the numbers in the list:", result)
