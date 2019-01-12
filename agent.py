import Maze
import numpy as np

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

def q_learning_episode(Q, maze, alpha, epsilon):
    s = (0, 0)
    while s != (2, 5):
        a = choose_action_eplsion_greedy(Q, s, epsilon)
        #get s' and r
        s_new = Maze.take_action(maze, s, a)
        r = Maze.get_reward(s_new)
        #update Q(s,a) using q-learning updating formula
        Q_prime = max([Q[s_new[0], s_new[1], 0], Q[s_new[0], s_new[1], 1],Q[s_new[0], s_new[1], 2], Q[s_new[0], s_new[1], 3]])
        Q[s[0], s[1], a] = (1 - alpha)*Q[s[0], s[1], a] + alpha*(r + Q_prime)
        s = s_new
        #print(s)


def sarsa_episode(Q, maze, alpha, epsilon):
    s = (0, 0)
    while s != (2, 5):
        a = choose_action_eplsion_greedy(Q, s, epsilon)
        #get s' and r
        s_new = Maze.take_action(maze, s, a)
        r = Maze.get_reward(s_new)
        #update Q(s,a) using Sarsa updating formula
        #Q_prime = max([Q[s_new[0], s_new[1], 0], Q[s_new[0], s_new[1], 1],Q[s_new[0], s_new[1], 2], Q[s_new[0], s_new[1], 3]])
        a_new = choose_action_eplsion_greedy(Q, s_new, epsilon)
        Q[s[0], s[1], a] = (1 - alpha)*Q[s[0], s[1], a] + alpha*(r + Q[s_new[0], s_new[1], a_new])
        s = s_new
        #print(s)


def get_policy(Q):
    #pi = np.zeros((Q.shape[0], Q.shape[1]))
    pi = np.argmax(Q, 2)
    #print(pi.shape)
    return pi

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
    #initialize Q
    Q = np.random.random_integers(-10, 10, (6,6,4))
    Q[2, 5,:] = 0
    #learning Q(s, a)
    for i in range(10000):
        sarsa_episode(Q, Maze.maze, 0.3, 0.4)
        pi = get_policy(Q)
        #print(pi)
        print("the " + str(i+1) + "-th episode:")
        draw_policy(pi, Maze.maze)




