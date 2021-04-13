# Jake Billard   UHID 1582534


# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbr):
    for x in range(len(numbr) - 1):
        max_ind = x
        for n in range(x + 1, len(numbr)):
            if numbr[n] > numbr[max_ind]:
                max_ind = n
        numbr[x], numbr[max_ind] = numbr[max_ind], numbr[x]

        print(' '.join([str(y) for y in numbr]), '')

    return numbr


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers

    numbers = [int(y) for y in input().split()]
    selection_sort_descend_trace(numbers)



