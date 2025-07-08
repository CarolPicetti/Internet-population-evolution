import csv
import matplotlib.pyplot as plt

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
        
plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400],
         label="Europe",
         marker="o")
plt.plot([2000, 2010, 2020, 2030], [200, 300, 500, 800],
         label="Asia",
         marker="o")
plt.title("Internet Population per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.grid(True)
plt.legend()

plt.show()