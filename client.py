import grpc
from concurrent import futures
import time


import brain_pb2
import brain_pb2_grpc

import graph_pb2
import graph_pb2_grpc

import coordinates_pb2
import coordinates_pb2_grpc
import cell_pb2
import cell_pb2_grpc
import table_pb2
import table_pb2_grpc

import config


channel = grpc.insecure_channel('localhost:8080')
brainStub = brain_pb2_grpc.BrainStub(channel)
graphStub = graph_pb2_grpc.GraphStub(channel)

# request = brain_pb2.UserCopyPasteRequest(from_table_uid="0", to_table_uid="1")
# copyPaste = brainStub.UserCopyPaste(request)

# print("The shit")
# print(copyPaste)

#responseCells = copyPaste.cells

request = graph_pb2.AddRequest(table=table_pb2.Table(uid="0", name="0", cells=[cell_pb2.Cell(uid="292111136",coordinates=coordinates_pb2.Coordinates(),value="Company"),cell_pb2.Cell(uid="2143500677",coordinates=coordinates_pb2.Coordinates(col=1),value="Contact"),cell_pb2.Cell(uid="1075296975",coordinates=coordinates_pb2.Coordinates(col=2),value="Country"),cell_pb2.Cell(uid="643294799",coordinates=coordinates_pb2.Coordinates(row=1),value="AlfredsFutterkiste"),cell_pb2.Cell(uid="330708918",coordinates=coordinates_pb2.Coordinates(row=1,col=1),value="MariaAnders"),cell_pb2.Cell(uid="1865576430",coordinates=coordinates_pb2.Coordinates(row=1,col=2),value="Germany"),cell_pb2.Cell(uid="786473412",coordinates=coordinates_pb2.Coordinates(row=2),value="CentrocomercialMoctezuma"),cell_pb2.Cell(uid="150472825",coordinates=coordinates_pb2.Coordinates(row=2,col=1),value="FranciscoChang"),cell_pb2.Cell(uid="118929904",coordinates=coordinates_pb2.Coordinates(row=2,col=2),value="Mexico"),cell_pb2.Cell(uid="231344122",coordinates=coordinates_pb2.Coordinates(row=3),value="ErnstHandel"),cell_pb2.Cell(uid="1146756079",coordinates=coordinates_pb2.Coordinates(row=3,col=1),value="RolandMendel"),cell_pb2.Cell(uid="1177622414",coordinates=coordinates_pb2.Coordinates(row=3,col=2),value="Austria"),cell_pb2.Cell(uid="808421865",coordinates=coordinates_pb2.Coordinates(row=4),value="IslandTrading"),cell_pb2.Cell(uid="421247298",coordinates=coordinates_pb2.Coordinates(row=4,col=1),value="HelenBennett"),cell_pb2.Cell(uid="550556263",coordinates=coordinates_pb2.Coordinates(row=4,col=2),value="UK"),cell_pb2.Cell(uid="1009215780",coordinates=coordinates_pb2.Coordinates(row=5),value="LaughingBacchusWinecellars"),cell_pb2.Cell(uid="302051192",coordinates=coordinates_pb2.Coordinates(row=5,col=1),value="YoshiTannamuri"),cell_pb2.Cell(uid="110208742",coordinates=coordinates_pb2.Coordinates(row=5,col=2),value="Canada")] ))
Add = graphStub.Add(request)

print("Added first table")

request = graph_pb2.AddRequest(table=table_pb2.Table(uid="1", name="1", cells=[cell_pb2.Cell(uid="292111136",coordinates=coordinates_pb2.Coordinates(),value="Company"),cell_pb2.Cell(uid="2143500677",coordinates=coordinates_pb2.Coordinates(col=1),value="Contact"),cell_pb2.Cell(uid="1075296975",coordinates=coordinates_pb2.Coordinates(col=2),value="Country"),cell_pb2.Cell(uid="643294799",coordinates=coordinates_pb2.Coordinates(row=1),value="AlfredsFutterkiste")]))
Add = graphStub.Add(request)

print("Added second table")

copyTables = brain_pb2.CopyTableRequest(from_table_uid="0",to_table_uid="1")
changes = brainStub.CopyTable(copyTables)

print("You've been compared boi")