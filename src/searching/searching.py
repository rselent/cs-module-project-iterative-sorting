def linear_search(arr, target):
    # Your code here
    for n in range( len( arr)):
        if arr[n] == target:
            return n
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    left = 0
    right = len( arr) - 1

    print( "left", left, "\nright", right)

    while left <= right:
        mid = (left + right) // 2
        print( "\nmid", mid)

        if arr[ mid] == target:
            return mid
        
        if arr[ mid] < target:
            left = mid + 1
            print( "left", left)
        else:
            right = mid - 1
            print( "right", right)

    return -1  # not found


def main():
    #testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #testArray = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
    testArray = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

    print( binary_search( testArray, 7))
    print( linear_search( testArray, -6))


if __name__ == "__main__":
    main()