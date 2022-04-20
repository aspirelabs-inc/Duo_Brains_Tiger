from aspire.database.query_manager import query_manager

class prediction_engine:
	def Predict():
		# Get Parents of Cell
		query_manager.runQuery('MATCH (c:Cell {viewReference: 0}) RETURN c')

		query = query_manager.db_driver.session().read_transaction(get_data,'MATCH (c:Cell{uid: 110208742})-[p:HAS_PARENT]-(n) RETURN n',"n")
		print(query)

		# Update Node with Parents
		updateQuery = query_manager.db_driver.session().write_transaction(get_data,'MATCH (n)-[p:HAS_CHILD]-(h:Cell{uid: 110208742}) SET n.value = "Updated value"')
		updateQuery = query_manager.db_driver.session().write_transaction(get_data,'MATCH (r:Cell{uid: 1009215780})-[:HAS_CHILD]->(t:Cell)-[:HAS_PARENT]->(c:Cell{uid: 1075296975}) SET t.value = "Updated value"')