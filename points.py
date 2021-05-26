import numpy as np

N = 10
c = np.linspace(0, 2 * np.pi, N)
e = np.linspace(1, 10, N)
x = np.array((e, np.sin(c), np.cos(c))).T
D = np.array([[np.sum((x[i] - x[j]) ** 2) for i in range(N)] for j in range(N)])
print(x)

"""
        code to print no, x & y coordinates of cities
        use the output and save as points.txt
        """