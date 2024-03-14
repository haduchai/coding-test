from math import factorial

def Solution(num_a, num_b):
    ''''
    Đưa về bài toán tính số cách sắp xếp khác nhau của chuỗi có độ dài x + y, ta có công thức:
                            (n)! / ((a)! * (b)!)
    '''
    total_chars = num_a + num_b
    total_combinations = factorial(total_chars) // (factorial(num_a) * factorial(num_b))
    return total_combinations

# số lượng test
N = int(input())

for i in range(N):
    # Input x, y 
    x, y = map(int, input().split())

    # Tính số cách tạo chuỗi khác nhau
    res = Solution(x, y)
    print(res)
