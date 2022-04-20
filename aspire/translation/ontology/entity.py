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
		return "CREATE (:"+self.Type+" { uid:"+self.UID+", viewReference:"+self.ViewReference+", hash:"+str(hash)+", value:\""+self.Value+"\", row:\""+str(self.Row)+"\", col:\""+str(self.Col)+"\"})"

	def getHash(self):
		return str(hash(self.ViewReference+self.UID+self.Type+self.Value))