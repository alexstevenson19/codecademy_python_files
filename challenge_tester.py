def  find_sum_and_avg(ints):
    sum = 0
    odd_sum = 0
    avg = 0
    for n in ints:
    	print n
        sum += n
        if n % 2 == 0:
            odd_sum += n
    
        avg = sum / len(ints)
    return odd_sum, avg


print find_sum_and_avg([5,1,2,3,4,5])

print "===================================="

# Complete the function below.
def remove_n_duplicates(n, int_array):
    # need to count and keep track of items.
    # option one, store matched items in a list, then check the length of the list. any that match length 'n' are then taken out of the list.
    # option two, sort the order of the list first, then check the contents and add to a counter each time the same item is encountered. When the counter reaches 'n' do one more check. If negative, delete value.
    i = 0
    dup = 0
    store = ""
    delete = ""
    new_array = []
    # int_array.sort - don't quite recall how this works in Python at the moment. Maybe the same as Ruby? Or maybe not, nothing is returned?
    print(int_array)
    for num in int_array:
        if int_array[i] == int_array[ i + 1]:
            dup += 1
            if dup == n:
                store = int(i)
        
        if dup == n: # I want to match the value and delete all matches from array
            delete = int_array[store]     # I can't remember the built in function for this in Python, so I will loop through again and match it that way.
            for match in int_array:
                if match == delete:
                    print int_array.remove(match)
    return new_array

print remove_n_duplicates(2, [3, 7, 1, 9, 9])




