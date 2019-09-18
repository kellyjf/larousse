#!/usr/bin/python3


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey


Base=declarative_base()
engine=create_engine("sqlite:///junk.sqlite")
Session=sessionmaker(bind=engine)

class Root(Base):
	__tablename__ = "roots"

	id = Column(Integer, primary_key=True)
	root = Column(String)
	usages = relationship("Usage",back_populates='root',cascade="all, delete-orphan")

class Usage(Base):
	__tablename__ = "usages"

	id = Column(Integer, primary_key=True)
	address = Column(String)
	lienson = Column(String)
	grammar = Column(String)
	phonetic = Column(String)
	root_id = Column(Integer, ForeignKey('roots.id'))
	root = relationship("Root",back_populates='usages')
	meanings = relationship("Meaning",back_populates='usage',cascade="all, delete-orphan")

class Meaning(Base):
	__tablename__ = "meanings"

	id = Column(Integer, primary_key=True)
	meaning = Column(String)
	usage_id = Column(Integer, ForeignKey('usages.id'))
	usage = relationship("Usage",back_populates='meanings')
	examples = relationship("Example",back_populates='meaning',cascade="all, delete-orphan")

class Example(Base):
	__tablename__ = "examples"

	id = Column(Integer, primary_key=True)
	expression = Column(String)
	translation = Column(String)
	lienson = Column(String)
	meaning_id = Column(Integer, ForeignKey('meanings.id'))
	meaning = relationship("Meaning",back_populates='examples')

def create():
	Base.metadata.create_all(engine)

if __name__ == "__main__":
	print("Hello")

