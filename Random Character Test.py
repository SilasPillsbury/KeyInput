import sqlalchemy as sqla
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import text

engine = create_engine("sqlite:///keyInput.db", echo=True)

def main():
  conn = engine.connect()
  metadata = MetaData()
  createTables(metadata, conn)
  keysIn = input("\nPlease mash random keys on your keyboard.\n After ten or so keys, press enter.\n")
  keysIn = keysIn[0:10]
  statement = text("INSERT INTO inKeys (char) values ('" + keysIn + "')")
  #sqla.insert(characters,keysIn)
  conn.execute(statement)

def createTables(metadata, conn):
  inKeys = Table('inKeys',metadata,
    Column('id', Integer, primary_key=True),
    Column('char',String)
  )

  metadata.create_all(engine)

main()
