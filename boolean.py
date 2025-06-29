def find(num1, num2, num3):
    result1 = (num1 < num2) and (num2 >= num3)
    result2 = (num1 > num2) and (num2 <= num3)
    result3 = (num3 == num1) and (num1 != num2)
    print(result1, result2, result3)
    return 0

if __name__ == '__main__':
    num1 = int(input().strip())
    num2 = int(input().strip())
    num3 = int(input().strip())
    find(num1, num2, num3)