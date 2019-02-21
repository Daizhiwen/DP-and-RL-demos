import numpy as np
#绘制一个迷宫

maze = np.zeros((6, 6))
maze[0,0] = 1
maze[0,1] = 1
maze[1,1] = 1
maze[2,1] = 1
maze[3,0] = 1
maze[3,1] = 1
maze[3,2] = 1
maze[3,3] = 1
maze[3,4] = 1
maze[3,5] = 1
maze[4,2] = 1
maze[5,2] = 1
maze[5,3] = 1
maze[5,4] = 1
maze[5,5] = 1
maze[4,5] = 1
maze[2,5] = 1
maze[0,3] = 1
maze[0,4] = 1
maze[0,5] = 1
maze[1,3] = 1
maze[2,3] = 1
#进行一次“试验”，返回新的状态
#如果走不动，就保持在原处
def take_action(maze, s, a):
    #up:
    if a == 0 and s[0] > 0 and maze[s[0] - 1, s[1]] == 1:
            s  = (s[0] - 1, s[1])
    #down:
    elif a == 1 and s[0] < 5 and maze[s[0] + 1, s[1]] == 1:
        s = (s[0] + 1, s[1])
    #left
    elif a == 2 and s[1] > 0 and maze[s[0], s[1] - 1] == 1:
        s = (s[0], s[1] - 1)
    #right
    elif a == 3 and s[1] < 5 and maze[s[0], s[1] + 1] == 1:
        s = (s[0], s[1] + 1)
    return s

#在s处得到reward
#没有到达终点：reward = -5,因为希望减少走的步数
#到达终点：给100的reward
def get_reward(s):
    if s[0] != 2 or s[1] != 5:
        return -5
    else:
        return 0

if __name__ == "__main__":
    print(maze)