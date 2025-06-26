def print_pattern(n):
    char = 'A'
    for i in range(1, n + 1):
        for j in range(i):
            if j % 2 == 0:
                if i % 2 == 0:
                    print(char.lower(), end=" ")
                else:
                    print(char.upper(), end=" ")
            else:
                if i % 2 == 0:
                    print(char.upper(), end=" ")
                else:
                    print(char.lower(), end=" ")
            char = chr(ord(char) + 1)
        print()

N = 4
print_pattern(N)