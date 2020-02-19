@echo on
D:
CALL D:\sync\websvr\python\py_import_excel_env\Scripts\activate
cd D:\sync\websvr\python\py_import_excel
CALL python service_run.py
pause