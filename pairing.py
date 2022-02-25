import json
from itertools import combinations
from datetime import datetime, timedelta

# load project json
f = open('project.json')
project_data = json.load(f)
# for i in project_data['project']:
#     print(i)

# set variables from json
devs = project_data['project']['dev_names'] 
nsprints = project_data['project']['num_sprints'] 
project_start_date = project_data['project']['start_date']
sprint_days = project_data['project']['sprint_days']  
# dev_pairs = [",".join(map(str, combo)) for combo in combinations(devs, 2)] # list of possible 1:1 pairing combinations; 
# print(len(dev_pairs)) # 5 devs should yield 10 pairs

# function to create team rotations
def Rotate(l1,num):
    for i in range(0,num):
        l1 = [l1[(i + 4) % len(l1)] for i, x in enumerate(l1)]
        rotations.append(l1)
        l1=rotations[-1]
rotations=list() # empty list to store team rotations
Rotate(devs,nsprints)


# function to assign pairs, solo devs per sprint

sprint_assigns = dict() # dict of pairs & solo for each sprint
all_sprints = list() # list to store all sprint rotation schedule info
sprint_num = 1 # begin numbering sprints at 1
sprint_start_obj = datetime.strptime(project_start_date, "%B %d, %Y") # convert to datetime object for timedelta 
for r in rotations: #for every rotated team
    assn_list = list() # list to store the pair assignments
    chunk_size = 2 
    pair_count = 1
    sprint_title = 'Sprint_'+str(sprint_num)
    for i in range(0, len(r), chunk_size): # iterating by 2 over a range between 0 and team size
        pair_n = 'Pair_'+str(pair_count)
        pair_assn = r[i:i+chunk_size] #chunk team by n chunk_size; should
        if len(pair_assn) == 1: # if only one dev assigned, they are Solo
            pair_dict = {'Solo':pair_assn} 
        else:
            pair_dict = {pair_n:pair_assn}
        assn_list.append(pair_dict)
        pair_assn_dict = {'pairs':assn_list}
        sprint={sprint_title : pair_assn_dict,
                'start_date' : datetime.strftime(sprint_start_obj,"%B %d %Y"),
                'days':sprint_days}
        pair_count+=1 
    all_sprints.append(sprint)
    sprint_num+=1
    sprint_start_obj = sprint_start_obj + timedelta(days=7)
project_dict = {'project':all_sprints}


import json
import pprint
s = json.dumps(project_dict)
d = json.loads(s)
for i in range(0,len(d['project'])):
    pprint.pprint(d['project'][i])
    print('*********************')


# persist data in csv
import csv
with open('test.csv', 'w') as f:
    for i in range(0,len(d['project'])):
        f.write("%s,%s\n"%(i,d['project'][i]))