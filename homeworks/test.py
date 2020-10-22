def my_range(start, end):
    while start <= end:
        yield start
        start += 1

print(list(my_range(1,3)))



