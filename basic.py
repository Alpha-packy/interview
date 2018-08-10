# 问题一：字符串排序

s = "hello world"

# 请编写代码，将 s 以 [a-z] 顺序输出

# 问题二：数值比较

n = [9,15,23,89,33,26,2,76]

# 请编写代码，找出数组中的最大数与最小数

# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
# 通过参数输入打印出完整的句子

#问题1
def sort_s(s):
    trans_list = []
    result_list = []

    #将字符串转换成列表
    for i in s:
        trans_list.append(ord(i))
    #print(trans_list)

    #列表排序由小至大
    for i in range(len(trans_list)):
        cur_min_idx = trans_list.index(min(trans_list))
        if trans_list[cur_min_idx] >= 97 and trans_list[cur_min_idx] <= 122:
            result_list.append(trans_list[cur_min_idx])
        del trans_list[cur_min_idx]

    for i in range(len(result_list)):
        result_list[i] = chr(result_list[i])

    print("".join(result_list))

#问题2
def compare_n(n):
    min, max = n[0], n[0]
    for i in range(1, len(n)):
        if min > n[i]:
            min = n[i]
        if max < n[i]:
            max = n[i]
    print(min, max)

#问题3
import argparse
def cmd_print():
    parser = argparse.ArgumentParser(description='This is a print cmd.')
    parser.add_argument('--profession', help='show your profession')
    parser.add_argument('--location', help='show your location')
    args = parser.parse_args()
    print('i,am,a,%s,in,%s'%(args.profession, args.location))