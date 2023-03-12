import sys
import json
import csv


if len(sys.argv ) != 3:
    print( "Please give the 2 following parameters:" )
    print( "1. your txt file containing the initial data - 1 line = 1 nodeId," )
    print( "2. your mapping file nodeId -> nodeInformation." )
    exit()

# Give your initial json file containing the conflicting nodes
solutions = sys.argv[1]
file_csv = open(solutions, 'r')

# Give your initial json file containing the non conflicting nodes
mapping = sys.argv[2]
with open(mapping, 'r') as f:
    liste_mapping = json.load(f)

mappings = {}
total = 0
for mapping in liste_mapping:
    mappings[mapping['Node_id']] = mapping['valid']
    if mapping['valid'] == False:
        total = total + 1

invalid = 0
lines_csv = csv.reader(file_csv, delimiter=",")
for line_csv in lines_csv:
    if mappings[int(line_csv[0])] == False:
        invalid = invalid + 1

print(f'invalids = {invalid}, total invalid = {total}')
file_csv.close()
exit(0)
