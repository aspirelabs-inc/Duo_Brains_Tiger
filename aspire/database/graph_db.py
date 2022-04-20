from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
db_driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

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