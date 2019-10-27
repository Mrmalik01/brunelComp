def int_to_bin_string(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    if len(s) != 8:
        zeros = 8-len(s)
        for i in range(zeros):
            s = "0"+s
    return s

def bin_to_int(i):
    arr = [128, 64, 32, 16, 8, 4, 2, 1]
    sm = 0
    for index in range(8):
        if i[index] == "1":
            sm+= arr[index]
    return sm
        

test_str = "Hello worldkkk"
messArr = [int_to_bin_string(ord(ch)) for ch in test_str]
print(messArr)

coded = [chr(bin_to_int(ch)) for ch in messArr]
print(coded)

