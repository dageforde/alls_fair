import json
from itertools import combinations

# load project json
##sys input??
f = open('project.json')#sys input?
project_data = json.load(f)
# for i in project_data['project']:
#     print(i)

# variables
devs = project_data['project']['dev_names'] # list of developers
nsprints = project_data['project']['num_sprints'] # number of sprints
dev_pairs = [",".join(map(str, combo)) for combo in combinations(devs, 2)] # list of possible 1:1 pairing combinations
# print(dev_pairs)
# print(len(dev_pairs))


# function to rotate left rotate team by 1 X Number of sprints
rotations=[] # empty list to store team rotations
def Rotate(l1,num):
    for i in range(0,num):
        l1 = [l1[(i + 4) % len(l1)] for i, x in enumerate(l1)]
        rotations.append(l1)
        l1=rotations[-1]
Rotate(devs,nsprints)
# print(rotations)

# function to define pairs, solo devs per sprint
sprint_pairs = list() # list of pairs & solo for each sprint
for r in rotations:
    chunked_list = list()
    chunk_size = 2
    for i in range(0, len(r), chunk_size):
        chunked_list.append(r[i:i+chunk_size])
    sprint_pairs.append(chunked_list)
print(sprint_pairs)
# for i in sprint_pairs:
#     print(i , sprint_pairs.count(i))


# pair_nest = {
#             'Sprint':
#                 {'pairs':
#                     {'Pair_1':[a,b],'Pair_2':[c,d],'Solo':[e]},
#                  'start_date':yyyy-mm-dd}}

# dictionary = dict(zip(keys, values))
# print(dictionary) # {'a': 1, 'b': 2, 'c': 3}
dict_keys = ['Pair_1','Pair_2','Solo']
sprint_name = []
paired_sprints = []#dict of sprints with pair assignments
n=1
for pair in sprint_pairs:
    sprint_n = 'Sprint_'+str(n)
    # pairs_dict = dict(zip(dict_keys, pair))
    pairs_dict = dict.fromkeys(dict_keys, pair)
    sprint_name.append(sprint_n)
    sprint_n_dict = dict.fromkeys(sprint_name,pairs_dict) # dict of pairing assignments per sprint
    # paired_sprints.append(sprint_n_dict)
    n+=1
    # print(pair)
    # print(sprint_n)
# print(sprint_pairs[0])
# print('sprnt n dict: ',sprint_n_dict)





#figure most even distribution of pairs DONE-ISH
# assign dates to each sprint
#write to calendar 
#write to data store
#function to enter date and see pairs that day