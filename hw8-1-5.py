# Author: CMOB 12/7/2021

def year_pop(origin_pop, pop_per_day):
    days = 367

    total_pop = origin_pop + (days * pop_per_day)

    return total_pop


print(year_pop(89023547, 12309) == 93540950)
print(year_pop(512478, 9340) == 3940258 )
print(year_pop(100, 1) == 467)
