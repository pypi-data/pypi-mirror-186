# ciri_results_db. EXTENDED DOCUMENTATION FOUND HERE: https://cirui.atlassian.net/l/cp/4RTuBfG6
Repo containing files related the results database of the results processing (ciri) app.
### Data Visualizer Folder/postgis.py
When run with all supporting files in directory, creates a local/remote geospatial DB and then plots the data.
### csvConverters folder/csvToPg.py (and csvToSqlite.py)
When run, this script reads and converts all CSVs and EXCELs in the CsvData folder and converts them to either a PG or SQLITE database.
### jsonBuilder folder/jsonBuilder.py
When run, this program creates a classifiers.json and result_tables.json in jsonResults/ using remote Postgres sample data (NWT_01_SampleProject_results). 
### pg2sqlite_metadata.py (OUTDATED: See pg2sqlite_md.py)
When run, this script connects to a remote Heroku Postgres database that contains metadata. The Postgres database is then copied and converted to a SQLite3 .db file.
### sqlite2pg_metadata.py (OUTDATED: See sqlite2pg_md.py)
When run, this script takes the .db file generated from the above script and copies and converts to a locally hosted Postgres database.
### pg2sqlite_sampledb.py (OUTDATED: See pg2sqlite_md.py)
When run, this script connects to a remote Heroku Postgres database that contains sample data. The Postgres database is then copied and converted to a SQLite3 .db file.
### sqlite2pg_sampledb.py (OUTDATED: See sqlite2pg_md.py)
When run, this script takes the .db file generated from the above script and copies and converts to a locally hosted Postgres database.
### postgresDatabase.sql
This is the SQL script for creating the sample data database used by the pg2sqlite/sqlite2pg_sampledb.py scripts.
### postgresMetadata.sql
This is the SQL script for creating the metadata database used by the pg2sqlite/sqlite2pg_metadata.py scripts.
### pg2sqlite_md.py
This is a refactored version of the pg2sqlite_metadata.py and pg2sqlite_sampledb.py DB generation scripts.
### sq2lite2pg_md.py
This is a refactored version of the sqlite2pg_metadata.py and sqlite2pg_sampledb.py DB generation scripts.

Documentation for all scripts coming soon.
