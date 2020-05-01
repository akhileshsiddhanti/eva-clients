from flask import Blueprint, request, Response, jsonify, url_for,\
    redirect, render_template, render_template_string, session

import asyncio
query_server = Blueprint('query', __name__)

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

@query_server.route('/insert')
def odbc_insert():
    host, port = "0.0.0.0", 5432
    command =  "INSERT INTO MyVideo (Frame_ID, Frame_Path) \
        VALUES (3, '/mnt/frames/test.png');"

    result = asyncio.run(tcp_client(command,host,port))

    return result

def odbc_query(command):
    host, port = "0.0.0.0", 5432
    
    result = asyncio.run(tcp_client(command,host,port))

    return result

    
@query_server.route('/')
def odbc_server_query():
    command = request.form.get('command')

    return odbc_query(command)