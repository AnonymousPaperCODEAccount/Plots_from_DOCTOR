### Before running this code, please place the pomcp binary executable to the current working directory.

import pandas as pd
import numpy as np
import time
import subprocess
import matplotlib.pyplot as plt

def run_program_from_shell_command(total_population = 89000, num_of_simulation = 2 ** 11, output_file_name = "output.csv", horizon = 30, testing_action_step = 10, R0_value = 2.0, I_ratio = 0.0056, R_ratio = 0.0051, total_testing_number = 200):
    # Shell command space.
    shell_command = "./pomcp --problem covid --outputfile {} --total_population {} --horizon {} --maximum_testing_number {} --R0_value {:.2f} --I_class_ratio {:.4f} --R_class_ratio {:.4f} " \
                    " --testing_group_number 32 --testing_action_step {} --runs 100 --mindoubles {} --maxdoubles {} --time_step 1 " \
                    "--accuracy 0.1 --verbose 0 --autoexploration false --timeout 999999 --userave false " \
                    "--ravediscount 1.0 --raveconstant 0.01 --disabletree false --exploration 1 --usetransforms true --debug_mode 1".format(
        output_file_name,
        total_population,
        horizon,
        total_testing_number,
        R0_value,
        I_ratio,
        R_ratio,
        testing_action_step,
        num_of_simulation,
        num_of_simulation
    )
    print("\n" + shell_command + "\n")
    process = subprocess.Popen(shell_command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True
                               )
    while True:
        output = process.stdout.readline()
        print(output.strip())
        stderr = process.stderr.readline()
        print(stderr.strip())

        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            # for output in process.stdout.readlines():
            #     print(output.strip())
            if return_code != 0:
                # raise RuntimeError("Shell script return code is not 0.")
                return 1
            return 0
            
            

if __name__=="__main__":

    fixed_number_of_simulation = 10
    fixed_horizon = 30
    fixed_testing_action_step = 10
    fixed_population = 89000
    fixed_R0_value = 2.0
    fixed_I_ratio = 0.00637
    fixed_R_ratio = 0.0162

    for total_testing_number in range(200, 400, 50):

        print("Running on population: {}, total_testing_number:{}, num_simulation: {}, horizon: {}, testing_action_step: {}, R0_value: {:.2f}, I_ratio: {:.4f}, R_ratio: {:.4f}.".format(
            fixed_population,
            total_testing_number,
            2**fixed_number_of_simulation,
            fixed_horizon,
            fixed_testing_action_step,
            fixed_R0_value,
            fixed_I_ratio,
            fixed_R_ratio
        ))

        output_file_name = "output_testing_number_{}.csv".format(total_testing_number)


        run_program_from_shell_command(total_population=fixed_population, num_of_simulation=fixed_number_of_simulation,
                                       output_file_name=output_file_name, horizon=fixed_horizon, testing_action_step=fixed_testing_action_step, R0_value=fixed_R0_value, I_ratio=fixed_I_ratio, R_ratio=fixed_R_ratio,
                                       total_testing_number = total_testing_number)

