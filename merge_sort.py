import random


def merge_sort(list):
    if len(list) > 1:

        # divide list
        divide_position = len(list) // 2
        left_list = list[:divide_position]
        right_list = list[divide_position:]
        
        merge_sort(left_list)
        merge_sort(right_list)

        left_cnt = 0
        right_cnt =0
        sorted_position =0

        # 左リストと右リストを比較して、小さい方を格納する。
        while left_cnt < len(left_list) and right_cnt < len(right_list):
            if left_list[left_cnt] < right_list[right_cnt]:
                list[sorted_position] = left_list[left_cnt]
                left_cnt +=1
            else:
                list[sorted_position] = right_list[right_cnt]
                right_cnt+=1
            sorted_position +=1

        # 残りの左リストor右リスト(ソート済み)を格納
        while left_cnt < len(left_list):
            list[sorted_position] = left_list[left_cnt]
            left_cnt +=1
            sorted_position +=1
        
        while right_cnt < len(right_list):
            list[sorted_position] = right_list[right_cnt]
            right_cnt +=1
            sorted_position +=1

list=[]
list1=[]
for _ in range(1000000):
    value = random.randrange(100000)
    list1.append(value)
    list.append(value)

list1.sort()
merge_sort(list)
# print(list)
# print(list1)

if list == list1:
    print(".sort() equal merge_sort")
