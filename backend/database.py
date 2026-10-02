import pymysql  

def obter_conexao():
    return pymysql.connect(
        host='localhost',
        user='root', #<- PONHA SEU USUÁRIO AQUI
        password='3214', #<- PONHA SUA SENHA AQUI
        database= "Explog_db",
        cursorclass=pymysql.cursors.DictCursor)