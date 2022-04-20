import pyTigerGraph as tg
import config

token = tg.TigerGraphConnection(host=config.hostName, graphname=config.graphName)
print (token)

token.getToken(config.secret)[0]


conn = tg.TigerGraphConnection(host=config.hostName, graphname=config.graphName, password=config.password, apiToken=token)


# print ("Auth Token: {authToken}")

def get_data(tx, query, Object):
	outputList = []
	result = tx.run(query)
	for output in result:
		print(output)
		outputList.append(output[Object])
	return outputList

def create(tx,query):
	result = tx.run(query)
	print (result)

	# objects = []
	# for record in result:
	# 	print (record)

	#movies = session.read_transaction()

# print ("Done")