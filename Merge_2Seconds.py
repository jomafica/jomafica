import csv
from collections import defaultdict
import time

input_file = '-full.csv'
#input_file = '-medium.csv'
#input_file = '-short.csv'
output_file = 'output.csv'

def search_data(csv_reader, csv_writer):
    start_time = time.time()

    results = process_oportunidade(csv_reader)
    for result in results:
        csv_writer.writerow(result)

    elapsed_time = time.time() - start_time
    print(f"Took {elapsed_time} seconds.")

def process_oportunidade(csv_list) -> list:
    temp_data = defaultdict(set)
    last_row = {}
    new_clean_csv_list = []

    for row in csv_list:
        if last_row:
            if row['Oportunidade ID'] != last_row['Oportunidade ID']:
                last_row.update({'Família': temp_data['Família'],'Produto: Nome do Produto': temp_data['Produto: Nome do Produto'],'Nome do produto': temp_data['Nome do produto']})
                new_clean_csv_list.append(last_row)
                temp_data.clear()
                if row == csv_list[-1]:
                    new_clean_csv_list.append(row)
                    print(len(new_clean_csv_list))
                    return new_clean_csv_list
        temp_data['Família'].add(row['Família'])
        temp_data['Produto: Nome do Produto'].add(row['Produto: Nome do Produto'])
        temp_data['Nome do produto'].add(row['Nome do produto'])
        last_row = row.copy()

with open(input_file, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=";")
    list_of_csv = list(csv_reader)
    list_of_csv_sorted = sorted(list_of_csv, key=lambda x: x['Oportunidade ID'])

    with open(output_file, 'w', newline='') as files:
        fieldnames = ["Nome da Empresa",
                      "NIF",
                      "Segmento Empresarial",
                      "Negócio","Setor",
                      "Data de criação",
                      "Oportunidade ID",
                      "Nome da oportunidade",
                      "Fase",
                      "Duração Contrato (meses)",
                      "Proprietário da conta",
                      "Gestor Comercial",
                      "Responsável comercial da conta",
                      "Família",
                      "Produto: Nome do Produto",
                      "Nome do produto",
                      "Produto: Gama",
                      "Produto: Parceiro de Produto",
                      "Receita Total Contrato",
                      "Margem Total Contrato",
                      "Custo Total Contrato",
                      "Receita Total Produto",
                      "Margem Total Produto",
                      "Data de Ganho",
                      "Volume de negócios"]

        csv_writer = csv.DictWriter(files, fieldnames=fieldnames, delimiter=";")
        csv_writer.writeheader()
        search_data(list_of_csv_sorted, csv_writer)

