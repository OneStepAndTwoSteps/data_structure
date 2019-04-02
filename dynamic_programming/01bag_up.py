'''
author: py chen
'''
from typing import List, Tuple

def bag_with_max_value(items_info: List[Tuple[int, int]], capacity: int) -> int:
    """
    固定容量的背包，计算能装进背包的物品组合的最大价值
    :param items_info: 物品的重量和价值
    :param capacity: 背包容量
    :return: 最大装载价值
    """
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 0
    if items_info[0][0] <= capacity:
        memo[0][items_info[0][0]] = items_info[0][1]

    for i in range(1, n):
        for cur_weight in range(capacity+1):
            memo[i][0] = 0
            if memo[i-1][cur_weight] >= 0 :
                # 这里有一个问题比较棘手，就是当物品的重量一致时，我们需要保证一致的重量取价值最大的值
                # 举个例子，我们现在有2个2kg的物品，但是价格不同，所以在决策完这两个物品之后，我们要保证决策完的这个2kg中保留的是价值最大的物品 也就是保留价值为4的物品
                # 如果物品重量一致，或者当前物品的重量等于之前物品组合的重量，我们要保证这个重量保留的是最大的价值的物品
                # 如之前组合 第0个物品和第1个物品，他的总重量为4kg，但是第2个物品的重量是4kg，并且比之前两个物品组合之后的价值还要高，我们就要保存第2个物品的价值在memo中
                if items_info[i][0] == cur_weight:
                    if items_info[i][1] > memo[i-1][cur_weight]:
                        # 现在物品的价值，比之前组合物品的价值要高，所以不继承之前组合后的最大价值
                        memo[i][cur_weight] = items_info[i][1]
                    else:
                        # 继承之前组合后的最大价值
                        memo[i][cur_weight] = memo[i - 1][cur_weight]
                    
                    # 推导其他组合的最大价值
                    if cur_weight + items_info[i][0] <= capacity:
                        memo[i][cur_weight + items_info[i][0]] = memo[i - 1][cur_weight] + items_info[i][1]

                else:
                    # 继承之前组合后的最大价值
                    memo[i][cur_weight] = memo[i - 1][cur_weight]
                    # 推导其他组合的最大价值
                    if cur_weight + items_info[i][0] <= capacity:
                        memo[i][cur_weight + items_info[i][0]] = memo[i - 1][cur_weight] + items_info[i][1]


    return max(memo[-1])




if __name__ == '__main__':

    # [(weight, value), ...]
    items_info = [(2,3),(2,4),(4,8),(6,9),(3,6)]
    capacity = 9
    print(bag_with_max_value(items_info, capacity))



