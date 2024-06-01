from sqlalchemy import create_engine

# Thay các thông tin kết nối dựa vào cấu hình của máy chủ SQL Server
server = 'MSI\SQLEXPRESS'
database = 'WebApiPython'
username = 'sa'
password = 'abcd'

# Định dạng URL cho SQL Server
url = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

