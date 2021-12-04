def depth_delta(depth):
    temp_increased = []
    temp_decreased = []
    for i,x in enumerate(depth):
        if i == 0:
            pass
        else:
            pre = depth[i-1]
            if pre < x:
                temp_increased.append(x)
            else:
                temp_decreased.append(x)
    return temp_increased, temp_decreased


#####################p1####################################
count = 0
increased = []
decreased = []
f = open("Day1\Day1.txt", "r")
depth = f.read().splitlines()
increased, decreased = depth_delta(depth)
print("Total input size {} with {} increases and {} decreases".format(len(depth), len(increased)+1, len(decreased)))

#######################p2####################################
sliding_depth = []
sliding_increased = []
sliding_decreased = []
for i,x in enumerate(depth):
    if i == len(depth)-2:
        break
    else:
        un = x
        deux = depth[i+1]
        trois = depth[i+2]
        sliding_depth.append(int(un)+int(deux)+int(trois))
sliding_increased, sliding_decreased = depth_delta(sliding_depth)
print("Total input size {} with {} increases and {} decreases".format(len(sliding_depth), len(sliding_increased), len(sliding_decreased)))
