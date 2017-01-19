from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Index, DateTime
import mysql.connector
import datetime

Base = declarative_base()

def get_session():
	engine = create_engine("mysql+pymysql://root:123@localhost:3306/mydb?charset=utf8", max_overflow=5)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session


class CityCode(Base):
	__tablename__ = 'city_code'

	id = Column(Integer, primary_key=True)
	code = Column(String(32))
	name = Column(String(64))
	gmt_create = Column(DateTime)
	gmt_modified = Column(DateTime)

#city_code = CityCode(code='0001', name='北京', gmt_create=datetime.datetime.utcnow(), gmt_modified= datetime.datetime.utcnow())
session = get_session()
#session.add(city_code)

#session.query(Flow).filter(Flow.trace_id == 1).count()
print (session.query(CityCode).filter(CityCode.id == 1).count())
session.query(CityCode).filter(CityCode.id == 1).update({'gmt_modified':datetime.datetime.utcnow()})

session.commit()
session.close(); 