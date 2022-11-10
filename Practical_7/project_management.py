import csv
from project import Project
from operator import attrgetter

project_list = []
with open('projects.txt', 'r', newline='') as data:
    sorter = csv.reader(data, delimiter='\t')
    data.readline()
    for data in sorter:
        project_info = Project(data[0], data[1], data[2], data[3], data[4])
        project_list.append(project_info)

project_list.sort(key=attrgetter("priority"))

for project_info in project_list:
    print(project_info)