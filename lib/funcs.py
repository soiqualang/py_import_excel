#functions by soiqualang
import sys
import sqlite3
import pandas
import json
import requests
import datetime

# Function

def makeDict(data_url):
    datadict={}
    tramdo = requests.get(data_url)
    if(tramdo.ok):
        jData = json.loads(tramdo.content)
    else:
        tramdo.raise_for_status()

    features=jData['features']
    for tramdo in features:
        datadict.update( {tramdo['properties']['ten'] : tramdo['properties']['maso']} )

    return datadict

def prepare_cctl_giatri_mucnuoc(record,colsname,maso_tramdo,errs,recid):
    fields=[]
    values=[]
    #for key, value in cctl_giatri_mucnuoc[0].items():
    #recid=3
    for key, value in record.items():
        #print(key, value)
        key=str(colsname[key])
        value=str(value)
        if(key=='maso_tramdo'):
            #value=maso_tramdo[value]
            value=get_maso(maso_tramdo,value,recid,errs)
        if(key=='thoigian'):
            value=check_date(value,recid,errs)
        if(key=='giatri'):
            value=check_val(value,recid,errs)
        
        fields.append(key)
        values.append(value)

    fields.append('maso_loaigiatri')
    values.append('TV01')

    #Thống nhất ghichu là tên file excel để có thể xóa dữ liệu về sau
    fields.append('ghichu')
    values.append('mucnuoc_20rec_haha.xlsx')

    fields.append('maso_nguoidung')
    values.append('a5213aa3f426539eee278e082816e0df')

    return {
            'fields':fields,
            'values':values
            }

## Các hàm băt lỗi
def get_maso(dict,key,rowid,errs):
    #Check maso_tramdo['Chợ Lách'] có tồn tại không
    ################################################
    if(key=='nan'):
        errs.append('Lỗi! Dòng %s không có giá trị' % (rowid))
    else:
        try:
            return dict[key]
        except:
            errs.append('Lỗi dòng %s, không tim thấy mã số của "%s"' % (rowid,key))

def check_date(datestr,rowid,errs):
    #Check date format YYYY-MM-DD
    #datetime.datetime.strptime(datestr, '%Y-%m-%d')
    ##############################
    try:
        datetime.datetime.strptime(datestr, '%Y-%m-%d')
        #print(datestr)
        return datestr
    except:
        errs.append('Lỗi dòng %s, định dạng của "%s" phải là YYYY-MM-DD' % (rowid,datestr))

def check_val(val,rowid,errs):
    #Check null
    #Check isnumber
    ###################
    #Check null
    if(val=='nan'):
        errs.append('Cảnh báo! Dòng %s không có giá trị' % (rowid))
    else:
        if(val.isnumeric()==False):
            errs.append('Lỗi dòng %s, giá trị "%s" không phải là số.' % (rowid,val))
        else:
            return val

