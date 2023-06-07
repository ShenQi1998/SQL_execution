import socket
from multiprocessing import Process
from config import configData
import detailed

#   处理客户端请求
def handle_client(client_socket , config_data , config_env , config_db):

    # try:
        request_data = client_socket.recvfrom(1024)
        request_data = request_data[0].decode('utf-8')
        print(request_data)
        line_list = request_data.split('\r\n')

        path = line_list[0]
        trancodeList = path.split(" ")
        trancode = trancodeList[1][1:]

        strData = line_list[len(line_list)-1]
        
        # jsonData = json.dumps(strData, sort_keys=True, indent=4, separators=(',', ':'))
        dictData = eval(strData)
        #业务主处理流程
        requesr_data = detailed.handle(trancode,dictData , config_data ,config_env , config_db)

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        # response_body = "<h1>Python HTTP Test</h1>"
        response_body = requesr_data
        response = response_start_line + response_headers + "\r\n" + response_body
        print("response" ,response)

        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))

    # except Exception as e :
    #     print(e)

    # finally:
        client_socket.close()



def startProcess():
    print("Server Start")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1",8000))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]connect" % client_address)
        print(configData.getEnvir() )
        handle_client_process = Process(target=handle_client, args=(client_socket, configData.getData()  ,configData.getEnvir() , configData.getDB () ))   # , kwargs=
        handle_client_process.start()
        client_socket.close()

