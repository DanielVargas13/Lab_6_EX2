import os.path
from os import path
import csv
import subprocess
from git import Repo

def createCsv(urls,locs):
  with open("/Lab_6_EX2/Guido/RepositoriosPythonLOC.csv", 'w', newline='') as n_file:

    fnames = [
        'URL;',
        'LOC;'
    ]

    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    csv_writer.writeheader()
    for y in range(len(urls)):
        csv_writer.writerow(
            {
                'URL;': "{};".format(urls[y]),
                'LOC;': "{};".format(locs[y])
            })

def getTotal(result):
    index = 0
    total = ""
    ch = result[index]
    while ch == " ":
        index += 1
        ch = result[index]
    while ch != " ":
        total += ch
        index += 1
        ch = result[index]
    return total

size = 25

locs = []

urls_repo = []

urls = [
    'https://github.com/python/mypy',
    'https://github.com/gvanrossum/500lines',
    'https://github.com/gvanrossum/ballot-box',
    'https://github.com/gvanrossum/asyncio',
    'https://github.com/fake-python/cpython',
    'https://github.com/gvanrossum/pyxl3',
    'https://github.com/edreamleo/make-stub-files',
    'https://github.com/ilevkivskyi/peps',
    'https://github.com/phouse512/peps',
    'https://github.com/ilevkivskyi/com2ann',
    'https://github.com/gvanrossum/pytype',
    'https://github.com/gvanrossum/arq',
    'https://github.com/emilyemorehouse/cpython',
    'https://github.com/neogeny/TatSu',
    'https://github.com/gvanrossum/mypy',
    'https://github.com/gvanrossum/mypy-dummy',
    'https://github.com/gvanrossum/pep550',
    'https://github.com/gvanrossum/welcome-wagon-2018',
    'https://github.com/gvanrossum/cpython',
    'https://github.com/gvanrossum/python-memcached',
    'https://github.com/python/mypy_extensions',
    'https://github.com/gvanrossum/stone',
    'https://github.com/neogeny/pygl',
    'https://github.com/gvanrossum/pegen',
    'https://github.com/gvanrossum/guidos_time_machine'
]

for x in range(size):
    try:
        repo_url = urls[x]
        repo_path = '/Repos/{}'.format(x)
        Repo.clone_from(repo_url, repo_path)
    except:
        print("Repositórios {} não foi clonado".format(x))
    if path.exists(repo_path):
        try:
            sbprs = subprocess.Popen("pygount {} --format=summary".format(repo_path),stdout=subprocess.PIPE)
            result = str(sbprs.stdout.read())
            results = result.split("total")
            loc = getTotal(results[1])
            locs.append(loc)
            urls_repo.append(urls[x])
            print("Repositorio {} deu bom!".format(x))
        except:
            locs.append(str(0))
            urls_repo.append(urls[x])
            print("Repositorio {} deu ruim!".format(x))
            continue

print('Repositorios clonados com sucesso')
createCsv(urls,locs)
print('Repositorios analisados com sucesso')