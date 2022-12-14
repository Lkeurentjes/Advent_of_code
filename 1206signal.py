with open("1206signal.txt") as f:
    lines = f.read().splitlines()
    print(lines)
    for i in range(len(lines[0])-14):
          print(set(lines[0][i:i+14]))
          if len(set(lines[0][i:i+14])) == 14:
              print(i+14)
              break