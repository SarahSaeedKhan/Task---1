def binary_gap(N):
    N = bin(N)[2:]
    print('the binary conversion N is:', N)
    zero_count = 0
    max_no_of_zeros = 0
    for k in N:
        if int(k) == 0:
            zero_count += 1
        elif int(k) == 1:
            max_no_of_zeros = max(zero_count, max_no_of_zeros)
            zero_count = 0
    print('The maximum binary gap is:', max_no_of_zeros)


N = int(input('enter a positive integer'))
binary_gap(N)
