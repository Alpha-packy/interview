# 问题1: 使用 while 循环打印 1 3 5 7 9

# 问题2: 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”

l = [1,5,7,8,9]

# 问题3: 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"

#问题1:
def print_odd():
    n = 1
    while n <= 9:
        if n%2 != 0:
            print(n)
        if n == 9:
            n = 0
        n += 1

#问题2
def find_6(l):
    for i in l:
        if i == 6:
            print("found")
            return l.index(i)
    print("not found")

#问题3
def split_str(s):
    s1_temp, s2_temp = "", ""
    s1, s2 = "", ""
    #分割为s1,s2
    for i in s:
        if int(ord(i)) >= 65 and int(ord(i)) <= 122:
            if int(ord(i)) >= 65 and int(ord(i)) <= 90:
                i = chr(int(ord(i))+32)
            s1_temp = "".join((s1_temp, i))
        else:
            s2_temp = "".join((s2_temp, i))

    s1_temp = list(s1_temp)
    s2_temp = list(s2_temp)

    # 排列s1
    for i in range(len(s1_temp)):
        min_s1_idx = s1_temp.index(min(s1_temp))
        s1 = "".join((s1, s1_temp[min_s1_idx]))
        del s1_temp[min_s1_idx]
    # 排列s2
    for j in range(len(s2_temp)):
        min_s2_idx = s2_temp.index(min(s2_temp))
        s2 = "".join((s2, s2_temp[min_s2_idx]))
        del s2_temp[min_s2_idx]

    print("s1:", s1)
    print("s2:", s2)