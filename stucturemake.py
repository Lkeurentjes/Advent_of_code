import os


YEAR = "2023"
DATE = "22"
NAME = "sand-slab"


combinationname = YEAR + "-" + DATE + "-" + NAME


os.mkdir(YEAR + "/"+ combinationname)
with open(YEAR + "/"+ combinationname+ "/"+ combinationname +".txt", "a") as ftxt:
    pass

with open(YEAR + "/"+ combinationname+ "/"+ combinationname +".py", "a") as fpy:
    fpy.write("with open('"+ combinationname +".txt'" +") as f:"+ "\n")
    fpy.write("    lines = f.read().splitlines()"+ "\n")
    fpy.write("    print(lines)"+ "\n")


