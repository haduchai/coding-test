def minimum_gold_needed(m, d, k, c):
    # nếu vũ khí ko giết nổi 1 con quái, trả về -1
    if k > d or (k==d and m>1):
        return -1
   
    # nếu map không có quái hoặc giết quái ko giảm độ bền vũ khí, trả về 0
    if m==0 or k==0 or (d == 1 and m == 1):
        return 0

    # số quái có thể giết trước khi sửa vũ khí
    kill_pre_repair = (d-1)/k
    
    # Tính số lần cần sửa vũ khí để hết quái vật
    repair_count = m/kill_pre_repair

    # Trả về tổng số gold cần chuẩn bị
    gold_needed = int(repair_count) * c

    # kiểm tra giết quái cuối cùng ko cần sửa vũ khí có thỏa mãn
    if m%kill_pre_repair + kill_pre_repair <= d:
        gold_needed -= c
    return gold_needed

# Input
m, d, k, c = map(int, input().split())

# Output
print(minimum_gold_needed(m, d, k, c))
