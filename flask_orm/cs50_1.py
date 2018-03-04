class Flight(object):
	"""docstring for Flight"""
	count=0
	def __init__(self, ori,des,dur):
		Flight.count+=1
		self.ori=ori
		self.des=des
		self.dur=dur
		self.id=Flight.count

		self.passenger=[]
	def delay(self,amount):
		self.dur+=amount
	def addPassenger(self,p):
		self.passenger.append(p)
		p.flight_id=self.id


class Passenger(object):
	"""docstring for Passenger"""
	def __init__(self, name):
		self.name = name
		self.flight_id=None
		
def main():
	print ("now we have %d Flights" %Flight.count)
	f=Flight("Wuhan","Shahai",540)
	f.dur+=10
	print (f.ori,f.des,f.dur)
	f1=Flight("Wuhan","Shahai",540)
	print ("now we have %d Flights" % Flight.count)
	f2=Flight("Wuhan","Shahai",540)
	print ("now we have %d Flights" % Flight.count)
	print ("now we have",f.count, "Flights")
	f1.delay(30)
	print ("flight 1 duration",f1.dur)
	time=Passenger("Time")
	jack=Passenger("Jack")
	cat=Passenger("cat")
	f1.addPassenger(time)
	print (f1.passenger)
	print pass_jim.flight_id
	f1.addPassenger(jack)
	print "passengers in flight:",f1.id
	for p in f1.passenger:
		print  p.name


if __name__=="__main__":
	main()