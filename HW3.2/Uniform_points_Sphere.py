import numpy as np
import numpy.random as rnd
import numpy.linalg as lin
import math
import matplotlib.pyplot as plt

list_N = [300, 3000, 30000, 300000, 3000000]
err1 = []
err2 = []

for N in list_N:

    # 1 Method: Normal Distribution
    points1 = []

    for i in range(N):
        x = rnd.normal(size=3)
        x_sphere = x * (1/lin.norm(x)) 
        points1.append(x_sphere)

    # 2 Method: Spherical coordinates method
    points2 = []

    for i in range(N):
        lon = rnd.uniform(0, 2*math.pi)
        z = rnd.uniform()
        lat = math.acos(1-2*z)
        x_sphere = [math.sin(lat)*math.cos(lon), math.sin(lat)*math.sin(lon), math.cos(lat)]
        points2.append(x_sphere)

    # Plot of 3D points
    if N == 300:
        xr = [p[0] for p in points1]
        yr = [p[1] for p in points1]
        zr = [p[2] for p in points1]

        xb = [p[0] for p in points2]
        yb = [p[1] for p in points2]
        zb = [p[2] for p in points2]

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(xr, yr, zr, c='red', label='Normal Distribution Method')
        ax.scatter(xb, yb, zb, c='blue', label='Spherical Coordinates Method')
        plt.title('Plot of 3D random points')
        plt.legend()
        plt.savefig('Points')

    # 3 Testing
    k = N//30
    C = [0 for _ in range(k)]

    z1 = [p[2] for p in points1]
    z2 = [p[2] for p in points2]

    lim = np.linspace(-1, 1, k+1)

    obs1, _ = np.histogram(z1, bins=lim)
    obs2, _ = np.histogram(z2, bins=lim)

    exp = N/k
    mse1 = (1/k) * sum((obs - exp) ** 2 for obs in obs1)
    err1.append(mse1)
    mse2 = (1/k) * sum((obs - exp) ** 2 for obs in obs2)
    err2.append(mse2)


plt.figure()
plt.plot(list_N, err1, c='red', label='Normal Distribution Method')
plt.plot(list_N, err2, c='blue', label='Spherical Coordinates Method')
plt.title('Comparison of Uniform Point Generation Methods on S²')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Sample Size N (log)')
plt.ylabel('Uniformity Error MSE (log)')
plt.savefig('Results.png')
plt.show()

