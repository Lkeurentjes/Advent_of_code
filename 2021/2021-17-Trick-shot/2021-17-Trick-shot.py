import numpy as np
def factorial_sum(xs):
    i = 1
    current_sum = 0
    while current_sum < xs:
        current_sum += i
        i += 1
    return i - 1

def simulate_trajectory(x_velocity, y_velocity, xs, xe, ys, ye):
    x, y = 0, 0 #start point
    highest_y = 0
    while not (y < ys or x > xe):
        x += x_velocity
        y += y_velocity
        highest_y = max(y, highest_y)
        x_velocity = max(0, x_velocity - 1)
        y_velocity -= 1

        if xs <= x <= xe and ye >= y >= ys:
            return highest_y

    # return None  # overshot

def find_highest_y_position(xs, xe, ys, ye):
    highest_y_position = 0
    count = 0

    for x_velocity in range(factorial_sum(xs), xe+1):
        for y_velocity in range(ys, 1000):  # 100 not hardcoded?
            best_y = simulate_trajectory(x_velocity, y_velocity, xs, xe, ys, ye)
            if best_y is not None:
                count += 1
                if best_y > highest_y_position:
                    highest_y_position = best_y
                    best_velocity = (x_velocity, y_velocity)

    return highest_y_position, best_velocity, count

with open('2021-17-Trick-shot.txt') as f:
    lines = f.read().replace(".", " ").replace("target area: x=", "").replace(", y=", " ").split()
    xs, xe, ys, ye = [int(l) for l in lines]

highest_y_position, best_velocity, count = find_highest_y_position(xs,xe, ys,ye)

print("Part 1: Highest Y Position:", highest_y_position, "on Velocity:", best_velocity)
print("Part 2: The total count of working velocities:", count)