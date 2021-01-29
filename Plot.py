# Crie um Plot com a Distribuição de Veículos com base no Ano de Registro

# Imports
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

clean_data_path = "dataset/autos.csv"
df = pd.read_csv(clean_data_path,encoding="latin-1")

sns.set(style="white")

fig, ax = plt.subplots(figsize=(8,6))
sns.distplot(df["yearOfRegistration"], color="#33cc33",kde=True, ax=ax)
ax.set_title('Distribuição de Veículos com base no Ano de Registro', fontsize= 15)
plt.ylabel("Densidade (KDE)", fontsize= 15)
plt.xlabel("Ano de Registro", fontsize= 15)
plt.show()

fig.savefig("plots/Analise1/vehicle-distribution.png")