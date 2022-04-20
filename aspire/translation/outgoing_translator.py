import aspire.translation.brain_pb2 as brain_pb2
import aspire.translation.brain_pb2_grpc as brain_pb2_grpc

import aspire.translation.graph_pb2 as graph_pb2
import aspire.translation.graph_pb2_grpc as graph_pb2_grpc

import aspire.translation.coordinates_pb2 as coordinates_pb2
import aspire.translation.coordinates_pb2_grpc as coordinates_pb2_grpc
import aspire.translation.cell_pb2 as cell_pb2
import aspire.translation.cell_pb2_grpc as cell_pb2_grpc
import aspire.translation.table_pb2 as table_pb2
import aspire.translation.table_pb2_grpc as table_pb2_grpc

from aspire.translation.ontology.spo import SPO
from aspire.translation.ontology.entity import Entity
from aspire.translation.ontology.relation import Relation


class outgoing_translator:
	def formatOutgoing(Message):
		# Convert knowledge graph cell representation to GRPC Proto
		cells = []
		for element in Message:
			cell = cell_pb2.Cell(uid=str(element._properties["uid"]),coordinates=coordinates_pb2.Coordinates(row=int(element._properties["row"]), col=int(element._properties["col"])),value=element._properties["value"])
			cells.append(cell)
		return cells