'''
author: py chen
'''


from typing import List, Tuple


def bag(item_info:List,capacity:int):
    '''
    :param item_info: 物品的信息
    :param capacity:  背包能承受的最大重量
    :param n: 物品的個數
    :param cur_weight:当前背包的重量
    :return: 組合后得出的最大重量
    '''
    n=len(item_info)
    memo=[[-1] *(capacity+1) for i in range(n)]
    memo[0][0]=1
    max_values=[]
    # 第0次决策
    if item_info[0] <=capacity:
        memo[0][item_info[0]]=1

    # 1-4 左闭右开，表示第i次决策
    for i in range(1,n):
        for cur_weight in range(capacity+1):
            # 我们把每一层重复的状态（节点）合并，只记录不同的状态，然后基于上一层的状态集合，来推导下一层的状态集合。
            # 继承上一层的状态是为了避免重复计算，上面的状态表示除了不选i物品外的所有重量出现的情况。
            if memo[i - 1][cur_weight] != -1:
                memo[i][cur_weight] = memo[i - 1][cur_weight]
                # 通过继承上层的状态结合物品i的重量，可以推导出i物品和上层物品组合后的重量。
                if cur_weight+item_info[i] <=capacity:
                    memo[i][item_info[i] + cur_weight] = 1

    for i in range(n - 1, -1, -1):
        for w in range(capacity,-1,-1):

            if memo[i][w] != -1:
                max_values.append(w)
                break

    max_value=sorted(max_values)[-1]
    return max_value



if __name__ == '__main__':
    item_info=[2,2,4,6,3]
    capacity=9

    print(bag(item_info=item_info,capacity=capacity))





