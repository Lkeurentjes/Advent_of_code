
from collections import defaultdict

with open('2022-07Storage.txt') as f:
    lines = f.read().splitlines()
    print(lines)

#
# drivesdict = {"/":[0]}
# drivessize = 0
#
#
# def recursivesize(sizes):
#     sumsize = sizes[0]
#     if sumsize <= 100000:
#         return sumsize
#     else:
#         for i in range(1,len(sizes)):
#             sumsize += recursivesize(drivesdict[sizes[i]])
#         if sumsize <= 100000:
#             return sumsize
#         else:
#             return 0
#
#
#
# with open("1207storage.txt") as f:
#     lines = f.read().splitlines()
#     print(lines)
#     dirnow = None
#     for line in lines:
#         line = line.split(" ")
#         # print(line)
#         if len(line) == 3:
#             dirnow = line[2]
#             continue
#         if line[0] == "$":
#             continue
#         try:
#             size = int(line[0])
#         except:
#             drivesdict[dirnow].append(line[1])
#             drivesdict[line[1]] = [0]
#             continue
#         drivesdict[dirnow][0] += size
#
#     print(drivesdict)
#     for sizes in drivesdict.values():
#         print(sizes)
#         print(recursivesize(sizes))
#         drivessize += recursivesize(sizes)
#         print(drivessize)
#

with open('1207storage.txt') as f:
  executions = f.read().strip().split('$ ')

tree = {}
pwd = []

for execution in executions[1:]:
  command, *output = execution.splitlines()
  program, *args = command.split(' ')
  if program == 'ls':
    for line in output:
      size, name = line.split(' ')
      if size != 'dir':
        tree[tuple(pwd) + (name,)] = int(size)
  else: # program == 'cd'
    if args[0] == '..':
      pwd.pop()
    else:
      pwd.append(args[0])

sizes = defaultdict(int)
for path, size in tree.items():
  pwd = []
  for dir in path:
    sizes[tuple(pwd)] += size
    pwd.append(dir)

print(sum([size for size in sizes.values() if size <= 100000]))

total = 70000000
needed = 30000000
taken = sizes[()]

for size in sorted(sizes.values()):
  if total - (taken - size) >= needed:
    print(size)
    break