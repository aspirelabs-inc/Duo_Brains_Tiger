import pyTigerGraph as tg
import config

token = tg.TigerGraphConnection(host=config.hostName, graphname=config.graphName)
authToken = token.getToken(config.secret)[0]

conn = tg.TigerGraphConnection(host=config.hostName, graphname=config.graphName, password=config.password, apiToken=authToken)

def get_data(tx, query, Object):
	outputList = []
	conn.gsql(query, options=None)
	for output in result:
		print(output)
		outputList.append(output[Object])
	return outputList

def create(tx,query):
	conn.gsql(query, options=None)
	print (result)

	# objects = []
	# for record in result:
	# 	print (record)

	#movies = session.read_transaction()