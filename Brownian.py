import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def brownian(N, λ, v, r):
    dt = λ / v
    step = int(r**2 / λ**2)
    pos = np.zeros((N, 2, step))
    cnt = 0
    while cnt < step:
        dis = np.random.normal(scale=λ, size=(N, 2))
        pos[:, :, cnt] = pos[:, :, cnt - 1] + dis
        cnt += 1
    time = cnt * dt
    return pos, time

def plotgraph(pos, r, N, col, bin, hist):
    plt.figure(figsize=(16, 8))
    
    plt.subplot(1, 2, 1)
    for i in range(N):
        plt.plot(pos[i, 0, :], pos[i, 1, :], alpha=0.5, linewidth=0.5)
        plt.scatter(pos[i, 0, -1], pos[i, 1, -1], color=col[i], s=2) 
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.title('Brownian Motion')
    plt.axis('equal') 
    plt.subplot(1, 2, 2)
    plt.bar(bin, hist, width=(bin[1] - bin[0]), align='center', color='navy', edgecolor='grey')
    plt.xlabel('Radial distance')
    plt.ylabel('Number of particles')
    plt.title('Radial Distribution of Particles')
    plt.tight_layout()
    plt.show()

N = 500  
λ = 1e-3
v = 1 
r = 0.03
pos, time = brownian(N, λ, v, r)
col = cm.rainbow(np.linspace(0, 1, N))
dist = np.sqrt(np.sum(pos[:, :, -1] ** 2, axis=1))
hist, bine = np.histogram(dist, bins=100)
bin = (bine[1:] + bine[:-1]) / 2
plotgraph(pos, r, N, col, bin, hist)
print(f"Time taken forming a spot of {r}: {time:.4f}s")
