# -*- coding: utf-8 -*-
import pandas as pd
for tabela in ['impressora', 'multifuncional', 'multifuncional_producao']:
      df = pd.read_excel(open('CargaDB/Planlilhao-EstruturaEDados.xlsx', 'rb'),
                  sheet_name=tabela)  
      from sqlalchemy import create_engine
      connect = create_engine('mysql+pymysql://root:secret@localhost:3306/planilhao')
      df.to_sql('planilhao_'+tabela, connect, index=False, if_exists='append')
