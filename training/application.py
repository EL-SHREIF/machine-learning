import python_challenge

if __name__ == '__main__':
    print("Select choice please: ")
    print("1: Read grid file and name it  'file.txt'")
    print("2: Generate random grid of size 11X40")
    choice = int(input("enter number of your Option: "))
    if choice == 1:
        sim_params = {
                "rows" : 5,
                "cols" : 10,
                "delay" : 0.1,
                "num_generations" : 2,
                "dead_cell" : " "
            }
        simulation = GOL(**sim_params)
        this_gen = []
        simulation.read_grid(this_gen)
        simulation.start_simulation(this_gen)
    elif choice == 2:
        sim_params = {
                "rows" : 22,
                "cols" : 62,
                "delay" : 0.1,
                "num_generations" : 100,
                "dead_cell" : " "
            }
        simulation = python_challenge.GOL(**sim_params)
        cur_gen = []
        simulation.init_grid(cur_gen)
        simulation.start_simulation(cur_gen)
    else:
        print("This choice is not supported")