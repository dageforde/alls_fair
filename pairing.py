import json
from itertools import combinations
from datetime import datetime, timedelta

# load project json
f = open('project.json')#sys input?
project_data = json.load(f)
# for i in project_data['project']:
#     print(i)

# set variables from json
devs = project_data['project']['dev_names'] # list of developers
nsprints = project_data['project']['num_sprints'] # number of sprints
dev_pairs = [",".join(map(str, combo)) for combo in combinations(devs, 2)] # list of possible 1:1 pairing combinations; 5 devs should yield 10 pairs
project_start_date = (datetime.strptime(project_data['project']['start_date'], "%B %d, %Y")) # convert date string to datetime
sprint_days = project_data['project']['sprint_days'] # number of days in sprint
# print(dev_pairs)
# print(len(dev_pairs)) 


# function to create team rotations
rotations=list()
def Rotate(l1,num):
    for i in range(0,num):
        l1 = [l1[(i + 4) % len(l1)] for i, x in enumerate(l1)]
        rotations.append(l1)
        l1=rotations[-1]
# rotations=[] # empty list to store team rotations
Rotate(devs,nsprints)
# print(rotations[0][0:2])


# function to assign pairs, solo devs per sprint
sprint_assigns = dict() # dict of pairs & solo for each sprint
all_sprints = list()
sprint_num = 1
for r in rotations: #for every rotated team
    assn_list = list() # list to store the pair assignments
    chunk_size = 2 # chunk the list by elements of 2
    pair_count = 1
    sprint_title = 'Sprint_'+str(sprint_num)
    for i in range(0, len(r), chunk_size): # iterating by 2 over a range between 0 and team size
        pair_n = 'Pair_'+str(pair_count)
        pair_assn = r[i:i+chunk_size]
        if len(pair_assn) == 1:
            pair_dict = {'Solo':pair_assn}
        else:
            pair_dict = {pair_n:pair_assn}
        assn_list.append(pair_dict)
        pair_assn_dict = {'pairs':assn_list}
        sprint={sprint_title : pair_assn_dict,
                'start_date' : project_start_date}
        pair_count+=1 
    # sprint_pairs.append(assn_list)
    # sprint_assigns.update(sprint_title)
    all_sprints.append(sprint)
    sprint_num+=1
# sprint_dict = {'project'+n:sprint_pairs}
project_dict = {'project':all_sprints}
# print(project_dict)


# new_date = current_date + timedelta(weeks=4)

res = project_start_date + timedelta(days=7)
print(project_start_date)
print(res)

# print(chunked_list[0])
# print(sprint_pairs)
# for i in sprint_pairs:
#     print(i , sprint_pairs.count(i))


# pair_nest = {Project DICT
#               Sprints LIST :
#               'Sprint' DICT:
#                 {'pairs DICT':
#                     ['Pair_1':[a,b],'Pair_2':[c,d],'Solo':[e]]},
#                  'start_date':yyyy-mm-dd}}


# dict_keys = ['Pair_1','Pair_2','Solo']
# sprint_name = []
# paired_sprints = []#dict of sprints with pair assignments
# n=1
# for pair in sprint_pairs:
#     sprint_n = 'Sprint_'+str(n)
#     # pairs_dict = dict(zip(dict_keys, pair))
#     pairs_dict = dict.fromkeys(dict_keys, pair)
#     sprint_name.append(sprint_n)
#     sprint_n_dict = dict.fromkeys(sprint_name,pairs_dict) # dict of pairing assignments per sprint
#     # paired_sprints.append(sprint_n_dict)
#     n+=1
#     # print(pair)
#     # print(sprint_n)
# # print(sprint_pairs[0])
# # print('sprnt n dict: ',sprint_n_dict)





#figure most even distribution of pairs DONE-ISH
# assign dates to each sprint
#write to calendar 
#write to data store
#function to enter date and see pairs that day