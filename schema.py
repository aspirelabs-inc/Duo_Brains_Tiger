from aspire.database.query_manager import query_manager

query_manager.runQuery('''
USE GRAPH Duo

CREATE SCHEMA_CHANGE JOB Duo_Schema FOR GRAPH Duo {

	ADD VERTEX Cell (PRIMARY_ID id INT, viewReference INT, hash STRING, value STRING, row STRING, col STRING) WITH primary_id_as_attribute="TRUE";

	ADD DIRECTED EDGE HAS_CHILD (FROM Cell, TO Cell);
	ADD DIRECTED EDGE HAS_PARENT (FROM Cell, TO Cell);

}

RUN SCHEMA_CHANGE JOB Duo_Schema

''')