import csv
from radon.cli.harvest import RawHarvester
from radon.cli import Config
from pygit2 import clone_repository

def createCsv(urls,locs):
  with open("/Lab_6_EX2/RepositoriosPythonLOC.csv", 'w', newline='') as n_file:

    fnames = [
        'URL;',
        'LOC;'
    ]

    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    csv_writer.writeheader()
    for y in range(size):
        csv_writer.writerow(
            {
                'URL;': "{};".format(urls[y]),
                'LOC;': "{};".format(locs[y])
            })

size = 25

loc = 0

locs = []

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
    repo_url = urls[x]
    repo_path = '/Repos/{}'.format(x)
    repo = clone_repository(repo_url, repo_path)
    config = Config(
        exclude='',
        ignore='.*'
    )
    rad = RawHarvester([repo_path],config).results
    file = next(rad,None)
    while file != None:
        if 'loc' in file[1]:
            loc += int(file[1]["loc"])
        file = next(rad,None)
    locs.append(str(loc))
    loc = 0

print('Repositorios clonados com sucesso')
createCsv(urls,locs)
print('Repositorios analisados com sucesso')