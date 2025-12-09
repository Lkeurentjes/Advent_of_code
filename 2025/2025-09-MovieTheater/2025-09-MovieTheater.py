from shapely.geometry import Polygon

def area(xa,ya,xb,yb):
    return (abs(xa-xb)+1) * (abs(ya-yb)+1)

def largestArea(coords):
    largest = 0
    for i, (xa, ya) in enumerate(coords):
        for j, (xb, yb) in enumerate(coords[i+1:]):
            largest = max(area(xa,ya,xb,yb), largest)
    return largest

def largest_area_overlap(coords):
    polygon = Polygon(coords)
    #print(polygon)

    largest = 0
    for i, (xa, ya) in enumerate(coords):
        for j, (xb, yb) in enumerate(coords[i+1:]):
            if xa != xb and ya != yb:
                rectangle = Polygon([(xa,ya),(xa,yb),(xb,yb),(xb,ya)])
                # print(rectangle)
                if polygon.contains(rectangle):
                    largest = max(area(xa,ya,xb,yb), largest)
    return largest

with open('2025-09-MovieTheater.txt') as f:
    lines = [(int(line.split(",")[0]),int(line.split(",")[1])) for line in f.read().splitlines()]
    print("Part 1, the largest area you can make is",largestArea(lines))
    print("Part 2, the largest area you can make is",largest_area_overlap(lines))
