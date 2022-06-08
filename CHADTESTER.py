import random

from utils.data_import import data_from_file
from utils.query import check_question
import sys

if len(sys.argv) != 2:
    print("Not enough arguments! Usage CHADTESTER.py database.")
    SystemExit()

data = data_from_file(sys.argv[1])

indices = [x for x in range(len(data))]
map = [0 for x in range(len(data))]
random.shuffle(indices)
questions = 0
correct = 0

while len(indices) > 0:
    ret = check_question(data, indices[0], (correct + 1) / (questions + 1), len(indices))
    if ret == 1:
        map[indices[0]] += 1
        correct += 1
    elif ret == -1:
        break
    # Two times correct eliminates the question
    if map[indices[0]] < 2:
        indices.insert(indices[0], random.randint(1, len(indices)))
    indices.pop(0)
    questions += 1
