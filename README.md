# py_import_excel
py_import_excel

## Tạo môi trường
```cmd
pip install virtualenv
pip install xlrd
```

```python
virtualenv py_import_excel_env

python -m pip install jupyter
jupyter notebook
```

## Cấu hình VSCode

### Kích hoạt VSCode chạy môi trường ảo `virtualenv`

`
C:\Users\soiqu\AppData\Roaming\Code\User\settings.json`

```json
{
    "workbench.iconTheme": "material-icon-theme",
    "editor.fontSize": 18,
    "workbench.colorTheme": "One Dark Pro",
    "git.autofetch": true,
    "git.enableSmartCommit": true,
    "extensions.ignoreRecommendations": true,
    "python.pythonPath": "D:/sync/websvr/python/py_import_excel_env/Scripts/python.exe"
}
```

### Chạy Jupyter của môi trường ảo trong VSCode

<img src="img/h2.png">

https://code.visualstudio.com/docs/python/jupyter-support


### Jupyter reload module when run a cell

```python
import importlib

sys.path.append('lib/')
import Py4Sqlite3 as db
import funcs
importlib.reload(funcs)
```

## Check lỗi dữ liệu Excel

* Check formate date
* Check trạm đo có tồn tại hay không để lấy mã số
* Check giá trị null, là số hay không
    * null vẫn lấy để lưu vào db

### Kết quả lỗi trả về có dạng

`{'type': 'err', 'info': 'Lỗi! Dòng 17 không có giá trị'}`

> type có 3 dạng

* success: File hợp lệ, có thể import
* warning: Cảnh báo, vẫn thế thể import
* error: Lỗi, không được phép import

```json
[
  {
    "type": "success",
    "info": "File h\u1ee3p l\u1ec7."
  },
  {
    "type": "warning",
    "info": "C\u1ea3nh b\u00e1o! D\u00f2ng 2508 kh\u00f4ng c\u00f3 gi\u00e1 tr\u1ecb"
  },
  {
    "type": "error",
    "info": "L\u1ed7i d\u00f2ng 4, \u0111\u1ecbnh d\u1ea1ng c\u1ee7a \"2017-01-03 00:00:00\" ph\u1ea3i l\u00e0 YYYY-MM-DD"
  }
]
```


<img src="img/h1.png">

### Build services

> Dùng flash

```python
pip install flash
pip install flask_cors

pip install requests
```

http://localhost:5000/import/cctl_giatri_mucnuoc

> Muốn hotreload khi test thì thêm option debug

```python
if __name__ == "__main__":
	app.run(debug=True)
```


### 


## References

https://dothanhlong.org/thu-cai-geo-notebook/

https://www.journaldev.com/33306/pandas-read_excel-reading-excel-file-in-python

https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330

> Format date python

https://www.w3schools.com/python/python_datetime.asp

```python
x = datetime.datetime.now()
print(x.strftime("%d-%m-%Y_%Hh%Mm%S"))
```
