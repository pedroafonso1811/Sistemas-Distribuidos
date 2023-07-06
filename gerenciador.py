import socket
import requests
import json


server_ip = '127.0.0.1'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))
    
    server_socket.listen(1)
    print("Servidor pronto para receber conexões.")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com:", client_address)
        
        # Função para coletar dados dos sensores de bueiros
        def coletar_dados_sensores():
            dados = {
                'nivel_agua': 0.75,
                'qualidade_agua': 'Boa',
                'fluxo': 'Normal'                
            }
            return dados
        
        # Função para enviar os dados para a nuvem
        def enviar_dados_nuvem(dados):
            url = 'https://api.exemplo.com/enviar_dados'
            headers = {'Content-Type': 'application/json'}
            resposta = requests.post(url, headers=headers, data=json.dumps(dados))
            if resposta.status_code == 200:
                print("Dados enviados para a nuvem com sucesso!")
            else:
                print("Erro ao enviar dados para a nuvem.")
                
        # Função para processar os dados e tomar ações adequadas
        def processar_dados(dados):
            if dados['nivel_agua'] > 0.9:
                print("Risco de enchente! Acionando alerta para a equipe de manutenção.")
                
        # Função principal para executar o sistema de gerenciamento de bueiros
        def executar_gerenciador():
            while True:
                dados_sensores = coletar_dados_sensores()
                enviar_dados_nuvem(dados_sensores)
                processar_dados(dados_sensores)
                
        executar_gerenciador()
        
        client_socket.close()
        print("Conexão encerrada com:", client_address)
        
finally:
    server_socket.close()