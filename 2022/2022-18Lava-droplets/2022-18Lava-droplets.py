import numpy as np
from scipy.spatial import KDTree
import copy
import time

with open('2022-18Lava-droplets.txt') as f:
    lines = f.read().splitlines()
    number_of_cubes = len(lines)

    max, min= 0,100

    coordlist = []
    for line in lines:
        coord = []
        line = line.split(",")
        for i in range(len(line)):
            coord.append(int(line[i]))
            if int(line[i])> max:
                max = int(line[i])
            if int(line[i]) < min:
                min = int(line[i])
        coordlist.append(coord)
    npcoord = np.array(coordlist)

    # PART 1 ANSWER
    kd_tree = KDTree(npcoord)
    start_time = time.time()
    count = kd_tree.count_neighbors(kd_tree, 1)
    print("answer Part 1: ", number_of_cubes * 7 - count)
    print("count neighbour took ", time.time() - start_time, " to run")

    # start_time = time.time()
    # indexes = kd_tree.query_ball_tree(kd_tree, r=1)
    # count2 = sum([len(i) for i in indexes])
    # print("answer Part 1: ", number_of_cubes * 7 - count2)
    # print("query ball took ", time.time() - start_time, " to run")

    # # visualise point clouds
    # pcd = o3d.geometry.PointCloud()
    # pcd.points = o3d.utility.Vector3dVector(npcoord)
    # o3d.visualization.draw_geometries([pcd])

    print("\n")



    # FOR PART 2 - FILL ALL THE CAVITIES
    coordlistpart2 = copy.deepcopy(coordlist)
    max +=1
    min -=1

    # all cells
    emptygrid = []
    for i in range(min,max):
        for j in range(min,max):
            for h in range(min,max):
                if ([i, j, h]) not in coordlist:
                    emptygrid.append([i, j, h])
    emptylist = emptygrid
    emptygrid = np.array(emptygrid)
    kd_tree_empty = KDTree(emptygrid)
    connection = kd_tree_empty.query_ball_tree(kd_tree_empty,1)

    #find which are connected to the border
    indexes_to_pop = [0]
    for index in indexes_to_pop:
        for add in connection[index]:
            if add not in indexes_to_pop:
                indexes_to_pop.append(add)

    #add cavities
    for i in range(len(emptygrid)):
        if i not in indexes_to_pop:
            coordlistpart2.append(emptylist[i])
    npcoord2 = np.array((coordlistpart2))



    #PART 2 ANSWER
    number_of_cubes = len(npcoord2)
    kd_tree = KDTree(npcoord2)

    start_time = time.time()
    count = kd_tree.count_neighbors(kd_tree, 1)
    print("answer Part 2: ", number_of_cubes * 7 - count)
    print("count neighbour took ", time.time() - start_time, " to run")

    # start_time = time.time()
    # indexes = kd_tree.query_ball_tree(kd_tree, r=1)
    # count2 = sum([len(i) for i in indexes])
    # print("answer Part 2: ", number_of_cubes * 7 - count2)
    # print("query ball took ", time.time() - start_time, " to run")

    # #visualise point clouds
    # pcd = o3d.geometry.PointCloud()
    # pcd.points = o3d.utility.Vector3dVector(npcoord2)
    # o3d.visualization.draw_geometries([pcd])

    print("\n")










