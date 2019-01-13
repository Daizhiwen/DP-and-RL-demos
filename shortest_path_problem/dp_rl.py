from shortest_path_problem import graph

#算法来自Sutton书Chapter3

#对当前的策略pi进行评估，得到V_pi
def policy_evaluation(graph, V, epsilon, pi):
    while True:
        delta = 0
        for s in range(1, 12):
            #s: type node
            v = V[s]
            #s': 根据当前pi在s时得到的action，在该问题中也就是下一个点
            s_prime = pi[s]
            #更新V[s], reward = - distance
            V[s] = - graph[s].action[s_prime] + V[s_prime]
            #print(s, V[s])
            delta = max(delta, abs(v - V[s]))
            #print(delta)

        if delta < epsilon:
            break

#根据当前的V_pi改进策略
def policy_improve(graph, V, pi):
    policy_stable = True
    for s in range(1, 12):
        values = {}
        old_action = pi[s]
        for s_prime, dist in graph[s].action.items():
            values[s_prime] = - dist + V[s_prime]
        pi[s] = max(values, key=values.get)
        if old_action != pi[s]:
            policy_stable = False
    return policy_stable


#初始化策略pi和价值V
def init(graph, pi, V):
    for s in range(1, 12):
        #选取能够执行的第一个action
        pi[s] = list(graph[s].action)[0]
        V[s] = 0
    V[12] = 0


#主循环函数，不断对策略进行评估和改进，直到策略稳定
def policy_iteration(graph, V, pi):
    init(graph, pi, V)
    stable = False
    while not stable:
        print("当前策略:")
        print(pi)
        policy_evaluation(graph, V, 0.3, pi)
        stable = policy_improve(graph, V, pi)

if __name__ == "__main__":
    G = graph.n
    V = {}
    pi = {}
    policy_iteration(G, V, pi)

    print("最终策略:\n", pi)
    print("V：\n", V)





