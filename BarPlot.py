# Crie um Barplot com o Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path,encoding="latin-1")

sns.set(style="white")
fig, ax = plt.subplots(figsize=(8,5))
colors = ["#00e600", "#ff8c1a","#a180cc"]
sns.barplot(x="fuelType", y="price",hue="gearbox", palette="husl",data=df)
ax.set_title("Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio",fontdict= {'size':12})
ax.xaxis.set_label_text("Tipo de Combustível",fontdict= {'size':14})
ax.yaxis.set_label_text("Preço Médio",fontdict= {'size':14})
plt.show()

fig.savefig("plots/Analise3/fueltype-vehicleType-price.png")