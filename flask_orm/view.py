#coding:utf-8
from create import app, db 
from flask import render_template, request,redirect, flash, session
from model import addflight, query_all_flights, Flight
@app.route("/")
def index():
    filename="index.html"
    data={}
    flights_list=query_all_flights()
    if flights_list:
        data["flights"]=flights_list
    # data["msg"]=session.get("msg",False)
    # session["msg"]=False
    return render_template(filename, **data)


@app.route("/flight",methods=["POST"])
def addFlight():
    if request.method=="POST":
        # print request.form
        ori=request.form['origin']
        des=request.form['destination']
        dur=request.form['duration']
        addflight(ori=ori,des=des,dur=dur)
        # session["msg"]=True
        flash(u"恭喜你，航班信息添加成功！")
    return redirect("/")

@app.route("/flight/delete/<int:id>", methods=["get"])
def deleteFlight(id):
    Flight.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/")