
def solution(s):
    open = ['(', '[', '{']
    close = [')', ']', '}']
    stack = []
    for c in s:
        # nếu là dấu mở, thêm vào stack
        if c in open:
            stack.append(c)
        else:
            # nếu là dấu đóng, mà stack rỗng, trả về False
            if not stack:
                return 'False'
            
            # kiểm tra xem có đúng cặp với dấu mở trước đó ko
            if open.index(stack.pop()) != close.index(c):
                return 'False'
            
    # nếu trong stack vẫn còn phần tử, trả về False
    if stack:
        return 'False'
    
    return 'True'
    
# input
N = int(input())

for i in range(N):
    # input
    s = input()
    # output
    print(solution(s))