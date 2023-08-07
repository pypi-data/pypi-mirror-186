#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

from __future__ import print_function
# import os
# import re
from os.path import expanduser
import configparser
import requests
import os
import json
import csv
import coreapi
# import pandas as pd
import typer

app = typer.Typer()

INF = 999999999

config = configparser.ConfigParser()
home = expanduser("~")
config.read(os.path.join(home, '.ppbank/config'))

try:
    API_ADDRESS = config['global'].get(
        'API_ADDRESS', "http://api.dev.databank.localhost/")
    SHOW = config['global'].get('SHOW_ADDRESS', False)
    if SHOW == 'True':
        print(API_ADDRESS)
except:
    API_ADDRESS = "http://api.dev.databank.localhost/"


############################################

def json_to_csv(ans, csv_filename):
    data_file = open(csv_filename, 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for item in ans:
        if count == 0:
            # Writing headers of CSV file
            header = item.keys()
            csv_writer.writerow(header)
            count += 1
        # Writing data of CSV file
        csv_writer.writerow(item.values())
    data_file.close()


def parse_folder_name(molecule_folder):
    dirname = os.path.dirname(molecule_folder)
    basename = os.path.basename(molecule_folder)
    return (dirname, basename)


# @app.command()
def get_conformers_by_energy(mole_name_folder: str, energy_level: float):
    folder = os.path.exists(mole_name_folder)
    if not folder:
        os.makedirs(mole_name_folder)
    else:
        print("Folder "+mole_name_folder+" already exists, stoped")
        exit(-1)
        return "error"

    (dirname, basename) = parse_folder_name(mole_name_folder)
    payload = {'mole_name': basename, 'energy_level': energy_level}
    r = requests.get(API_ADDRESS+'/get_conformers/', params=payload)
    if r.text == 'error':
        print("molecule " + basename +
              " does not exist in database or have no matching result")
        exit(-1)
        return "error"

    ans = json.loads(r.text)

    os.makedirs(os.path.join(mole_name_folder, 'xyzfiles'))
    for i in ans:
        xyz = i.pop('xyz', None)
        open(os.path.join(mole_name_folder,
                          'xyzfiles', i['conf_name']), 'w').write(xyz)
        i.pop('id', None)

        i.pop('mole_name', None)
        i.pop('residue_num', None)
        i.pop('seq', None)
        i.pop('modification', None)

    json_to_csv(ans, os.path.join(mole_name_folder, 'conformers.csv'))


# @app.command()
def get_conformers(mole_name_folder: str):
    folder = os.path.exists(mole_name_folder)
    if not folder:
        os.makedirs(mole_name_folder)
    else:
        print("Folder "+mole_name_folder+" already exists, stoped")
        exit(-1)
        return "error"

    (dirname, basename) = parse_folder_name(mole_name_folder)
    payload = {'mole_name': basename}
    r = requests.get(API_ADDRESS+'/get_conformers/', params=payload)
    if r.text == 'error':
        print("molecule " + basename+" does not exist in database")
        exit(-1)
        return "error"

    ans = json.loads(r.text)
    xyzfile_path = os.path.join(mole_name_folder, 'xyzfiles')
    for i in ans:
        xyz = i.pop('xyz', None)
        if xyz != '' and xyz != None:
            if not os.path.exists(xyzfile_path):
                os.makedirs(xyzfile_path)
            open(os.path.join(mole_name_folder,
                              'xyzfiles', i['conf_name']), 'w').write(xyz)
        i.pop('id', None)

        i.pop('mole_name', None)
        i.pop('residue_num', None)
        i.pop('seq', None)
        i.pop('modification', None)

    json_to_csv(ans, os.path.join(mole_name_folder, 'conformers.csv'))


# @app.command()
def del_conformers(basename: str):
    payload = {'mole_name': basename}
    r = requests.get(API_ADDRESS+'/del_conformers/', params=payload)
    if r.text == 'ok':
        # print("molecule "+basename+" deleted.")
        return "ok"
    elif r.text == 'error':
        print("There is no such molecule to delete")

# @app.command()


def zip_attachment(mole_name):
    '''
    '''
    import zipfile
    import tempfile
    newname = os.path.join(mole_name,mole_name + '.zip')
    # zipdir=os.path.join(, 'archives')
    zipdir = os.path.join(mole_name)
    # if not os.path.exists(newname):
    archivefile = tempfile.mktemp(dir=zipdir)
    f = zipfile.ZipFile(archivefile, 'w', zipfile.ZIP_DEFLATED)
    # datapath = os.path.join(DATABANK_PATH, 'data')
    # with cd(datapath):
        # startdir = molecule.molecule_name
        # for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in os.listdir(mole_name):
        if filename.endswith('dihedra_list-ele') or filename.endswith('uni_diha_list-ele') \
            or filename.endswith('dihedra_list') or filename.endswith('uni_diha_list') or filename.endswith('.pdf') \
            or filename.endswith('.docx') or filename.endswith('.xlsx') :
            f.write(os.path.join(mole_name,filename))
    f.close()
    base = os.path.basename(archivefile)
    dir = os.path.dirname(archivefile)
    os.rename(archivefile, newname)
    payload={
        'file': newname,
        'type': 'application/zip'
    }
    with open(newname,'rb') as file:
        r = requests.post(API_ADDRESS+'/attachment/'+mole_name, data=file)
    # print(r.text)

    os.remove(newname)


def put_conformers(folder: str):
    mole_full_name = os.path.basename(folder).strip()
    method = mole_full_name.split('@')[1]
    mole_name = mole_full_name.split('@')[0]
    residue_num = int(mole_name.split('-')[0])
    seq = mole_name.split('-')[1]
    modification = mole_name.split('-')[2]
    conf_list = []
    file = os.path.join(folder, 'conformers.csv')
    csvfile = open(file, 'r')

    fieldnames = ('conf_name', 'dih', 'dih_pattern', 'energy', 'free_energy')
    # fieldnames = ('mole_name','residue_num','seq','modification','conf_name','dih','dih_pattern','energy', 'free_energy')

    reader = csv.DictReader(csvfile, fieldnames)
    out = [row for row in reader][1:]
    # print(out)
    for i in out:
        conf_name = i['conf_name'].strip()
        if i['energy'].strip() != '':
            energy = float(i['energy'].strip())
        else:
            energy = INF
        if i['free_energy'].strip() != '':
            free_energy = float(i['free_energy'].strip())
        else:
            free_energy = INF
        file = os.path.join(folder, 'xyzfiles', conf_name)
        conformer = {
            "mole_name": mole_full_name,
            "residue_num": residue_num,
            "seq": seq,
            "modification": modification,
            "method": method,
            "conf_name": conf_name,
            "dih": i['dih'].strip(),
            "dih_pattern": i['dih_pattern'].strip(),
            "energy": energy,
            "free_energy": free_energy,
        }
        if os.path.exists(file):
            conformer["xyz"] = open(file).read()
        # else:
            # conformer["xyz"] = ''

        conf_list.append(conformer.copy())

    payload = {
        "conf_list": conf_list,
        "file_type": "xyz",
    }

    r = requests.post(API_ADDRESS+'/put_conformers/', data=json.dumps(payload))
    if r.text == 'ok':
        zip_attachment(folder)
        return "ok"
    elif r.text == 'error':
        print("molecule "+mole_name + " already exists")
        exit(-1)
        # return "error"
    else:
        print(r.text)
        print("some error occured")
        exit(-1)



# @app.command()
def replace_conformers(folder: str):
    del_conformers(os.path.basename(folder))
    put_conformers(folder)


@app.command()
def replace(mole_folder: str):
    return replace_conformers(mole_folder)


@app.command()
def put(mole_folder: str):
    return put_conformers(mole_folder)


@app.command()
def rm(mole_name: str):
    return del_conformers(mole_name)


@app.command()
def get(mole_folder: str):
    return get_conformers(mole_folder)

def unzip(filename):
    import zipfile
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(os.path.curdir)
@app.command()
def get_att(mole_name_folder: str):
    folder = os.path.exists(mole_name_folder)
    if not folder:
        os.makedirs(mole_name_folder)
    (dirname, basename) = parse_folder_name(os.path.join(os.path.curdir,mole_name_folder))
    # (dirname, basename) = parse_folder_name(mole_name_folder)
    payload = {'mole_name': basename}


    r = requests.get(API_ADDRESS+'/get_att/', params=payload, stream=True)

    if r.text == 'error':
        print("molecule " + basename+" does not have attachments in database")
        exit(-1)
        return "error"
    os.chdir(dirname)
    # print(dirname)
    # print(basename)
    with open(basename+'.zip','wb') as f:
        f.write(r.content)

    unzip(basename+'.zip')
    os.remove(basename+'.zip')



@app.command()
def get_by_energy(mole_folder: str, energy_level: float):
    return get_conformers_by_energy(mole_folder, energy_level)


@app.command()
def ls():
  # Initialize a client & load the schema document
    # client = coreapi.Client()
    # schema = client.get(API_ADDRESS+'/docs/')

    # # Interact with the API endpoint
    # action = ["molecules", "list"]
    # result = client.action(schema, action)
    # for i in result:
    #     print(i['molecule_name'])


    # payload = {'mole_name': basename}
    r = requests.get(API_ADDRESS+'//molecules/', stream=True)

    if r.text == 'error':
        print("molecule list error")
        exit(-1)
        return "error"
    ans = json.loads(r.text)
    for i in ans:
        print(i['molecule_name'])

@app.command()
def trans(folder):
    os.chdir(folder)
    import ppbank.transform
    ppbank.transform.write_to_csv()
    if not os.path.exists('xyzfiles'):
        os.system('rm *.out')
        os.system('mkdir xyzfiles')
        os.system('mv *.xyz xyzfiles/')
    print('transformed.')

if __name__ == "__main__":
    app()


# def put_conformers_xyz(folder):
#     mole_name = os.path.basename(folder)
#     conf_list = []
#     file = os.path.join(folder, 'xyz_info.csv')
#     csvfile = open(file, 'r')
#     fieldnames = ("conf_name", "energy")
#     reader = csv.DictReader(csvfile, fieldnames)
#     out = [row for row in reader][1:]
#     # print(out)
#     for i in out:
#         conf_name = i['conf_name'].strip()
#         energy = float(i['energy'])
#         file = os.path.join(folder, 'xyzfiles', conf_name)
#         conformer = {
#             "mole_name": mole_name,
#             "residue_num": int(mole_name.split('-')[0]),
#             "seq": mole_name.split('-')[1],
#             "modification": mole_name.split('-')[2],
#             "conf_name": conf_name,
#             "dih": '',
#             "dih_pattern": '',
#             "energy": energy,
#             "free_energy": energy,
#             "xyz": open(file).read(),
#         }
#         conf_list.append(conformer.copy())

#     payload = {
#         "conf_list": conf_list,
#         "file_type": "xyz",
#     }
#     # print(json.dumps(payload))
#     r = requests.post(API_ADDRESS+'/put_conformers/', data=json.dumps(payload))
#     # print(r.text)


# def csv_to_json(file):

#     csvfile = open(file, 'r')
#     # jsonfile_obj = tempfile.NamedTemporaryFile()
#     # jsonfile = open(jsonfile_obj.name, 'w')
#     fieldnames = ("mole_name", " residue_num", " seq", " type",
#                   " conf_name", "dih", "dih_pattern", " energy", " free_energy")
#     reader = csv.DictReader(csvfile, fieldnames)
#     out = json.dumps([row for row in reader][1:])
#     # out = out[1:]
#     # print(out)
#     return out
#     # for row in reader:
#     #     json.dump(row, jsonfile)
#     #     jsonfile.write('\n')
#     # jsonfile.close()
#     # jsonfile=open(jsonfile_obj.name)
#     # print(jsonfile.read())
#     # conf_list=json.loads(jsonfile.read())
#     # return conf_list


# def csv_to_json_by_pandas(file):
#     df = pd.DataFrame(pd.read_csv(file))
#     df.to_json(r'new.json')


# def get_conformers_xyz(name, folder):
#     pass


# def get_conformers_by_energy_xyz(name, folder, energy):
#     pass


# def get_conformers_by_energy_dih(mole_name_folder, energy):
#     pass


# def get_conformers_dih(mole_name_folder):
#     (dirname, basename) = parse_folder_name(mole_name_folder)
#     payload = {'mole_name': basename}
#     r = requests.get(API_ADDRESS+'/get_conformers/', params=payload)
#     ans = json.loads(r.text)
#     json_to_csv(ans, 'test.csv')


# def put_conformers_dih(molecule_folder):
#     (dirname, basename) = parse_folder_name(molecule_folder)
#     csv_file_path = os.path.join(molecule_folder, 'conformers.csv')
#     conf_list = csv_to_json(csv_file_path)
#     payload = {
#         "conf_list": conf_list,
#         "file_type": "dih",
#     }
#     # print(json.dumps(payload))

#     r = requests.post(API_ADDRESS+'/put_conformers/', data=json.dumps(payload))

# if __name__ == "__main__":
#     TESTFILE_xyz = '/Users/lhr/@/project-databank/ppbank/apiserver/2-IG-N'
#     TESTFILE_get = '/Users/lhr/@/project-databank/ppbank/apiserver/2-IG-N'
#     TESTFILE = '/Users/lhr/@/project-databank/ppbank/apiserver/2-CC-N'

#     # put_conformers_xyz(TESTFILE_xyz)
#     # del_conformers('2-CC-N')
#     # put_conformers(TESTFILE)
#     # replace_conformers(TESTFILE)
#     # get_conformers(TESTFILE_get)
#     get_conformers_by_energy(TESTFILE_get, 2)

    # put_conformers_dih(TESTFILE)
    # get_conformers_dih(TESTFILE_get)


# 3
    # print(conf_list)
    # for row in reader:
    #     json.dump(row, jsonfile)
    #     jsonfile.write('\n')
    # jsonfile.close()
    # jsonfile=open(jsonfile_obj.name)
    # print(jsonfile.read())
    # conf_list=json.loads(jsonfile.read())
    # return conf_list
