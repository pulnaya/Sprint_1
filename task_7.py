def digit_root(num):
    if num < 10:
        return num
    else:
        digit_sum = 0
        for digit in str(num):
            digit_sum += int(digit)
        return digit_root(digit_sum)