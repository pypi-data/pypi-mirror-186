# from ppbank_cli.extract_docx import Doc
import requests
import coreapi
import os
import json



def get_api():
  # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://api.dev.databank.localhost/docs/")

    # Interact with the API endpoint
    action = ["detailed_molecules", "list"]
    result = client.action(schema, action)
    print(result)



def generate_meta_one(molecule_folder):
    dirname = os.path.dirname(molecule_folder)
    basename = os.path.basename(molecule_folder)
    molecule_name = basename
    datapath = dirname
    base = os.path.join(datapath, molecule_folder)

    showxyz = ''
    detailed_description = ''
    docx_description = ''
    img = ''
    simple_description = ''

    showxyzfiles = [
        os.path.join(base, 'showxyz.xyz'),
        os.path.join(base, 'default.xyz'),
        os.path.join(base, '1.xyz'),
        os.path.join(base, '01.xyz'),
        os.path.join(base, '001.xyz'),
        os.path.join(base, 'xyzfile', '1.xyz'),
        os.path.join(base, 'xyzfile', '01.xyz'),
        os.path.join(base, 'xyzfile', '001.xyz'),
    ]

    try:
        docfile_name = next(filter(lambda s: re.findall(
            r'^[^\~].*\.docx?$', s), os.listdir(base)))

    except:
        docfile_name = 'none'
    # docfile_name=molecule_name+'.docx'
    descriptionfiles = [
        os.path.join(base, docfile_name),
        os.path.join(base, 'detailed_description.txt'),
    ]

    for filename in showxyzfiles:
        if os.path.exists(filename):
            # print(filename)
            with open(filename, 'r') as f:
                showxyz = f.read()
            break

    for filename in descriptionfiles:
        if os.path.exists(filename):
            extension = os.path.basename(filename).split('.')[-1]
            if extension == 'txt':
                with open(filename) as f:
                    detailed_description = f.read()
            elif extension == 'docx':
                doc = Doc(filename)
                docx_description = doc.text
                # description = doc.markdown
                img = doc.image
                # with open(os.path.join(base,"description.txt"),'w') as f:
                #     f.write(doc.markdown)
            break

    simpledescriptionfiles = [
        os.path.join(base, 'simple_description.txt'),
    ]
    for filename in simpledescriptionfiles:
        if os.path.exists(filename):
            with open(filename) as f:
                simple_description = f.read()
            break

    metadata = {
        "molecule_name": molecule_name,
        "docx_description": docx_description,
        "detailed_description": detailed_description,
        "simple_description": simple_description,
        "showxyz": showxyz + '\n',
        "img": img,
    }

    # print(json.dumps(metadata))
    with open(os.path.join(base, '.metadata.json'), 'w') as f:
        json.dump(metadata, f)


def insert_meta_one(molecule_folder):

    dirname = os.path.dirname(molecule_folder)
    basename = os.path.basename(molecule_folder)
    molecule_name = basename
    datapath = dirname
    base = os.path.join(datapath, molecule_folder)
    # 读取 json，update 数据库
    metadate = json.load(open(os.path.join(base, '.metadata.json')))

    Molecule.objects.update_or_create(
        molecule_name=metadate['molecule_name'],
        defaults={'molecule_name': metadate['molecule_name'],
                  'detailed_description': metadate['detailed_description'],
                  'docx_description': metadate['docx_description'],
                  'simple_description': metadate['simple_description'],
                  'img': metadate['img'],
                  'showxyz': metadate['showxyz'], },

    )


def insert_one(molecule_folder):
    generate_meta_one(molecule_folder)
    insert_meta_one(molecule_folder)
    # todo: clear archive files
    # todo: clear database
    # todo: rename this function to reconstruct_db (optional)

    response = 'refresh db succeeded'
    return HttpResponse("<p>" + response + "</p>")


def insert_all(datapath):
    for molecule_folder in os.listdir(datapath):
        insert_one(molecule_folder)
