import os
import json

def write_results(filename, dataset):
    f = open(filename, "w+")
    json.dump(dataset, f, indent=2)
    f.close()
    print("Exported to JSON.")