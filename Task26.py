numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
list_even = []
list_odd = []

def count_def():
    for i in numbers:
        if i % 2 == 0:
            list_even.append(i)
        elif i % 2 != 0:
            list_odd.append(i)
    # print(list_even)
    # print(list_odd)
    print(f"\nThere are {len(list_even)} even numbers in list 'numbers'")
    print(f"\nThere are {len(list_odd)} odd numbers in list 'numbers'")   

print(numbers, end = " \n")
count_def()
