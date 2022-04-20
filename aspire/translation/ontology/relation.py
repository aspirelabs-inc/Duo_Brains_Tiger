class Relation:
	def __init__(self, Subject, Predicate, Object):
		self.Subject = Subject
		self.Predicate = Predicate
		self.Object = Object


	def toCreateQuery(self):
		return "MATCH (s:"+self.Subject.Type+" { uid:"+self.Subject.UID+"}), (p:"+self.Object.Type+" { uid:"+self.Object.UID+"}) MERGE (s)-[d:"+self.Predicate+"]-(p)"
