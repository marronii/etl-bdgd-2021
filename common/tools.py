def normalize_types(dataframe):

    #Verificando se existe colunas com mais de um types
    [print(colname,types)
            if types > 1 else None
            for colname,types in dataframe.applymap(type).nunique().items()]