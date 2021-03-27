def count_valid(A,B,no_of_pages):
    pages_taken = 0
    k = 1
    for i in range(0,len(A)):
        pages_taken += A[i]
        if pages_taken > no_of_pages :
            k += 1
            pages_taken = A[i]
    if k <= B:
        return True
    else:
        return False


def allocate_books(A,B):
    # A is the array ,each element represent the no of pages in the book i
    # no of Students
    total_no_of_books = len(A)
    if B > total_no_of_books :
        return -1 # invalid if student are more than no of books
    else:
        min_pages = max(A)
        max_pages = sum(A)
        res = 0
        while min_pages <= max_pages :
            mid = min_pages + (max_pages - min_pages) // 2
            if count_valid(A,B,mid) :
                res = mid
                max_pages = mid - 1
            else:
                min_pages = mid + 1

        return res


# test case
A = [12,34,67,90]
B = 2
minimum_pages = allocate_books(A,B)
print(minimum_pages)

