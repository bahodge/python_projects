import math
import numpy as np
import datetime


def bubble_sort(arr):
    global correction_count
    global time_to_solve
    time_to_solve = 0
    correction_count = 0
    time_started = datetime.datetime.now()
    while True:
        corrected = False
        for num in range(0, len(arr) - 1):
            if arr[num] > arr[num + 1]:
                arr[num], arr[num + 1] = arr[num + 1], arr[num]
                corrected = True
                correction_count += 1
        if not corrected:
            time_ended = datetime.datetime.now()
            time_to_solve = time_ended - time_started
            return arr


def generate_list(list_length=0):
    if list_length < 0:
        return None

    new_list = []
    for _ in range(list_length):
        new_list.append(math.floor(np.random.rand() * 100))

    return new_list


def program_stats(program_time, iteration_times, corrections):
    print("\nFINAL STATS: ")
    print("Total Program Time: " + str(program_time))
    print("Average Time To Solve: " + str(np.sum(iteration_times) / len(iteration_times)))
    print("Average Correction Count: " + str(np.sum(corrections) / len(corrections)))


def iteration_stats(iteration, time, corrections):
    print(f"Random Array: {iteration}")
    print("Number of Corrections: " + str(corrections))
    print("Time to solve: " + str(time))


def run_program(iterations=1, list_length=10):
    global time_collector
    global correction_collector
    global count

    count = 1
    time_collector = []
    correction_collector = []
    program_time_start = datetime.datetime.now()

    for _ in range(iterations):
        random_list = generate_list(list_length)
        bubble_sort(random_list)
        time_collector.append(time_to_solve)
        correction_collector.append(correction_count)
        iteration_stats(count, time_to_solve, correction_count)
        count += 1

    program_time_end = datetime.datetime.now()
    program_time = program_time_end - program_time_start
    program_stats(program_time, time_collector, correction_collector)


run_program(100, 1000)

