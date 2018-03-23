def find_smallest_pos(int_arr):
    # First, set every entry in int_arr which is 0 to -1
    for i in range(len(int_arr)):
        if int_arr[i] == 0:
            int_arr[i] = -1

    # Iterate through the list, if we find a positive number, we set the 
    # entry of int_arr[k -1] to 0, and cascade further down until we no 
    # longer have an entry with a positive value
    for i in range(len(int_arr)):
        if int_arr[i] > 0: 
            x = int_arr[i]

            while x > 0 and x <= len(int_arr):
                temp = int_arr[x - 1]
                int_arr[x - 1] = 0

                x = temp

    # Find the first index with a nonzero entry, otherwise the answer is 
    # the length of int_arr
    for i in range(len(int_arr)):
        if int_arr[i] != 0:
            return i + 1

    return len(int_arr) + 1

# Main function for the user
def main():
    number_of_entries = int(input("Number of entries: "))
    integers = []

    while(number_of_entries > 0):
        user_input = int(input("Enter a number: "))
        integers.append(user_input)
        number_of_entries -= 1

    smallest_missing_int = find_smallest_pos(integers)

    print("Lowest missing positive integer: {}".format(smallest_missing_int))

if __name__ == '__main__':
    main()