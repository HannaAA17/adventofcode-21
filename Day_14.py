from Day_0 import day_data
from collections import Counter
from copy import deepcopy

temp, map_ = day_data(14).split('\n\n')

mapper = {
    k: v
    for k_v in map_.strip().split('\n')
    for k, v in [k_v.split(' -> ')]
}

c = Counter(map(''.join, zip(temp, temp[1:])))

for i in range(40):
    nc = {}
    for k, v in c.items():
        nc[k[0] + mapper[k]] = nc.get(k[0] + mapper[k], 0) + v
        nc[mapper[k] + k[1]] = nc.get(mapper[k] + k[1], 0) + v

    c = deepcopy(nc)

    if i not in (9, 39):
        continue

    nc = {}
    for (k1, k2), v in c.items():
        nc[k1] = nc.get(k1, 0) + v

    print((max(nc.values()) - min(nc.values()))-1)
