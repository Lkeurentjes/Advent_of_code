import os


YEAR = "2020"
DATE = "08"
NAME = "Handheld Halting"


combinationname = YEAR + "-" + DATE + "-" + NAME.replace(" ", "_")


os.mkdir(YEAR + "/"+ combinationname)
with open(YEAR + "/"+ combinationname+ "/"+ combinationname +".txt", "a") as ftxt:
    pass

with open(YEAR + "/"+ combinationname+ "/"+ combinationname +".py", "a") as fpy:
    fpy.write("with open('"+ combinationname +".txt'" +") as f:"+ "\n")
    fpy.write("    lines = f.read().splitlines()"+ "\n")
    fpy.write("    print(lines)"+ "\n")


