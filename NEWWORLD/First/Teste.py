
# Fiz a instalação do Twilio = Manda Sms, OpenpyXL e Pandas = fazem a integração do Excel ao Python. 
import pandas as pd
from twilio.rest import Client
account_sid = "AC7b2e461b974b98e6a76bb093ca0d3866"
auth_token  = "297689e434c597b999b989eebd691d41"

client = Client(account_sid, auth_token)

lista_meses = ['maio', 'março', 'abril', 'fevereiro', 'janeiro']
for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
    if (tabela_vendas['Vendas'] >= 55.000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55.000, 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55.000, 'Vendas'].values[0]
        print = (f'No mês de {mes} o vendedore {Vendedor} alcancou a meta e a Dilma dobrou a meta')



