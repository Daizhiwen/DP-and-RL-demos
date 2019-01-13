from shortest_path_problem import graph


#dp函数：对node节点进行一次规划，计算其到终点的最短距离，并保存路径
def dp(graph, node, J, path):
    #获取node可以执行的所有action
    actions = graph[node].action
    #如果是最基本的问题，直接得到J和path
    if 12 in actions:
        J[graph[node].name] = actions[12]
        path[graph[node].name] = [12]
        return
    #否则，利用更新公式计算最优的J，并记录path
    else:
        costs = {}
        for action, dist in actions.items():
            costs[action] = dist + J[action]
            #选择最优的action
            best_action = min(costs, key=costs.get)
            #得到J
            J[node] = costs[best_action]
            #print(path)
            #得到best_action的path，并在前面加入当前节点
            path[node] = path[best_action].copy()
            path[node].insert(0, best_action)

#从后往前遍历每一个点，得到所有的J和path
def dp_loop(graph):
    J = {}
    path = {}
    for node in range(11, 0, -1):
        dp(graph, node, J, path)
    #打印最终的J和path
    print("J:\n", J)
    print("策略:\n", path)

if __name__ == "__main__":
    #graph.n是路径图
    dp_loop(graph.n)