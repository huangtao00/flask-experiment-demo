#coding:utf-8
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

#数据库中表的映射对象，通过下面的object,完成数据库的crud操作
class Flight(db.Model):
	__tablename__="flights"
	id=db.Column(db.Integer,primary_key=True)
	origin=db.Column(db.String,nullable=False)
	destination=db.Column(db.String,nullable=False)
	duration=db.Column(db.Integer,nullable=False)


class Passenger(db.Model):
	__tablename__="passengers"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String,nullable=False)
	flight_id=db.Column(db.Integer, db.ForeignKey("flights.id"),nullable=False)

# 写入航班信息到数据库，数据可来源于用户输入，或网上爬取
def addflight(ori,des,dur):
    flight=Flight(origin=ori,destination=des,duration=dur)
    db.session.add(flight)
    db.session.commit()

def query_all_flights():
    all_flights=[]
    for flight in Flight.query.all():
        # print flight.__dict__
        all_flights.append(flight.__dict__)
    return all_flights

#一对多（多的表里面保存外键，指向一的主键）： 一个航班的飞机上 可以有 很多乘客    