import csv
import matplotlib.pyplot as plt


def generate_population_dictionary_from_csv(filename):
    """Generate populaton diction from CSV data
    return a dictionary follow this structure:
    {
    "Africa":{population: [100,200, 300], years[2000, 2001, 2002]} """
    output = {}

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

            if continent not in output:
                output[continent] = {'population': [], 'years': []}

            output[continent]['population'].append(population)
            output[continent]['years'].append(year)
    return output


def generate_population_plots_from_dictionary(population_dictionary):
    """Generate population plots from dictionary
    one plot per continent"""
    for continent in population_dictionary:
        print(population_dictionary[continent]['years'])
        years = population_dictionary[continent]['years']
        population = population_dictionary[continent]['population']
        plt.plot(years, population, label=continent, marker="o", alpha=0.5)

    plt.title("Internet Population per Continent")
    plt.xlabel("Year")
    plt.ylabel("Internet Users (in billion Users)")
    plt.grid(True)
    plt.legend()
    plt.show()


filename = 'data.csv'

# display internet population in a plot
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)
