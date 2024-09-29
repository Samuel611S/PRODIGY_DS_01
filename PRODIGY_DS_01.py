import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

data = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv')


print(data.head())

country_code_column = 'Country Code'
years = list(map(str,range(1960,2023)))


country_codes = data[country_code_column].unique()

root = tk.Tk()
root.title("Population Over Time")


fig, ax = plt.subplots(figsize=(16,6))

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.get_tk_widget().pack()
current_country_index = 0

def update_chart():
    global current_country_index

    ax.clear()

    country_code = country_codes[current_country_index]

    country_data = data[data[country_code_column]== country_code]
    population_data = country_data[years].T

    population_data.columns = ['Population']
    population_data.index.name = 'Year'
    population_data['Population'] = population_data['Population'].astype(float)

    ax.bar(population_data.index, population_data['Population'], color='skyblue')
    ax.set_xlabel('Year')
    ax.set_ylabel('Population')
    ax.set_title(f'Population Distribution for Country Code: {country_code} (1960-2023)')
    ax.tick_params(axis='x', rotation=45)

    canvas.draw()

def next_country():
    global current_country_index
    current_country_index = (current_country_index + 1) % len(country_codes)  # Move to the next country
    update_chart()

# Function to go to the previous country
def previous_country():
    global current_country_index
    current_country_index = (current_country_index - 1) % len(country_codes)  # Move to the previous country
    update_chart()

# Button to go to the previous country
prev_button = tk.Button(root, text="Previous Country", command=previous_country)
prev_button.pack(side=tk.LEFT)

# Button to go to the next country
next_button = tk.Button(root, text="Next Country", command=next_country)
next_button.pack(side=tk.RIGHT)


update_chart()

root.mainloop()