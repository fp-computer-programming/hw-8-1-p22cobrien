# Author: CMOB 11/29/2021


def points_scored(free, basket, three):
    points = ((three * 3) + (basket * 2) + free)
    return points


print(points_scored(1, 1, 1,) == 6)
print(points_scored(456, 4, 12,) == 500)
print(points_scored(56, 46, 13,) == 187)
