import os


YEAR = "2024"
DATE = "01"
NAME = "Historian-Hysteria"


combinationname = YEAR + "-" + DATE + "-" + NAME


os.mkdir(YEAR + "/"+ combinationname)
with open(YEAR + "/"+ combinationname+ "/"+ combinationname +".txt", "a") as ftxt:
    pass

with open(YEAR + "/"+ combinationname+ "/"+ combinationname +".py", "a") as fpy:
    fpy.write("with open('"+ combinationname +".txt'" +") as f:"+ "\n")
    fpy.write("    lines = f.read().splitlines()"+ "\n")
    fpy.write("    print(lines)"+ "\n")


