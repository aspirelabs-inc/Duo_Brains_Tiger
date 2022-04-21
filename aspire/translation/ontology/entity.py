class Entity:
	def __init__(self, UID, ViewReference, Object, Type, Value, Row=-1, Col=-1):
		self.UID = str(UID)
		self.ViewReference = ViewReference
		self.Object = Object
		self.Type = Type
		self.Value = Value
		self.Row = Row
		self.Col = Col

	def toCreateQuery(self):
		hash = self.getHash()
		print ("INSERT INTO "+self.Type+" VALUES ("+self.UID+","+self.ViewReference+",'"+str(hash)+"','"+self.Value+"','"+str(self.Row)+"','"+str(self.Col)+"');")
		return "CREATE QUERY CreateVertex() FOR GRAPH Duo { INSERT INTO "+self.Type+" VALUES ("+self.UID+","+self.ViewReference+",'"+str(hash)+"','"+self.Value+"','"+str(self.Row)+"','"+str(self.Col)+"');}"

	def getHash(self):
		return str(hash(self.ViewReference+self.UID+self.Type+self.Value))