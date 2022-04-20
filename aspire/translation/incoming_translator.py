#import aspire.translation.translator


# Remove
#import aspire.translation.outgoing_translator as outgoing_translator


import grpc
from google.protobuf.json_format import MessageToJson

import random

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

import aspire.translation.list_pb2 as list_pb2
import aspire.translation.text_pb2 as text_pb2
import aspire.translation.button_pb2 as button_pb2
import aspire.translation.link_pb2 as link_pb2

import aspire.translation.pixel_location_pb2 as pixel_location_pb2

from aspire.translation.ontology.spo import SPO
from aspire.translation.ontology.entity import Entity
from aspire.translation.ontology.relation import Relation

from aspire.database.query_manager import query_manager

copyPasteActions = []

tables = dict()
table_full = dict()

entityContainer = dict()

class incoming_translator:
	def generateTable(table_id, tableCells):
		for cell in tableCells:
			# Create Entity Object
			node = Entity(cell.uid,table_id,cell,"Cell",cell.value,cell.coordinates.row,cell.coordinates.col)
			query_manager.input(node, "Create")

			# Does this contain a value? If so what is it and create another entity
			if node.Value:
				# TODO: Determine string type. Is this a time? Date? Etc.
				textEntity = Entity(random.randint(111111111, 999999999),table_id,None,"Text",cell.value)
				# Add to DB
				query_manager.input(textEntity, "Create")

				# Create directed edge to cell
				relation = Relation(node,"CONTAINS_TEXT",textEntity)
				query_manager.input(relation, "Create")


			# Create two spo objects each for the first row and column cell
			# One connecting the child to the parent and another connecting the parent to the child
			# Skip the very first cell in the table (0,0) since there's no parent cell to connect it to

			if cell.coordinates.row == 0 or cell.coordinates.col == 0:
				print("SKIPPED")
			else:
				print("Current cell value: "+cell.value)
				pCol = tables[int(table_id)][0][cell.coordinates.col]
				pRow = tables[int(table_id)][cell.coordinates.row][0]
				print("Parent is: Col:"+str(pCol.coordinates.col)+":"+str(pCol.coordinates.row)+":"+pCol.value)
				print("Parent is: Row:"+str(pRow.coordinates.col)+":"+str(pRow.coordinates.row)+":"+pRow.value)

				pColNode = Entity(pCol.uid,table_id,pCol,"Cell",pCol.value,pCol.coordinates.row,pCol.coordinates.col)
				pRowNode = Entity(pRow.uid,table_id,pRow,"Cell",pRow.value,pRow.coordinates.row,pRow.coordinates.col)


				# parent_of_n[table_id][genCoordHash(cell)] = [pCol,pRow]

				# child_of_n[table_id][genCoordHash()]

				# Add Parent relationships
				
				# Create directed edge to cell
				relation = Relation(node,"HAS_PARENT",pRowNode)
				query_manager.input(relation, "Create")
				relation = Relation(node,"HAS_PARENT",pColNode)
				query_manager.input(relation, "Create")

				# UISnapshot.append(SPO(node,"HAS_PARENT",pRow))
				# UISnapshot.append(SPO(node,"HAS_PARENT",pCol))

				# Add Child relationships

				relation = Relation(pRowNode,"HAS_CHILD",node)
				query_manager.input(relation, "Create")
				relation = Relation(pColNode,"HAS_CHILD",node)
				query_manager.input(relation, "Create")
				
				# UISnapshot.append(SPO(pRow,"HAS_CHILD",node))
				# UISnapshot.append(SPO(pCol,"HAS_CHILD",node))

				print("Added relationships")

			# Add spatial relations (Not requried for table structure)
	def generateInteractable(object, type):

		print (object.value)
		# Generate interactable element and send to query manager to generate query
		interactable = Entity(random.randint(111111111, 999999999),"0",None,type,object.value)
		query_manager.input(interactable, "Create")

	def generateList(object):
		print (object)
		for elements in object.elements:
			for interactable in elements.list_data:
				print (interactable)
				print (interactable.DESCRIPTOR.fields_by_name.keys())
				#generateInteractable(interactable)


