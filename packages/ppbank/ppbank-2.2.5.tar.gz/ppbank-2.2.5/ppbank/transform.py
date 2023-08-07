#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

from __future__ import print_function
import os
import re
import csv
import fnmatch

def match_file_suffix(suffix):
    for i in os.listdir():
        if i.endswith(suffix) :
           return i

dihedra_list = 'dihedra_list'
dihedra_list = match_file_suffix('dihedra_list')
uni_diha_list =  match_file_suffix('uni_diha_list')


conf_name = []
dih = []
with open(dihedra_list, 'r') as f:
    for line in f:
        # s = line.split('\t')
        s = line.split()
        conf_name.append(s[0].strip())
        # dih.append(' '.join(s[1].split(' ')[1:]).strip())
        dih.append(' '.join(s[2:]).strip())
    # print(conf_name,dih)

energy = []
with open(uni_diha_list, 'r') as f:
    for line in f:
        # s = line.split('\t')
        s = line.split()
        energy.append(s[5].strip())
    # print(energy)

# dihedra_list = 'dihedra_list'
# uni_diha_list = 'uni_diha_list'

dih_pattern = ['' for i in dih]
free_energy = ['' for i in dih]


ans = zip(conf_name, dih, dih_pattern, energy, free_energy)
# print(len(ans))
# for i in ans:
# print(i)
# cou



def write_to_csv():
    csv_filename = 'conformers.csv'
    data_file = open(csv_filename, 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for item in ans:
        if count == 0:
            # Writing headers of CSV file
            header = ['conf_name', 'dih',
                      'dih_pattern', 'energy', 'free_energy']
            csv_writer.writerow(header)
            count += 1
        # Writing data of CSV file
        # print(item)
        csv_writer.writerow(item)
    data_file.close()


if __name__ == "__main__":
    write_to_csv(ans, csv_filename)
