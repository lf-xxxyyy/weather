from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Index, DateTime
from flask import Flask
import mysql.connector
import datetime
import urllib
import json


app = Flask(__name__)


Base = declarative_base()

def get_session():
	engine = create_engine("mysql+pymysql://root:123@localhost:3306/mydb?charset=utf8", max_overflow=5)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

#session = get_session()

class CityCode(Base):
	__tablename__ = 'city_code'

	id = Column(Integer, primary_key=True)
	code = Column(String(32))
	name = Column(String(64))
	gmt_create = Column(DateTime, default=datetime.datetime.now())
	gmt_modified = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

#city_code = CityCode(code='0001', name='北京')

#session.add(city_code)

#session.query(CityCode).filter(CityCode.id == 1).update({'name':'上海'})

#session.commit()
#session.close(); 



def query_all_city_code() :
	session = get_session()
	return session.query(CityCode).all()


@app.route('/')
def query_weather_of_city():
	weatherHtml = urllib.request.urlopen('http://www.weather.com.cn/data/cityinfo/101010100.html')
	result = weatherHtml.read().decode('utf8')
	weatherJSON = json.JSONDecoder().decode(result)
	weatherInfo = weatherJSON['weatherinfo']
	return weatherInfo['temp1']



@app.route('/displaycity')
def display_city():
	session = get_session()
	cityList = session.query(CityCode).all()
	for cl in cityList:
		print (cl.name)
	return "hello"






@app.route('/addcitycode/<code>/<name>')
def add_city_code(code, name):
	session = get_session()
	city_code = CityCode(code=code, name = name)
	session.add(city_code)
	session.commit()
	session.close()
	return "success"



if __name__ == '__main__' :
	app.run()



