import os

YEAR = "2022"
DATE = "22"
NAME = "Monkey_Map"

combinationname = YEAR + "-" + DATE + NAME


os.mkdir(combinationname)
with open(combinationname+ "/"+ combinationname +".txt", "a") as ftxt:
    pass

with open(combinationname+ "/"+ combinationname +".py", "a") as fpy:
    fpy.write("with open('"+ combinationname +".txt'" +") as f:"+ "\n")
    fpy.write("    lines = f.read().splitlines()"+ "\n")
    fpy.write("    print(lines)"+ "\n")

