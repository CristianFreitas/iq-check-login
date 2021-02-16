from iqoptionapi.stable_api import IQ_Option
import sys

API = IQ_Option('user', 'password')
API.connect();

API.change_balance('PRACTICE') # PRACTICE  / REAL

if API.check_connect():
	print('Conectado com Sucesso')
else:
	print(' Erro ao conectar')
	input('\n\n Aperte enter para sair')
	sys.exit()
