import pyTigerGraph as tg
import config

class query_manager:
	token = tg.TigerGraphConnection(host=config.hostName, graphname=config.graphName)
	authToken = token.getToken(config.secret)[0]
	conn = tg.TigerGraphConnection(host=config.hostName, graphname=config.graphName, password=config.password, apiToken=authToken)

	def input(Object, Type):
		# Determine what type of query needs to be executed
		print (Object.toCreateQuery())
		if Type == "Create":
			query_manager.conn.gsql(Object.toCreateQuery())
		elif Type == "Search":
			query_manager.conn.gsql(Object.toCreateQuery())


	def runQuery(query):
		return query_manager.conn.gsql(query)

	def executeQuery(tx, query):
		result = tx.run(query)
		return result

	def get_data(tx, query, Object):
		outputList = []
		result = tx.run(query)
		for output in result:
			# print(output)
			outputList.append(output[Object])
		return outputList

	def create(tx,query):
		result = tx.run(query)

query_manager.conn.gsql('ls', options=[])

