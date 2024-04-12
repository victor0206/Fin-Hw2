liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
import math
dis = list()
path = list()
vis = [0, 0, 0, 0, 0]
res = 0
best = list()
mp = {}
mp["tokenA"] = 0
mp["tokenB"] = 1
mp["tokenC"] = 2
mp["tokenD"] = 3
mp["tokenE"] = 4
for i in range(5):
    dis.append([0, 0, 0, 0, 0])
    dis[i][i] = 1
for (a, b) in liquidity:
    c, d = liquidity[(a, b)]
    dis[mp[a]][mp[b]] = max(dis[mp[a]][mp[b]], d)
    dis[mp[b]][mp[a]] = max(dis[mp[b]][mp[a]], c)

def count(m, i, j):
    return 997 * m * dis[i][j] / (1000 * dis[j][i] + 997 * m)

def dfs(x, m, start):
    global res, best
    vis[x] = 1
    path.append(x)
    for i in range(5):
        if (count(m, x, i) > res and i == start):
            res = count(m, x, i)
            best.clear()
            for j in path:
                best.append(j)
        if (vis[i] == 0):
            dfs(i, count(m, x, i), start)
    path.pop()
    vis[x] = 0
dfs(1, 5, 1)
best.append(1)

now = 5
for i in range(len(best) - 1):
    print(now, end='->')
    now = count(now, best[i], best[i + 1])
print(now)
for i in range(len(best)):
    best[i] = "token" + chr(ord('A') + best[i])
print('->'.join(best))