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
            Saving and Quitting:
            sq <FILENAME> save the game to the specified file, then quit
            q quit the game without saving""")

    elif uinput == 'issc':
        if ssubc == 'main':
             print("""Name: {} \nCash: {}""".format(world.player_comp.name, world.player_comp.MainCorp.cash)) 
        else:
            ssubc_id = core.SubC_Str_To_ID(ssubc, world)
            print("""Name: {} \nCash: {}, """.format(world.player_comp.name, world.player_comp.subcomps[ssubc_id].cash))
            print('Factory Info:')
            for i in range(0, len(world.player_comp.subcomps[ssubc_id].factories) - 1):
                selected_factory = world.player_comp.subcomps[ssubc_id].factories[i]
                print('Factory {} | Type: {} | Production {} | Running {}'.format(i, i.form,i.prod , i.running))
            selected_factory.close()
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
