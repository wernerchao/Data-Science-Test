#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "# of data points(persons) is: ", len(enron_data)
print "# of features is ", len(enron_data["SKILLING JEFFREY K"])

poiNum = 0
for person_name in enron_data:
    if enron_data[person_name]["poi"]:
        poiNum += 1
print "# of POI is: ", poiNum