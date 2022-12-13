# import json
#
# def recursivenested(left,right):
#     bool = None
#     for i in range(len(left)):
#         typeleft = type(left[i])
#         try:
#             typeright = type(right[i])
#         except:
#             print("right ran out")
#             bool = False
#             return bool
#
#         print(left[i], typeleft, right[i], typeright)
#         if typeleft == list and typeright == list:
#             # print(left[i], typeleft, right[i], typeright)
#             bool = recursivenested(left[i],right[i])
#             # if not bool:
#             #     return False
#
#         elif typeleft == int and typeright == list:
#             # print(left[i], typeleft, right[i], typeright)
#             bool = recursivenested([left[i]], right[i])
#             # if not bool:
#             #     return False
#
#         elif typeleft == list and typeright == int:
#             print(left[i], typeleft, right[i], typeright)
#             bool = recursivenested(left[i], [right[i]])
#             # if not bool:
#             #     return False
#
#         elif typeleft == int and typeright == int:
#             # print(left[i], typeleft, right[i], typeright)
#             if right[i] == left[i]:
#                 pass
#             elif right[i] > left[i]:
#                 print("right is bigger")
#                 bool = True
#             elif right[i] < left[i]:
#                 print("right is smoller")
#                 bool = False
#
#         if bool is not None:
#             return bool
#
#     return True
#
#     # return True
#
# def comparelists(left,right):
#     if (len(left) == 0):
#         return True
#     elif len(left) == 0:
#         return False
#     #can retun false
#     test = recursivenested(left,right)
#     if not test:
#         return False
#     #if no false
#     return True
#
#
#
#
#
# sumpairs = 0
#
# with open("1213signal.txt") as f:
#     lines = f.read().splitlines()
#     print(lines)
#     numberofpairs = (len(lines)+1)//3
#     print(numberofpairs)
#     for i in range(numberofpairs):
#         leftstr = lines[0+i*3]
#         rightstr = lines[1+i*3]
#         print(leftstr,rightstr)
#         leftlist = json.loads(leftstr)
#         rightlist = json.loads(rightstr)
#         bool = comparelists(leftlist,rightlist)
#         print(bool)
#         print("\n")
#         if bool:
#             print(i+1)
#             sumpairs += (i+1)
# print(sumpairs)

from json import loads
from functools import cmp_to_key

with open('1213signal.txt') as f:
  lines = f.read().strip().split('\n\n')

def compare(a, b):
  if isinstance(a, int):
    if isinstance(b, int):
      return a - b
    return compare([a], b)
  if isinstance(b, int):
    return compare(a, [b])
  for p, q in zip(a, b):
    c = compare(p, q)
    if c != 0:
      return c
  return len(a) - len(b)

# c = 0
# for i, line in enumerate(lines):
#   a, b = line.strip().splitlines()
#   a = loads(a)
#   b = loads(b)
#   if compare(a, b) < 0:
#     c += i + 1
# print(c)

l = [[[2]], [[6]]]

for i, line in enumerate(lines):
  a, b = line.strip().splitlines()
  l.append(loads(a))
  l.append(loads(b))

l.sort(key=cmp_to_key(compare))
r = l.index([[2]]) + 1
s = l.index([[6]]) + 1
print(r * s)