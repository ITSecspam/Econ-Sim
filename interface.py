"""Responsible for user input hanlding"""
import core
import sys

def run_interf(world):
    """Runs the interface"""
    ssubc = 'main'
    while True:
        #try:
        uinput = input("(econ-sim){}:".format(ssubc))
        ssubc = process_input(uinput, world, ssubc)
        #except KeyboardInterrupt:
            #print("To quit use sq <SAVEFILE>; or q for quitting without saving")

def process_input(uinput, world, ssubc):
    if uinput == 'help':
        print("""Econ-Sim help:
                i General company info
                issc Info about the selected subcompany
                cssc Change the selected subcompany
                step Step a week forward
            Transfers Sales and Purchases:
                transfer <RESOURCE> <AMOUNT> <FROM> <TO> to
                to <RESOURCE> <AMOUNT> <FROM> <TO> Set up a weekly transfer order between subcompanies. Use with amount 0 to delete orders
                po <RESOURCE> <AMOUNT> <FROM> <TO> Set up a weekly purchase order. Use with amount 0 to delete orders
                so <RESOURCE> <AMOUNT> <FROM> <TO> Set up a weekly sales order. Use with amount 0 to delete orders
                oi Prints information about all existing orders
            Building Management:
                constr <TYPE> Constructs a building of the speciefied type
                stop <FACTORYID> <FACTORYID_UPPER> Factoryid_upper is optional. Stops the factory with the specifeid id/ all factories in the specified range
                start <FACTORYID> <FACTORYID_UPPER> Factoryid_upper is optional. Starts the factory with the specifeid id/ all factories in the specified range
                set-prod <FACTORYID> <FACTORYID_UPPER>  Factoryid_upper is optional. Sets the production of the specified factory/range
                conv <NEW_TYPE ><FACTORYID> <FACTORYID_UPPER> Converts specified factory/range to another type
            Saving and Quitting:
                sq <FILENAME> save the game to the specified file, then quit
                q quit the game without saving""")

    elif uinput == 'issc':
        if ssubc == 'main':
            print("""Name: {} \nCash: {}""".format(world.player_comp.name, world.player_comp.MainCorp.resources[0])) 
            print("Date: {}".format(world.date))
            print('Factory Info:')
            selected_factory = None
            for i in range(0, len(world.player_comp.MainCorp.factories) - 1):
                selected_factory = world.player_comp.MainCorp.factories[i]
                print('Factory {} | Type: {} | Production {} | Running {}'.format(i, i.form,i.prod , i.running))

        else:
            ssubc_id = core.SubC_Str_To_ID(ssubc, world)
            print("""Name: {} \nCash: {}, """.format(world.player_comp.name, world.player_comp.subcomps[ssubc_id].cash))
            print("Date: {}".format(world.date))
            print('Factory Info:')
            selected_factory = None
            for i in range(0, len(world.player_comp.subcomps[ssubc_id].factories) - 1):
                selected_factory = world.player_comp.subcomps[ssubc_id].factories[i]
                print('Factory {} | Type: {} | Production {} | Running {}'.format(i, i.form,i.prod , i.running))
    elif uinput[:2] == 'sq':
        save_successful = core.write_to_savefile(uinput[3:], world)
        if save_successful:
            print("Game successfully saved")
            sys.exit()
        else:
            print("Saving failed")

    elif uinput == 'q':
        uinput2 = input('Do you really want to quit without saving[Y/N]')
        if uinput2 == 'Y' or uinput2 == 'y':
            print('QUITTING!')
            sys. exit()
        else:
            print('Aborting')
    else: 
        print('Command not recognized. For a list of all commands use help')
    return ssubc
