# Crie um Boxplot para avaliar os outliers

# Imports
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path,encoding="latin-1")

sns.set(style="white")

sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x="vehicleType", y="price", data=df)
ax.text(5.25,27000,"Análise de Outliers",fontsize=18,color="r",ha="center", va="center")
ax.xaxis.set_label_text("Tipo de Veículo",fontdict= {'size':14})
ax.yaxis.set_label_text("Range de Preço",fontdict= {'size':14})
plt.show()

fig.savefig("plots/Analise1/price-vehicleType-boxplot.png")