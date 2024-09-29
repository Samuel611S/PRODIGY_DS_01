import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('PRODIGY_DS_01/API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv')


print(data.head())

country_code = 'EGY'
country_data = data[data['Country Code'] == country_code]


years = list(map(str,range(1960,2023)))
population_data = country_data[years].T

population_data.columns = ['Population']
population_data.index.name = 'Year'
population_data['Population'] = population_data['Population'].astype(float)


plt.figure(figsize=(10,6))
plt.bar(population_data.index,population_data['Population'],color = 'skyblue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population Distribution for Country Code: {country_code} (1960-2023)')
plt.xticks(rotation=45, fontsize=8)  # Rotate the x-axis labels to fit the years
plt.tight_layout()
plt.show()