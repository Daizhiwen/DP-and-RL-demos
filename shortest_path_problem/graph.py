#定义节点，包括名字，可以执行的动作-执行该动作的一次cost，和所处于的level (没有用上)
class node():
    def __init__(self, name, out, cost, level):
        self.name = name
        self.action = dict(zip(out, cost))
        self.level = level

n = {}
n[1] = node(1, [2,3,4], [1, 2, 3], 0)

n[2] = node(2, [5,6], [3,4], 1)
n[3] = node(3, [6,7], [2, 1], 1)
n[4] = node(4, [7,8], [5,3], 1)

n[5] = node(5, [9], [7], 2)
n[6] = node(6, [9,10], [2,9], 2)
n[7] = node(7, [10,11], [2,1], 2)
n[8] = node(8, [11], [3], 2)

n[9] = node(9, [12], [4], 3)
n[10] = node(10, [12], [5], 3)
n[11] = node(11, [12], [2], 3)

if __name__ == "__main__":
    for s in n:
        print(s)