def CopyTables(to_table_id, from_table_id):
	query = 'MATCH (c:Cell {viewReference: 0}) RETURN c'
	values = query_manager.db_driver.session().write_transaction(query_manager.get_data, query, "c")

	updateCells = []
	for value in values:
		print (value._properties["value"])
		parents = query_manager.db_driver.session().write_transaction(query_manager.get_data,'MATCH (c:Cell{uid: '+str(value._properties["uid"])+'})-[p:HAS_PARENT]-(n) RETURN n',"n")
		parentList = []
		print (parents)
		for parent in parents:
			parentList.append(parent)
		if len(parentList) == 2:
			updateQuery = query_manager.db_driver.session().write_transaction(query_manager.executeQuery,'MATCH (r:Cell{value: "'+parentList[0]._properties["value"]+'"})-[:HAS_CHILD]->(t:Cell)-[:HAS_PARENT]->(c:Cell{value: "'+parentList[1]._properties["value"]+'"}) SET t.value = "'+value._properties["value"]+'"')
	cells = query_manager.db_driver.session().read_transaction(query_manager.get_data, "MATCH (c:Cell {viewReference: 1}) RETURN c", "c")
	returnCells = []
	for element in cells:
		cell = cell_pb2.Cell(uid=str(element._properties["uid"]),coordinates=coordinates_pb2.Coordinates(row=int(element._properties["row"]), col=int(element._properties["col"])),value=element._properties["value"])
		returnCells.append(cell)

	return returnCells

