c_list  = [[i,2] for i in range(4)]
c_list.append([12,2])
c_list.sort()
pre = [c_list.pop(0)]
for i in range(len(c_list)):
    j = (i+1)%len(c_list)

