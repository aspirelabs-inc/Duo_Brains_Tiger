from neo4j import GraphDatabase

class query_manager:
	uri = "bolt://localhost:7687"
	db_driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

	def input(Object, Type):
		# Determine what type of query needs to be executed
		print (Object.toCreateQuery())
		if Type == "Create":
			query_manager.db_driver.session().write_transaction(query_manager.create, Object.toCreateQuery())
		elif Type == "Search":
			query_manager.db_driver.session().write_transaction(query_manager.get_data, Object.toCreateQuery())


	def runQuery(query):
		return query_manager.db_driver.session().write_transaction(query_manager.executeQuery, query)

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

		# objects = []
		# for record in result:
		# 	print (record)

		#movies = session.read_transaction()

# 	print (value)
# 	cells.append(value["c"])