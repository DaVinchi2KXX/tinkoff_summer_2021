dom0 = input().split(' ')
dom1 = input().split(' ')
if dom0[0] == dom1[0]:
    print(dom0[1] + ' ' + dom0[0] + ' ' + dom1[0] + ' ' + dom1[1])
elif dom0[0] == dom1[1]:
    print(dom0[1] + ' ' + dom0[0] + ' ' + dom1[1] + ' ' + dom1[0])
elif dom0[1] == dom1[1]:
    print(dom0[0] + ' ' + dom0[1] + ' ' + dom1[1] + ' ' + dom1[0])
elif dom0[1] == dom1[0]:
    print(dom0[0] + ' ' + dom0[1] + ' ' + dom1[0] + ' ' + dom1[1])
else:
    print("-1")
