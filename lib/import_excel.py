import sys
import sqlite3
import pandas
import json
import requests
import datetime

#import importlib

sys.path.append('lib/')
import Py4Sqlite3 as db
import funcs
# Chỉ reload khi test trên jupyter
#importlib.reload(funcs)

conn=sqlite3.connect('mucnuoc.kt')

def check_cctl_giatri_mucnuoc(file_path):
    # Config
    colsname={
        'Trạm đo': 'maso_tramdo',
        'Mực nước (cm)': 'giatri',
        'Thời gian đo': 'thoigian'
    }
    maso_tramdo={}
    maso_tramdo=funcs.makeDict('https://github.com/soiqualang/py_import_excel/raw/master/data/tramdo.json')

    #excel_data_df = pandas.read_excel('data/mucnuoc_20rec.xlsx', sheet_name='Sheet1', usecols=['Trạm đo', 'Mực nước (cm)', 'Thời gian đo'])
    excel_data_df = pandas.read_excel(file_path, sheet_name='Sheet1', usecols=['Trạm đo', 'Mực nước (cm)', 'Thời gian đo'])

    cctl_giatri_mucnuoc=excel_data_df.to_dict(orient='records')

    errs=[]
    # Prepare data
    for index,record in enumerate(cctl_giatri_mucnuoc):
        #Do file excel mở đầu bằng tiêu đề cột và đếm từ 1
        recid=index+2
        rec=funcs.prepare_cctl_giatri_mucnuoc(record,colsname,maso_tramdo,errs,recid)
        #db.insert_table('cctl_giatri_mucnuoc',rec['fields'],rec['values'],conn)
    
    return errs