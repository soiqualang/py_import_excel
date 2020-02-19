# py_import_excel
py_import_excel

## Tạo môi trường

Cài `virtualenv`

```
pip install virtualenv
pip install xlrd
```

```python
virtualenv pytools

python -m pip install jupyter
jupyter notebook
```

> 
C:\Users\soiqu\AppData\Roaming\Code\User\settings.json

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

https://code.visualstudio.com/docs/python/jupyter-support

### Jupyter reload module when run a cell

```python
import importlib

sys.path.append('lib/')
import Py4Sqlite3 as db
importlib.reload(funcs)
```

### Check lỗi

<img src="img/h1.png">

### Build services




## References

https://dothanhlong.org/thu-cai-geo-notebook/

https://www.journaldev.com/33306/pandas-read_excel-reading-excel-file-in-python

https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330

