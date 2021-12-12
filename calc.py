
from math import ceil

# ======================================================

# ASSIGNMENT-1

# INFORMATION GIVEN

box_capacity = {
    'XS': 10,
    'S': 20,
    'M': 40,
    'L': 80,
    'XL': 160,
    'XXL': 320
}

delhi_costs = [('XS', 12), ('S', 23), ('M', 45),
               ('L', 77.4), ('XL', 140), ('XXL', 282)]
mumbai_costs = [('XS', 14), ('S', None), ('M', 41.3),
                ('L', 89), ('XL', 130), ('XXL', 297)]
kolkata_costs = [('XS', 11), ('S', 20), ('M', None),
                 ('L', 67), ('XL', 118), ('XXL', None)]

# =======================================================

# =======================================================

# SOLUTION

# remove boxes that cannot be used.
delhi_costs = [pair for pair in delhi_costs if pair[1] is not None]
mumbai_costs = [pair for pair in mumbai_costs if pair[1] is not None]
kolkata_costs = [pair for pair in kolkata_costs if pair[1] is not None]

# Sort box cost per unit for all regions, from the most economical to least.
for region in [delhi_costs, mumbai_costs, kolkata_costs]:
    region.sort(key=lambda x: x[1] / box_capacity[x[0]])


def calculate(total_units, duration, region_name, region_costs):
    ''' Returns miminum cost for each region.
        Params: 
            total_units (total units needed) 
            duration (Hours the boxes are needed for)
            region_name (region name)
            region_costs (array of boxes with respective costs)
    '''

    output = {
        'region': region_name,
        'total_cost': None,
        'boxes': []
    }

    total_cost = 0
    total_units = ceil(total_units / 10) * 10  # round to next tens
    for pair in region_costs:
        if total_units >= box_capacity[pair[0]]:
            units, units_left = divmod(total_units, box_capacity[pair[0]])
            output['boxes'].append((pair[0], units))
            total_cost += pair[1] * units * duration
            total_units = units_left

    output['total_cost'] = total_cost
    return output


def minimum_cost(total_units, duration):

    # Hours or total Box units cannot be 0
    if 0 in (total_units, duration):
        return None

    try:
        total_units = abs(int(total_units))
        duration = abs(int(duration))
    except ValueError:
        return 'Please enter integer values...'

    result = {'output': []}
    for region in [('Delhi', delhi_costs), ('Mumbai', mumbai_costs), ('Koltata', kolkata_costs)]:
        result['output'].append(
            calculate(total_units, duration, region[0], region[1]))
    return result


capacity = input('Enter the total units of boxes: ')
duration = input('Hours the boxes are needed for: ')

print(minimum_cost(capacity, duration))
