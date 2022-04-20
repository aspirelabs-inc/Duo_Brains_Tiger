# Clear on each run
from aspire.database.query_manager import query_manager
query_manager.runQuery('drop all')


import grpc
from concurrent import futures
import time

import aspire.translation.brain_pb2_grpc as brain_pb2_grpc
import aspire.translation.graph_pb2_grpc as graph_pb2_grpc

from aspire.translation.incoming_translator import incoming_translator, BrainsServicer, GraphServicer, Testing
from aspire.translation.outgoing_translator import outgoing_translator

import config

import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# embeddings = False

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

	brain_pb2_grpc.add_BrainServicer_to_server(BrainsServicer(), server)
	graph_pb2_grpc.add_GraphServicer_to_server(GraphServicer(), server)

	# brain_pb2_grpc.add_BrainServicer_to_server(BrainsServicer(), server)
	# graph_pb2_grpc.add_GraphServicer_to_server(GraphServicer(), server)

	print("Starting server: "+get_ip()+":8080")
	#server.add_insecure_port('[::]:8080')
	server.add_insecure_port(get_ip()+':8080')
	server.start()
	server.wait_for_termination()

#serve()

# cells = CopyTables("0","1")

# print (cells)

print(outgoing_translator.formatOutgoing(incoming_translator.Testing()))


# Get Parents of Cell
#query = query_manager.db_driver.session().read_transaction(get_data,'MATCH (c:Cell{uid: 110208742})-[p:HAS_PARENT]-(n) RETURN n',"n")
#print(query)

# Update Node with Parents
# updateQuery = query_manager.db_driver.session().write_transaction(get_data,'MATCH (n)-[p:HAS_CHILD]-(h:Cell{uid: 110208742}) SET n.value = "Updated value"')
#updateQuery = query_manager.db_driver.session().write_transaction(get_data,'MATCH (r:Cell{uid: 1009215780})-[:HAS_CHILD]->(t:Cell)-[:HAS_PARENT]->(c:Cell{uid: 1075296975}) SET t.value = "Updated value"')