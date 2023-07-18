def gen_binary(count, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            gen_binary(count + 1, n1 - 1, n2, prefix + '(')
        if count > 0 and n2 > 0:
            gen_binary(count - 1, n1, n2 - 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    prefix = ''
    gen_binary(0, n, n, prefix)
