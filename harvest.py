############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []
    
    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)
  
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append( crenshaw )

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'yellow_watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

   
    return all_melon_types

#test code:
#print(make_melon_types())


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    melons = make_melon_types()
    for melon in melons:
        print(melon.pairings)

#test code:
#print_pairing_info(make_melon_types)

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melons = make_melon_types()
    dict_melon_type = {}
    for melon in melons:
        dict_melon_type[melon.code] = melon

    return dict_melon_type

#test code:
#print(make_melon_type_lookup(make_melon_types()))


    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rate, color_rate, is_field3, worker_name, field_num):
        """Initialize a melon."""
        self.melon_type = melon_type
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.is_field3 = is_field3
        self.worker_name = worker_name
        self.field_num = field_num
        
    def is_sellable(self):
        return self.shape_rate > 5 and self.color_rate > 5 and self.is_field3 == False
    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""
   
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id['yw'], 8, 7, False, 'Sheila', 2)
    melon_2 = Melon(melons_by_id['yw'], 3, 4, False, 'Sheila', 2)
    melon_3 = Melon(melons_by_id['yw'], 9, 8, True, 'Sheila', 3)
    melon_4 = Melon(melons_by_id['cas'], 10, 6, False, 'Sheila',35)
    melon_5 = Melon(melons_by_id['cren'], 8, 9, False, 'Michael', 35)
    melon_6 = Melon(melons_by_id['cren'], 8, 2, False, 'Michael', 35)
    melon_7 = Melon(melons_by_id['cren'], 2, 3, False, 'Michael', 4)
    melon_8 = Melon(melons_by_id['musk'], 6, 7, False, 'Michael', 4)
    melon_9 = Melon(melons_by_id['yw'], 7, 10, True, 'Sheila', 3)

    melons_list =[melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7,
        melon_8, melon_9]

    return melons_list

#make_melons(make_melon_types())

    # Fill in the rest

def get_sellability_report(melons):
"""Given a list of melon object, prints whether each one is sellable."""

    melon_types = make_melon_types()
    melons = make_melons(melon_types)
    for melon in melons:
        if melon.is_sellable():
            print(f'Harvested by {melon.worker_name} from Field {melon.field_num} CAN BE SOLD')
        else:
            print(f'Harvested by {melon.worker_name} from Field {melon.field_num} NOT SELLABLE')





