import random
import time

def selection_sort(alist):
    comps = 0
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            comps += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

    return comps

def insertion_sort(alist):
    comps = 0
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            comps += 1
            alist[position] = alist[position - 1]
            position = position - 1
        if position != 0:
            comps += 1
        alist[position] = currentvalue

    return comps


def main():

    # Ascending Order List Test
    for num in [1000, 2000, 4000, 8000, 16000, 32000]:
        my_list = list(range(num))
        insertion_sort(my_list)
        start_time = time.time()
        comps = insertion_sort(my_list)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

    # for num in [1000, 2000, 4000, 8000, 16000, 32000]:
    #     random.seed(1234)
    #     randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
    #     start_time = time.time()
    #     comps = selection_sort(randoms)
    #     stop_time = time.time()
    #     print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

if __name__ == '__main__': 
    main()

