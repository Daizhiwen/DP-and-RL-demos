import graph

def policy_evaluation(graph, V, epsilon, pi):
    while True:
        delta = 0
        for s in range(1, 12):
            #s: type node
            v = V[s]
            s_prime = pi[s]
            #update V[s], reward = - distance
            V[s] = - graph[s].action[s_prime] + V[s_prime]
            #print(s, V[s])
            delta = max(delta, abs(v - V[s]))
            #print(delta)

        if delta < epsilon:
            break

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

def init(graph, pi, V):
    for s in range(1, 12):
        #get a action
        #print(s)
        pi[s] = list(graph[s].action)[0]
        V[s] = 0
    V[12] = 0

def policy_iteration(graph, V, pi):
    init(graph, pi, V)
    stable = False
    while not stable:
        print(pi)
        policy_evaluation(graph, V, 0.3, pi)
        stable = policy_improve(graph, V, pi)

if __name__ == "__main__":
    G = graph.n
    #print(G[1])
    V = {}
    pi = {}
    policy_iteration(G, V, pi)

    print("final policy:\n", pi)






