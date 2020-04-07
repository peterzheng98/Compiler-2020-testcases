import os

testcases = [
    "sorting/bubble_sort.mx",
    "sorting/merge_sort.mx",
    "sorting/quick_sort.mx",
    "sorting/selection_sort.mx",

    "shortest_path/dijkstra.mx",
    "shortest_path/floyd.mx",
    "shortest_path/spfa.mx",

    "std/queue.mt",
]


for testcase in testcases:
    cmd = "python3 ./preprocess.py " + \
        "../codegen2/" + testcase + " > " + \
        "../codegen/" + testcase
    os.system(cmd)
