def number_of_max(list):
max_number = 0
maximum = list[0]
for i in range(len(list)):
if list[i] > maximum:
maximum = list[i]
max_number = i
return max_number

number_of_max(A)
number_of_max(B)

A[number_of_max(A)], B[number_of_max(B)] = B[number_of_max(B)], A[number_of_max(A)]