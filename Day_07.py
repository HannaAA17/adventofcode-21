from Day_0 import day_data

from collections import Counter
from statistics import median, mean

from typing import Callable, Iterable

def Day7_(craps:Counter, rng:Iterable, fun:Callable):
    
    nearest_point = None
    min_fuel_cons = None

    for pin_point in rng:
        fuel_cons = 0
        
        for crap_pos, num_of_craps in craps.items():
            fuel_cons += fun(abs(crap_pos-pin_point))*num_of_craps
            
            if (min_fuel_cons) and (fuel_cons > min_fuel_cons):
                break

        if (not min_fuel_cons) or (fuel_cons < min_fuel_cons):
            min_fuel_cons = fuel_cons
            nearest_point = pin_point
    
    return nearest_point, fuel_cons

data_in = day_data(7)
# data_in = '16,1,2,0,4,2,7,1,2,14'

data_list = [int(x) for x in data_in.split(',')]

craps = Counter(data_list)

print(
    'Part 1: (fix_point, min_gas)',
    Day7_(
        craps, 
        rng=[int(median(data_list))], 
        fun=lambda x: x
    )
)

print(
    'Part 2: (fix_point, min_gas)',
    Day7_(
        craps, 
        rng=range(min(data_list), int(mean(data_list))+1), 
        fun=lambda x: x * (x+1) // 2
    )
)
