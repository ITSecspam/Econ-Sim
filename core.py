"""Core functions for econ-sim"""
import datetime
import sys

class world:
    """The games world object, contains all information about a game"""
    def __init__(self, name, compname):
        self.name = name
        self.date = datetime.date(1950, 1, 1)
        self.player_comp = player_comp(compname)
        self.buy_price = self.buy_price()
        self.sell_price = self.sell_price()
    def __str__(self):
        return None
    def __repr__(self):
        output = '{'
        output += self.name +', '
        output += str(self.date) +', '
        output += str(self.buy_price) +', '
        output += str(self.sell_price) +', '
        output += self.player_comp.__repr__()
        output += '}'
        return output

    def buy_price(self):
        purchase_price = {'Rice': 40, 'Chair': 600, 'Planks':35}
        return purchase_price

    def sell_price(self):
        sell_price = {'Rice': 30, 'Chair': 500, 'Planks': 30}
    def tick_date(self):
        self.date += datetime.timedelta(days=7)

class player_comp:
    """The players company"""
    def __init__(self, name):
        self.name = name
        self.MainCorp = subcomp("main", 20000)
        self.subcomps = []
    def __str__(self):
        return None
    def __repr__(self):
        output = '{'
        output += self.name + ', '
        output += self.MainCorp.__repr__() + ', '
        for i in self.subcomps:
            output += self.i.__repr__() + ', '
        output += '}'
        return output

class subcomp:
    """Subcompany"""
    def __init__(self, name, cash):
        self.name = name
        self.resources = []
        for i in range(0, 1800):
            self.resources.append(0)
        #setting the cash amount
        self.resources[0] = cash
        self.factories = []
    def __str__(self):
        return None
    def __repr__(self):
        output = '{'
        output += str(self.name) + ', '
        output += str(self.resources) + ', '
        for i in self.factories:
            output += str(self.i.__repr__()) + ', '
        output += '}'
        return output

class factory:
    def __init__(self, form):
        self.form = form
        self.prod = None
        self.running = False
    def __str__(self):
        return None
    def start(self):
        self.running = True
    def stop(self):
        self.running: False
    def __repr__(self):
        output = '{'
        output += str(self.form) + ', '
        output += str(self.prod) + ', '
        output += str(self.running) + ', '

def found_subcomp(world, comp, name, cash):
    """Founds a subcompany if possible"""
    if name != "main":
        if world.comp.MainCorp.cash >= 50000 + cash:
            world.comp.subcomps.append(subcomp(name, cash))
            world.comp.MainCorp.cash -= 50000 + cash
            print("Sucessfully founded subcompany {}".format(name))
        else:
            print("Could not found subcompany as you lack the money for it")
    else:
        print("Invalid name, please use another name")

def constr_factory(world, comp, subcomp, price, form):
    """Builds a factory"""
    if world.comp.subcomp.cash >= price:
        world.comp.subcomp.factories.append(factory(form))
    else:
        print("Could not build {}. Too little cash".format(form))

def load_from_savefile(savefile):
    """Loads a save"""
    save  = open(savefile)
    saveworld = save
    save.close()
    return saveworld

def write_to_savefile(savefile, world):
    success = False
    try:
        save = open(savefile, 'w')
        save.write(world.__repr__())
        save.close()
        success = True
    except FileNotFoundError:
        print('Please specify a valid path')
        success = False
    return success

def load_prod(filepath):
    """Loads the production data"""
    prod_file = open(filepath)
    prod = prod_file
    prod_file.close()
    return prod

def SubC_Str_To_ID(subcstr, world):
    SubCID = None
    for i in range(0, len(world.player_comp.subcomps) - 1):
        if world.player_comp[i].name == subcstr:
            SubCID = i
            break
    if SubCID == None:
        print('Error: Subcompany {} not found'.format(subcstr))
        sys.exit()
    else:
        return SubCID
