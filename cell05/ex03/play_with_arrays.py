#!/usr/bin/env python3


original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


new_array_set = {value + 2 for value in original_array if value > 5}


print(original_array)
print(new_array_set)