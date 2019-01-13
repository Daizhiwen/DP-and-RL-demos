from maze import Maze
import numpy as np
#算法来自Sutton Chapter 6: TD (中文：时序差分)
#基本思想：用一张表Q(s,a)储存对(s,a)的评价，根据经验估计Q. 最终的策略：在处于s时，选择使得Q(s,a)最大的a.


#利用epsilon-greedy的策略选取一个action
#算法：对Q值最高的策略以1-epsilon的概率选取；其余策略均匀选取，和为epsilon
def choose_action_eplsion_greedy(Q, s, epsilon):
    Qs = []
    for i in range(4):
        Qs.append(Q[s[0], s[1], i])
    a_best = np.argmax(np.array(Qs))
    p = [0,0,0,0]
    for i in range(4):
        if i == a_best:
            p[i] = 1 - epsilon
        else:
            p[i] = epsilon/3
    #print(Qs, p)
    a = np.random.choice(np.array([0, 1, 2, 3]), p = np.array(p))
    #print(a)
    #a = 1
    return int(a)

#对一个episode进行q-learning，更新Q(s,a)函数
#算法思想：在当前状态做一次“试验”，根据试验结果来更新Q(s,a)表
def q_learning_episode(Q, maze, alpha, epsilon):
    s = (0, 0)
    while s != (2, 5):
        a = choose_action_eplsion_greedy(Q, s, epsilon)
        #得到s'和r
        s_new = Maze.take_action(maze, s, a)
        r = Maze.get_reward(s_new)
        #更新Q(s,a)
        Q_prime = max([Q[s_new[0], s_new[1], 0], Q[s_new[0], s_new[1], 1],Q[s_new[0], s_new[1], 2], Q[s_new[0], s_new[1], 3]])
        Q[s[0], s[1], a] = (1 - alpha)*Q[s[0], s[1], a] + alpha*(r + Q_prime)
        s = s_new
        #print(s)

#对一个episode进行Sarsa学习，更新Q(s,a)函数
def sarsa_episode(Q, maze, alpha, epsilon):
    s = (0, 0)
    while s != (2, 5):
        a = choose_action_eplsion_greedy(Q, s, epsilon)
        #得到s'和r
        s_new = Maze.take_action(maze, s, a)
        r = Maze.get_reward(s_new)
        #更新Q(s,a)
        a_new = choose_action_eplsion_greedy(Q, s_new, epsilon)
        Q[s[0], s[1], a] = (1 - alpha)*Q[s[0], s[1], a] + alpha*(r + Q[s_new[0], s_new[1], a_new])
        s = s_new
        #print(s)

#从Q(s,a)表中得到greedy的策略
def get_policy(Q):
    #pi = np.zeros((Q.shape[0], Q.shape[1]))
    pi = np.argmax(Q, 2)
    #print(pi.shape)
    return pi

#画出策略
def draw_policy(pi, maze):
    m = []
    for i in range(6):
        m.append([])
        for j in range(6):
            if maze[i,j] == 1:
                if pi[i,j] == 0:
                    m[i].append("U")
                elif pi[i,j] == 1:
                    m[i].append("D")
                elif pi[i,j] == 2:
                    m[i].append("L")
                else:
                    m[i].append("R")
            else:
                m[i].append("-")

    m[2][5] = "X"
    print(m[0])
    print(m[1])
    print(m[2])
    print(m[3])
    print(m[4])
    print(m[5])






if __name__ == "__main__":
    #初始化Q
    Q = np.random.randint(-10, 10, (6,6,4))
    Q[2, 5,:] = 0
    #打印迷宫
    print("迷宫：1为路径，0为障碍. 目标：以最短时间从(0,0)走到(2,5)")
    print(Maze.maze)
    print("按回车键继续...")
    input()
    #迭代学习Q(s, a)
    for i in range(10000):
        #进行一次学习 (Sarsa or Q)
        q_learning_episode(Q, Maze.maze, 0.3, 0.4)
        #根据新的Q(s,a)计算greedy策略
        pi = get_policy(Q)
        #打印策略
        print("第" + str(i+1) + "-个episode的策略:")
        draw_policy(pi, Maze.maze)




