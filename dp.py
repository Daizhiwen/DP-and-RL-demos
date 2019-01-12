import graph

def dp(graph, node, J, path):
    actions = graph[node].action
    if 12 in actions:
        J[graph[node].name] = actions[12]
        path[graph[node].name] = [12]
        return
    else:
        costs = {}
        for action, dist in actions.items():
            costs[action] = dist + J[action]
            #choose the best action at current node
            best_action = min(costs, key=costs.get)

            J[node] = costs[best_action]
            print(path)

            path[node] = path[best_action].copy()
            path[node].insert(0, best_action)

def dp_loop(graph):
    J = {}
    path = {}
    for node in range(11, 0, -1):
        dp(graph, node, J, path)
        print(J)

if __name__ == "__main__":
    dp_loop(graph.n)