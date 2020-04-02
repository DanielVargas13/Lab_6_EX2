import requests
import time
import csv

headers = {"Authorization": "token ######"}

initial = "null"
results = [] #vetor de resultados

def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    while (request.status_code == 502):
          time.sleep(2)
          request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query falhou! Codigo de retorno: {}. {}".format(request.status_code, query))

def createCsv(nodes):
  with open("/Lab_6_EX2/RepositoriosPython.csv", 'w', newline='') as n_file:

    fnames = [
        'Nome/Dono;',
        'URL;',
        'Linguagem Primária;',
        'Nº de Estrelas;',
        'Nº de Watchers;',
        'Nº de Forks;',
        'Nº de Releases;',
        'Data de Criação;']

    csv_writer = csv.DictWriter(n_file, fieldnames=fnames, dialect="excel-tab")
    csv_writer.writeheader()
    for node in nodes:
        csv_writer.writerow(
            {
                'Nome/Dono;': "{};".format(node['nameWithOwner']),
                'URL;': "{};".format(node['url']),
                'Linguagem Primária;': "{};".format(node['primaryLanguage']['name'] if node['primaryLanguage']!= None else 'null'),
                'Nº de Estrelas;': "{};".format(node['stargazers']['totalCount']),
                'Nº de Watchers;': "{};".format(node['watchers']['totalCount']),
                'Nº de Forks;': "{};".format(node['forkCount']),
                'Nº de Releases;': "{};".format(node['releases']['totalCount']),
                'Data de Criação;': "{};".format(node['createdAt'])
            })

for x in range(50):   
  query = """
  {
    search(query:"stars:>100 language:Python", type:REPOSITORY, first:20, after:%s){
        nodes{
          ... on Repository
          {
            nameWithOwner
            url
            primaryLanguage
            {
              name
            }
            stargazers
            {
              totalCount
            }
            watchers
            {
              totalCount
            }
            forkCount
            releases
            {
              totalCount
            }
            createdAt
          }
        }
        pageInfo
        {
          endCursor
        }
      }
  }
  """ % (initial)

  result = run_query(query)
  for y in range(20):
    results.append(result["data"]["search"]["nodes"][y])
  initial = '"{}"'.format(result["data"]["search"]["pageInfo"]["endCursor"])

print('Dados obtidos com sucesso')
createCsv(results)
print('Csv gerado com sucesso')