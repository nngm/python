def adder(a, b):
    carry  = 0
    
    for i in range(64):
        now_carry = carry
        carry = carry and a & 1<<i
        a ^= now_carry<<i
        carry = bool(carry or (a & 1<<i and b & 1<<i))
        a ^= b & 1<<i

    return a

if __name__ == '__main__':
    print(adder(*map(int, input().split())))
