"""Core functions for econ-sim"""

class world:
    """The games world object, contains all information about a game"""
    def __init__(self, name, compname):
        self.name = name
        self.player_comp = player_comp(compname)
        self.buy_price = self.buy_price()
    def __repr__(self):
        output = ''
        output += "Name: "+ self.name + '\n'
        output += self.player_comp.__repr__()
        return output

    def buy_price(self):
        purchase_price = {'Rice': 40, 'Chair': 600, 'Planks':35}
        return purchase_price

    def sell_price(self):
        sell_price = {'Rice': 30, 'Chair': 500, 'Planks': 30}

class player_comp:
    """The players company"""
    def __init__(self, name):
        self.name = name
        self.MainCorp = subcomp("main", 20000)
        self.subcomps = []
    def __repr__(self):
        output = ''
        output += "Company name:" + self.name +'\n'
        output += self.MainCorp.__repr__()
        for i in self.subcomps:
            output += self.i.__repr__()
        return output

class subcomp:
    """Subcompany"""
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.factories = []
    def __repr__(self):
        output = ''
        output += "Subcompany Name:" + self.name + '\n'
        for i in self.factories:
            output += self.i.__repr__()
        return output

class factory:
    
    def __init__(self, form):
        self.form = form
        self.prod = None
    def __repr__(self):
        output = ''
        output += "Factory: Type: {} | Production: {}".format(self.form, self.prod)
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
