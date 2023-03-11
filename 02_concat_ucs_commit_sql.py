import pandas as pd
from glob import glob
from common.base import connection_oracle
from sqlalchemy import MetaData
from sqlalchemy.types import Numeric,Float,String

def read_csv(path):

    try:
        # Cols STRING
        cols_name = \
            ['COD_ID', 'LGRD', 'PN_CON', 'DIST', 'PAC', 'CTAT', 'CTMT', 'SUB', 'CONJ',  'CEG_GD', 'BRR',
             'CEP', 'CLAS_SUB', 'CNAE', 'TIP_CC', 'FAS_CON', 'GRU_TEN', 'TEN_FORN', 'UNI_TR_AT', 'SUB',
             'GRU_TAR', 'SIT_ATIV', 'DAT_CON', 'CAR_INST', 'LIV', 'ARE_LOC', 'DESCR', 'xcoord', 'ycoord']

        return pd.read_csv(path, index_col=0,
                           encoding='latin-1',
                           dtype={col_name: str for col_name in cols_name})
    except:
        print(f'Error Read {path}')
        return None

def commit_sql(df,uc_name,types_oracle):

    #df = read_csv(path)

    df.to_sql(f'db_raw_bdgd_{uc_name}',con=connection,
              if_exists='append',
              index=False,
              chunksize=1000,
              dtype=types_oracle)

def classification_types_oracle(col):

    if ('CAR_INST' in col) or ('ENE' in col) or ('DIC' in col):
        return Float
    elif ('DEM' in col) or ('FIC' in col) or ('MUN' in col):
        return Numeric
    else:
        return String(255)

def assign_types_oracle(df):

    dict_oracle = {col : classification_types_oracle(col) for col in df.keys()}

    return dict_oracle

def verify_types():
    """
    Building
    """
    [print(col, types) for col, types in df.applymap(type).nunique().items() if types > 1]

def export_csv(df):
    df.to_csv(f'./src/database/{dict_dist.get(resp)}_tab.csv', index=False, encoding='latin-1')

#SqlAlchemy
engine = connection_oracle()
metadata = MetaData()
connection = engine.connect()

#User
resp = int(input('1-UCAT\n2-UCMT\n3-UCBT\n=>'))
dict_dist = {1: 'ucat', 2: 'ucmt', 3: 'ucbt'}
uc_name = dict_dist.get(resp)

#Concat - Unidades Consumidora
paths = [*glob(f'./src/database/csv/{uc_name}_tab/*.csv')]
df = pd.concat([read_csv(path) for path in paths])

#Assign Types Oracle
types_oracle = assign_types_oracle(df)

#Commit DB_RAW SQL
commit_sql(df,uc_name,types_oracle)
connection.commit()
connection.close()