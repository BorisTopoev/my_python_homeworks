sum = 0
for i in range(10, 1000000):
    number_list = list(str(i))

    reverse_list = ''.join(number_list[::-1])
    number_list = ''.join(number_list)
    if number_list == reverse_list:
        binary_list = list(bin(i))
        binary_list.pop(0)
        binary_list.pop(0)
        reverse_binary = ''.join(binary_list[::-1])
        binary_list = ''.join(binary_list)
        if binary_list == reverse_binary:
            print(i)
            print(binary_list)
            sum = sum + i
print("сумма=", sum)