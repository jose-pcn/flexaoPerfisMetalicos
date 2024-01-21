import pandas as pd

def table_steel(product):

    path = './tabelas.xlsx'
    dataFrame = pd.read_excel(path, product)

    return dataFrame

def param_perfil(product, bitola):

    dataFrame = table_steel(product)
    filtro = bitola
    dfSelecionado = dataFrame.loc[dataFrame['Bitola (mm x kg/m)'] == filtro]
    listaParam = dfSelecionado.iloc[0].to_list()

    return listaParam

def lista_bitolas(product):

    dataFrame = table_steel(product)
    listaBitolas = dataFrame['Bitola (mm x kg/m)'].to_list()

    return listaBitolas
