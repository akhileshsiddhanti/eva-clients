from flask import Flask, jsonify, request
from flask_restful import Resource, Api 
from flask import Response

import pyodbc
import asyncio
import threading
import time

app = Flask(__name__)
api = Api(app)

@app.route('/', methods = ['GET'])
def odbc_connect():

    server = 'localhost'
    database = 'eva_catalog'
    username = 'root'
    password = 'root'

    connection = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};'+'SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM df_column')

    result = ''

    for row in cursor:
        result += str(row)
        result += " "

    return result

async def tcp_client(message, host, port):
    reader, writer = await asyncio.open_connection(
        host=host, port=port
    )

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(10000)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

    return data

@app.route('/insert', methods = ['GET'])
def odbc_insert():

    host = "0.0.0.0"
    port = 5432
    max_retry_count = 5

    sample = "INSERT INTO MyVideo (Frame_ID, Frame_Path) VALUES (3, '/mnt/frames/test.png');"
    result = asyncio.run(tcp_client(sample, host, port))

    return result

if __name__ == "__main__":

    app.run(port=8080, debug=True)