class BrainsServicer(brain_pb2_grpc.BrainServicer):
    def UserCopyPaste(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print("hello: from:"+request.from_table_uid+" to: "+request.to_table_uid)
        # Save copy paste action to copyPasteActions list
        copyPasteActions.append([request.from_table_uid,request.to_table_uid])

        cells = []
        # Are there more than 3 copy paste tasks?
        if (copyPasteActions.count([request.from_table_uid,request.to_table_uid]) >= 3):
        	cells = CopyTables(request.from_table_uid,request.to_table_uid)

        return brain_pb2.UserCopyPasteResponse(cells=cells)

    def CopyTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        CopyTables(request.from_table_uid,request.to_table_uid)
        return brain_pb2.CopyTableRequest(calls=cells)

    def UserAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        print(request.keys)
        return brain_pb2.UserActionResponse()

class GraphServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Add(self, request, context):
        """Missing associated documentation comment in .proto file."""

        print ("__________________")
        if request.HasField("button"):
        	print ("Button Value: "+request.button.value)
        	print ("Create button")
        	incoming_translator.generateInteractable(request.button, "Button")

        elif request.HasField("text"):
        	print ("Create text")
        	incoming_translator.generateInteractable(request.button, "Text")

        elif request.HasField("link"):
        	print ("Create link")
        	incoming_translator.generateInteractable(request.button, "Link")

        elif request.HasField("list"):
        	incoming_translator.generateList(request.list)
        	print ("List currently WIP")

        elif request.HasField("table"):
        	print("Adding Table")

	        # Get last cell of table to determine the table size
	        size = request.table.cells[-1].coordinates
	        table = [['' for x in range(size.col+1)] for y in range(size.row+1)] 

	        row = 0
	        col = 0
	        for cell in request.table.cells:
	        	if cell.coordinates.row > row:
	        		row = cell.coordinates.row
	        	if cell.coordinates.col > col:
	        		col = cell.coordinates.col
	        table = [['' for x in range(col+1)] for y in range(row+1)] 
	        

	        # Populate table list
	        for cell in request.table.cells:
	        	table[cell.coordinates.row][cell.coordinates.col] = cell

	        # Store original table and brain table
	        table_full[int(request.table.uid)] = request.table
	        tables[int(request.table.uid)] = table

	        # Generate UI Knowledge Graph
	        print("Table ID: "+request.table.uid)
	        incoming_translator.generateTable(request.table.uid, request.table.cells)

	        print("Added Table "+request.table.name)
	        # print(get_headers(request.table.uid))

        else:
        	print ("This type hasn't been implemented")


        return graph_pb2.AddResponse()

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def Testing():
	# Testing

	GraphServicer.Add("", graph_pb2.AddRequest(list=list_pb2.List(parent_uid = "0", uid = "0", name = "List #1", elements = [ 
		list_pb2.ListElement (list_data=[ list_pb2.ListElementObjects( button = button_pb2.Button(parent_uid = "0", uid = "0", location = pixel_location_pb2.PixelLocation(top = 0, bottom = 0, left = 0, right = 0), value="Market button") ) ]),
		list_pb2.ListElement (list_data=[ list_pb2.ListElementObjects( text = text_pb2.Text(parent_uid = "0", uid = "0", location = pixel_location_pb2.PixelLocation(top = 0, bottom = 0, left = 0, right = 0), value="Market text") ) ])
	] )), None)

	# list_pb2.ListElementObjects(button_pb2.Button(parent_uid = "0", uid = "0", location = pixel_location_pb2.PixelLocation(top = 0, bottom = 20, left = 0, right = 40), value="Market button"))

	#GraphServicer.Add("", graph_pb2.AddRequest(button=button_pb2.Button(parent_uid = "0", uid = "0", location = pixel_location_pb2.PixelLocation(top = 0, bottom = 0, left = 0, right = 0), value="Market button")),None)

	# GraphServicer.Add("", graph_pb2.AddRequest(table=table_pb2.Table(uid="0", name="0", cells=[cell_pb2.Cell(uid="292111136",coordinates=coordinates_pb2.Coordinates(),value="Company"),cell_pb2.Cell(uid="2143500677",coordinates=coordinates_pb2.Coordinates(col=1),value="Contact"),cell_pb2.Cell(uid="1075296975",coordinates=coordinates_pb2.Coordinates(col=2),value="Country"),cell_pb2.Cell(uid="643294799",coordinates=coordinates_pb2.Coordinates(row=1),value="AlfredsFutterkiste"),cell_pb2.Cell(uid="330708918",coordinates=coordinates_pb2.Coordinates(row=1,col=1),value="MariaAnders"),cell_pb2.Cell(uid="1865576430",coordinates=coordinates_pb2.Coordinates(row=1,col=2),value="Germany"),cell_pb2.Cell(uid="786473412",coordinates=coordinates_pb2.Coordinates(row=2),value="CentrocomercialMoctezuma"),cell_pb2.Cell(uid="150472825",coordinates=coordinates_pb2.Coordinates(row=2,col=1),value="FranciscoChang"),cell_pb2.Cell(uid="118929904",coordinates=coordinates_pb2.Coordinates(row=2,col=2),value="Mexico"),cell_pb2.Cell(uid="231344122",coordinates=coordinates_pb2.Coordinates(row=3),value="ErnstHandel"),cell_pb2.Cell(uid="1146756079",coordinates=coordinates_pb2.Coordinates(row=3,col=1),value="RolandMendel"),cell_pb2.Cell(uid="1177622414",coordinates=coordinates_pb2.Coordinates(row=3,col=2),value="Austria"),cell_pb2.Cell(uid="808421865",coordinates=coordinates_pb2.Coordinates(row=4),value="IslandTrading"),cell_pb2.Cell(uid="421247298",coordinates=coordinates_pb2.Coordinates(row=4,col=1),value="HelenBennett"),cell_pb2.Cell(uid="550556263",coordinates=coordinates_pb2.Coordinates(row=4,col=2),value="UK"),cell_pb2.Cell(uid="1009215780",coordinates=coordinates_pb2.Coordinates(row=5),value="LaughingBacchusWinecellars"),cell_pb2.Cell(uid="302051192",coordinates=coordinates_pb2.Coordinates(row=5,col=1),value="YoshiTannamuri"),cell_pb2.Cell(uid="110208742",coordinates=coordinates_pb2.Coordinates(row=5,col=2),value="Canada")] )), None)

	# #print("Added first table")

	# GraphServicer.Add("", graph_pb2.AddRequest(table=table_pb2.Table(uid="1", name="1", cells=[cell_pb2.Cell(uid="292111116",coordinates=coordinates_pb2.Coordinates(),value="Company"),cell_pb2.Cell(uid="2142500677",coordinates=coordinates_pb2.Coordinates(col=1),value="Country"),cell_pb2.Cell(uid="1075296973",coordinates=coordinates_pb2.Coordinates(col=2),value="Contact"),cell_pb2.Cell(uid="643194799",coordinates=coordinates_pb2.Coordinates(row=1),value="AlfredsFutterkiste"),cell_pb2.Cell(uid="330718918",coordinates=coordinates_pb2.Coordinates(row=1,col=1),value=""),cell_pb2.Cell(uid="1865576433",coordinates=coordinates_pb2.Coordinates(row=1,col=2),value=""),cell_pb2.Cell(uid="786473411",coordinates=coordinates_pb2.Coordinates(row=2),value="CentrocomercialMoctezuma"),cell_pb2.Cell(uid="150472824",coordinates=coordinates_pb2.Coordinates(row=2,col=1),value=""),cell_pb2.Cell(uid="118922904",coordinates=coordinates_pb2.Coordinates(row=2,col=2),value=""),cell_pb2.Cell(uid="231345122",coordinates=coordinates_pb2.Coordinates(row=3),value="ErnstHandel"),cell_pb2.Cell(uid="1146756073",coordinates=coordinates_pb2.Coordinates(row=3,col=1),value=""),cell_pb2.Cell(uid="1172622414",coordinates=coordinates_pb2.Coordinates(row=3,col=2),value=""),cell_pb2.Cell(uid="808421965",coordinates=coordinates_pb2.Coordinates(row=4),value="IslandTrading"),cell_pb2.Cell(uid="421247218",coordinates=coordinates_pb2.Coordinates(row=4,col=1),value=""),cell_pb2.Cell(uid="550558263",coordinates=coordinates_pb2.Coordinates(row=4,col=2),value=""),cell_pb2.Cell(uid="1009213780",coordinates=coordinates_pb2.Coordinates(row=5),value="LaughingBacchusWinecellars"),cell_pb2.Cell(uid="302051122",coordinates=coordinates_pb2.Coordinates(row=5,col=1),value=""),cell_pb2.Cell(uid="111208742",coordinates=coordinates_pb2.Coordinates(row=5,col=2),value="")] )), None)

	# query = 'MATCH (c:Cell {viewReference: 0}) RETURN c'
	# values = query_manager.db_driver.session().write_transaction(query_manager.get_data, query, "c")

	# updateCells = []
	# for value in values:
	# 	print (value._properties["value"])
	# 	parents = query_manager.db_driver.session().write_transaction(query_manager.get_data,'MATCH (c:Cell{uid: '+str(value._properties["uid"])+'})-[p:HAS_PARENT]-(n) RETURN n',"n")
	# 	parentList = []
	# 	print (parents)
	# 	for parent in parents:
	# 		parentList.append(parent)
	# 	if len(parentList) == 2:
	# 		updateQuery = query_manager.db_driver.session().write_transaction(query_manager.executeQuery,'MATCH (r:Cell{value: "'+parentList[0]._properties["value"]+'"})-[:HAS_CHILD]->(t:Cell)-[:HAS_PARENT]->(c:Cell{value: "'+parentList[1]._properties["value"]+'"}) SET t.value = "'+value._properties["value"]+'"')
	# cells = query_manager.db_driver.session().read_transaction(query_manager.get_data, "MATCH (c:Cell {viewReference: 1}) RETURN c", "c")
	# return cells

Testing()