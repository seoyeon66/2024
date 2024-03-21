a = ['메이킷','우진','시은']
print(a[0])
print(a[1][0])

a.append(1)
print(a)
a.remove(1)
print(a)
a.insert(2, '1')
a.extend(a)
print(a)

print(a[1:3:2])
print(a[1: ])
print(a[-1:-2])
print(len(a))

a = ['메이킷','우진','시은']
print(a[0:])
print(a[0])
print(a[1])
print(a[-1])
