import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data = df, x ='dia', y ='venda')
  grafico.set(title='Vendas por dia', xlabel='dia', ylabel='venda')

plt.savefig('gasolina.png')