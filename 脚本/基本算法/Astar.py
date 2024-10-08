import heapq

# 节点类，包含当前坐标、父节点、G（起点到当前节点的代价）、H（当前节点到终点的估计代价）、F（G + H）
class 节点:
    def __init__(self, 位置, 父节点=None):
        self.位置 = 位置
        self.父节点 = 父节点
        self.g值 = 0  # 路径代价
        self.h值 = 0  # 启发式代价
        self.f值 = 0  # 总代价

    # 用于优先队列的比较
    def __lt__(self, 其他节点):
        return self.f值 < 其他节点.f值

# A*算法
def A星算法(迷宫, 起点, 终点):
    行数 = len(迷宫)      # 获取迷宫行数
    列数 = len(迷宫[0])   # 获取迷宫列数

    # 开始节点和结束节点
    起始节点 = 节点(起点)
    结束节点 = 节点(终点)

    # 待处理的节点列表（优先队列）
    开放列表 = []
    heapq.heappush(开放列表, 起始节点)
    
    # 已处理的节点集合
    关闭列表 = set()

    # 四个方向移动
    移动方向 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while 开放列表:
        # 从优先队列中取出代价最小的节点
        当前节点 = heapq.heappop(开放列表)
        关闭列表.add(当前节点.位置)

        # 找到终点，返回路径
        if 当前节点.位置 == 结束节点.位置:
            路径 = []
            while 当前节点:
                路径.append(当前节点.位置)
                当前节点 = 当前节点.父节点
            return 路径[::-1]  # 反转路径

        # 遍历当前节点的邻居节点
        for 移动 in 移动方向:
            邻居位置 = (当前节点.位置[0] + 移动[0], 当前节点.位置[1] + 移动[1])

            # 检查边界条件和障碍物
            if (0 <= 邻居位置[0] < 行数) and (0 <= 邻居位置[1] < 列数):
                if 迷宫[邻居位置[0]][邻居位置[1]] == 1 or 邻居位置 in 关闭列表:
                    continue

                # 创建邻居节点
                邻居节点 = 节点(邻居位置, 当前节点)
                
                # 计算G, H, F
                邻居节点.g值 = 当前节点.g值 + 1
                邻居节点.h值 = abs(邻居位置[0] - 结束节点.位置[0]) + abs(邻居位置[1] - 结束节点.位置[1])  # 曼哈顿距离
                邻居节点.f值 = 邻居节点.g值 + 邻居节点.h值

                # 如果节点已经在开放列表中并且有更小的f值，跳过
                if any(开放节点 for 开放节点 in 开放列表 if 邻居节点.位置 == 开放节点.位置 and 邻居节点.f值 >= 开放节点.f值):
                    continue

                # 将邻居节点添加到优先队列
                heapq.heappush(开放列表, 邻居节点)

    return None  # 没有找到路径

# 打印迷宫并标记路径
def 打印带路径的迷宫(迷宫, 路径, 起点, 终点):
    带路径迷宫 = [[str(单元格) for 单元格 in 行] for 行 in 迷宫]

    # 标记路径
    for 位置 in 路径:
        if 位置 == 起点:
            带路径迷宫[位置[0]][位置[1]] = 'S'  # 起点
        elif 位置 == 终点:
            带路径迷宫[位置[0]][位置[1]] = 'E'  # 终点
        else:
            带路径迷宫[位置[0]][位置[1]] = '.'  # 路径

    # 打印迷宫
    for 行 in 带路径迷宫:
        print(' '.join(行))

# 测试不同大小的迷宫
迷宫 = [
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0]
]

# 打印迷宫表格
for 行 in 迷宫:
    print(' '.join(str(单元格) for 单元格 in 行))

# 定义起点和终点
起点 = (0, 0)
终点 = (len(迷宫)-1, len(迷宫[0])-1)

# 运行A*算法
路径 = A星算法(迷宫, 起点, 终点)

# 输出结果
if 路径:
    print("找到路径:")
    打印带路径的迷宫(迷宫, 路径, 起点, 终点)
else:
    print("没有找到路径")
