input_num = int(input("what step do you want to find?    "))
current = 1
previous = 1
transitio_num = 0

if input_num == 0:
    current = 0
elif input_num == 1:
    current = 1
elif input_num ==2:
    current = 1
else:
    for j in range(input_num-2):
        transitio_num = current
        current += previous
        previous = transitio_num


print(current)
