#pycharm
#shiko
#python challenge

import random
import time
import os
import numpy as np
'''
    this code is part of jderobot challenges 
    I use this implementation because I see it's the most genaric one 
    start simulation : This function runs the simulation
    I use termenal to print the output in a generated box
    * equal to 1 and nothing equal to 0
    If thier is any problem with the output it may be  mis-understanding from me to the game 
    I can solve any missing area I think logic is easy 
    I don't know what to make in the tests but I try to check the otput of a txt file and it runs correctly 
'''
class GOL():
    def __init__(self, rows, cols, delay, num_generations, alive_cell="*", dead_cell="."):
        self.rows = rows
        self.cols = cols
        self.delay = delay
        self.generations = num_generations
        self.alive_cell = alive_cell
        self.dead_cell = dead_cell

    def read_grid(self, array): #Reads a given grid from a text file
        with open("file.txt", 'r') as f:
            for line in f:
                temp = []
                for i in range(len(line) - 1):
                    if line[i] == "*":
                        temp.append(1)
                    elif line[i] == ".":
                        temp.append(0)
                array += [temp]
        print(array)
        for i in range(len(array)):
            for j in range(len(array[0])):
                if (i == 0 or j == 0 or (i == len(array) - 1) or (j == len(array[0]) - 1)):
                    array[i][j] = -1

    def init_grid(self, array):
        for i in range(self.rows):
            single_row = []
            for j in range(self.cols):
                if(i == 0 or j == 0 or (i == self.rows - 1) or ( j == self.cols - 1 )):
                    single_row.append(-1)
                else:
                    ran = random.randint(0,3)
                    if ran == 0:
                        single_row.append(1)
                    else:
                        single_row.append(0)
            array.append(single_row)

    def start_simulation(self, cur_gen):
        next_gen = []
        self.init_grid(next_gen)

        for gen in range(self.generations):
            self.print_gen(cur_gen, gen)
            self.process_next_gen(cur_gen, next_gen)
            time.sleep(self.delay)

            # Swapping this generation with the next
            cur_gen, next_gen = next_gen, cur_gen
        input("Simulation finished.")

    def process_next_gen(self, cur_gen, next_gen):
        for i in range(1, self.rows-1):
            for j in range(1, self.cols-1):
                next_gen[i][j] = self.process_neighbors(i, j, cur_gen)

    def process_neighbors(self, x, y, cur_gen):
        neighbor_count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if not(i == x and j == y):
                    if cur_gen[i][j] != -1:
                        neighbor_count += cur_gen[i][j]

        if cur_gen[x][y] == 1 and neighbor_count < 2:
            return 0
        if cur_gen[x][y] == 1 and neighbor_count > 3:
            return 0
        if cur_gen[x][y] == 0 and neighbor_count == 3:
            return 1
        else:
            return cur_gen[x][y]

    def print_gen(self, cur_gen, gen):
        os.system("clear")
        print("Conway's game of life simulation. Generation : " + str(gen + 1))

        for i in range(self.rows):
            for j in range(self.cols):
                if cur_gen[i][j] == -1:
                    print("#", end =" ")
                elif cur_gen[i][j] == 1:
                    print(self.alive_cell, end= " ")
                elif cur_gen[i][j] == 0:
                    print(self.dead_cell, end= " ")
            print("\n")
