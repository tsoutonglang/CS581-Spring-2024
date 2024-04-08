# Tania Soutonglang
# CS 581-01 Spring 2024
# Programming 02

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename, train):
    try:
        with open(filename, newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            
            # Get the number of columns in the .csv file
            prob = {label: [0, 0] for label in csv_data.fieldnames}
            arms = tuple(prob.keys())

            # Get the number of rows in the .csv file
            num_rows = sum(1 for row in csv_data if row)
            
            # Get the number of rows in the training set
            train_size = int(train / 100 * num_rows)

            return arms, prob, train_size, num_rows          
    except FileNotFoundError:
        print("ERROR: File not found.")
        exit()

def bandit(filename, train, epsilon, threshold):
    arms, prob, train_size, file_size = load_data(filename, train)

    with open(filename, 'r') as csvfile:
        i = 0
        csv_data = csv.DictReader(csvfile)
        count = iter(csv_data)
        arm = np.random.choice(arms)
        while i <= train_size and (row := next(count, None)) is not None:
            p = np.random.random()
            if p < epsilon:         # Explore
                # Select random arm
                arm = np.random.choice(arms)
            else:                   # Exploit
                arm = max(prob, key=prob.get)

            prob[arm][0] += 1 if float(row[arm]) < threshold else 0
            prob[arm][1] += 1
            i += 1
        
        prob = [(label, round(prob[label][0]/prob[label][1], 2) if probability[0] != 0 else 0) for label, probability in prob.items()]
        prob.sort(key = lambda x:x[1], reverse = True)
        arm = prob[0][0]

        num = 0
        test_size = file_size - train_size
        while (row := next(count, None)) is not None:
            if float(row[arm]) < threshold:
                num += 1
        test_prob  = num / test_size
        
    return arms, prob, arm, test_prob

# Parse command line arguments
if (len(sys.argv) != 5):
    print('ERROR: Not enough or too many input arguments.')
    exit()

# Import .csv file data
filename = sys.argv[1]

# Epsilon parameter
epsilon_input = sys.argv[2]
try:
    # Check that the input is a float
    epsilon = float(epsilon_input)
except ValueError:
    # Set the epsilon parameter to 0.3
    epsilon = 0.3
# Check that epsilon is between 0-1
if (epsilon > 1.0 or epsilon < 0.0):
    epsilon = 0.3

# Training percentage
train_input = sys.argv[3]
try:
    # Check that the input is an integer
    train = int(train_input)
except ValueError:
    # Set the training percentage to 50%
    train = 50
# Check that percentage is between 0-50
if (train > 50 or train < 0):
    train = 50

# Success threshold
thr = float(sys.argv[4])

label, train_prob, arm, test_prob = bandit(filename, train, epsilon, thr)

# Print results
print(f"Soutonglang, Tania, A20439949 solution:")
print(f"Epsilon: {epsilon}")
print(f"Training data percentage: {train}%")
print(f"Success threshold: {thr}")
print()
print("Success probabilities:")
for probability in train_prob:
    print(f"P({probability[0]}) = {probability[1]}")
print()
print(f"Bandit {arm} was chosen to be played for the rest of data set.")
print(f"{arm} Success percentage: {test_prob}")

label2, train_prob2, arm2, test_prob2 = bandit(filename, train, epsilon, thr)
print(f"Bandit {arm2} was chosen to be played for the rest of data set.")
print(f"{arm2} Success percentage: {test_prob2}")

label3, train_prob3, arm3, test_prob3 = bandit(filename, train, epsilon, thr)
print(f"Bandit {arm3} was chosen to be played for the rest of data set.")
print(f"{arm3} Success percentage: {test_prob3}")