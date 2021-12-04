##########################pt1######################
f = open("Day2\Day2.txt", "r")
instructions = f.read().splitlines()
forward = []
depth = []
for i,x in enumerate(instructions):
    input, value = x.split(' ')
    if input == "forward":
        forward.append(int(value))
    else:
        if input == "up":
            depth.append(-int(value))
        else:
            depth.append(int(value))
print("original heading is {}".format(sum(forward) * sum(depth)))

##########################pt2########################
revised_forward = 0
aim = 0
revised_depth = 0
for i,x in enumerate(instructions):
    input, value = x.split(' ')
    if input == "up":
        aim += -int(value)
    elif input == "down":
        aim += int(value)
    else:
        revised_forward += int(value)
        revised_depth = revised_depth+ (aim*int(value))
print("revised heading is {}".format(revised_forward * revised_depth))