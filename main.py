import csv

filename = 'data.csv'

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        continent = line['continent']
        year = line['year']
        population = line['population']
        
        print(continent)
        print(year)
        print(population)