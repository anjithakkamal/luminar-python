def last_digit_max_num(n1,n2):
    n1_last_digit=n1%10
    n2_last_digit=n2%10
    return n1 if n1_last_digit>n2_last_digit else n2
print(last_digit_max_num(257,450))
