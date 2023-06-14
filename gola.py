import numpy as np
import random
import time

def initialize_array(array):
    # Set the initial configuration of the array
    # For example, following lines create a glider pattern
    array[1, 2] = 1
    array[2, 3] = 1
    array[3, 1:4] = 1

def process_step(array, next_array):
    rows, columns = array.shape
    for i in range(rows):
        for j in range(columns):
            numNeighbors = 0
            # Calculate the number of living neighbors for each cell
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if ni >= 0 and ni < rows and nj >= 0 and nj < columns:
                        numNeighbors += array[ni, nj]
            
            # Update the next_array based on the rules of the Game of Life
            if array[i, j] == 1:
                if numNeighbors < 2 or numNeighbors > 3:
                    next_array[i, j] = 0
                else:
                    next_array[i, j] = 1
            else:
                if numNeighbors == 3:
                    next_array[i, j] = 1
                else:
                    next_array[i, j] = 0

    # Copy the values from next_array back to array
    np.copyto(array, next_array)

def run_game(num_steps=100):
    for i in range(num_steps):
        print("================================================================")
        process_step(arr, next_arr)
        
        arr_out = np.where(arr == 1, "█", "  ")
        print("\n".join(''.join(row) for row in arr_out))
        time.sleep(0.5)

# Dimensions
rows = 30
columns = 60

arr = np.zeros((rows, columns))
next_arr = np.zeros((rows, columns))

initialize_array(arr)
run_game()
