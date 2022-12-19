with open('2022-06Signal.txt') as f:
    lines = f.read().splitlines()
    # print(lines)

#part 1
for i in range(len(lines[0])-4):
      # print(set(lines[0][i:i+14]))
      if len(set(lines[0][i:i+4])) == 4:
          print("PART 1: the marker is at",i+4)
          break

# part 2
for i in range(len(lines[0])-14):
      # print(set(lines[0][i:i+14]))
      if len(set(lines[0][i:i+14])) == 14:
          print("PART 2: the marker is at",i+14)
          break