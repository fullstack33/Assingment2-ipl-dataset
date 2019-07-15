#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:14:32 2019

@author: nawal
"""

import matplotlib.pyplot as plt
import csv


years = []
bowlers = []
match_id = []
total_run_per_ball = []


def readcsvFile():
    
    # Read matches.csv file
    with open('matches.csv') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            years.append(row[1])
    csvFile.close()
    
    #find first and last index of year 2015
    first_index = str(years.index('2015'))
    last_index = str(years.index('2015') + years.count('2015'))
    
    # Read deliveries.csv file
    bowler_list = []
    with open('deliveries.csv') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            match_id.append(row[0])
            bowlers.append(row[8])
            total_run_per_ball.append(row[17])
    csvFile.close()
    
    #call the logic function
    logic(first_index, last_index, bowler_list)
    
    
# Create the Login of Extract useful Data  
def logic(first_index, last_index, bowler_list):
    
    # find all the indivisual bowler bowl in 2015 ipl matche
    for i in range(match_id.index(first_index), match_id.index(last_index)):
        if bowlers[i] not in bowler_list:
            bowler_list.append(bowlers[i])
    
    over_of_all = []
    runs = []
    dict_eco_bowler = {}
    #calculate the economy of all bowler , which bowl in 2015 ipl
    for b in bowler_list:
        over = 0
        run = 0
        for i in range(match_id.index(first_index), match_id.index(last_index)):
            if b == bowlers[i]:
                run += int(total_run_per_ball[i])
                if b != bowlers[i+1]:
                    over += 1
        runs.append(run)            
        over_of_all.append(over)
        dict_eco_bowler[run/over] = b
    
    # Sort the dictionary according to top economy and insert in d
    count = 0
    d = {}
    for i in sorted(dict_eco_bowler.keys(), reverse = True):
        if count<10 :
            d[dict_eco_bowler[i]] = i
            count += 1
        else:
            break
    #print(d)
    
    #call the plotgraph function
    plotgraph(d)


#plot the graph
def plotgraph(d):
    plt.bar(*zip(*d.items()), color="r")
    plt.title("Top 10 Economical Bowler of Year 2015 IPL", fontweight="bold")
    plt.xticks(rotation='90')
    plt.xlabel("Name Of Bowlers", fontweight='bold')
    plt.ylabel("Economic", fontweight="bold")


readcsvFile()