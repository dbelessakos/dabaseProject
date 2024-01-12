#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import pymysql


#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
					   port = 3307,
                       user='root',
                       password='',
                       db='airlineRes',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

print("connections Succecsful")

#Define a route to hello function
@app.route('/')
def hello():
	return render_template('index.html')

#Define route for login
@app.route('/login')
def login():
	return render_template('login.html')

#Define route for register
@app.route('/register')
def register():
	return render_template('customer_register.html')

@app.route('/staff_register')
def staff_reg():
	return render_template('airline_register.html')

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
	#grabs information from the forms
	customer_name = request.form['customer_name']
	password = request.form['password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM CUSTOMER WHERE customer_name = %s and password = %s'
	cursor.execute(query, (customer_name, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['customer_name'] = customer_name
		return redirect(url_for('home'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)

@app.route('/staffLoginAuth', methods=['GET', 'POST'])
def staffLoginAuth():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Airline_Staff WHERE username = %s and password = %s'
	cursor.execute(query, (username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		return redirect(url_for('staffHome'))
	else:
		#returns an error message to the html page
		error = 'Invalid login or username'
		return render_template('login.html', error=error)

#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
	#grabs information from the forms
	customer_name = request.form['customer_name']
	customer_email = request.form['email']
	password = request.form['password']
	customer_address = request.form['address']
	buidling_number = request.form['buildingNumber']
	street = request.form['street']
	state = request.form['state']
	phone_number = ['phoneNumber']
	passport_number = request.form['passportNum']
	passport_expiration = request.form['passportExp']
	passport_country = request.form['country']

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM CUSTOMER WHERE customer_name = %s'
	cursor.execute(query, (customer_name))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('customer_register.html', error = error)
	else:
		ins = 'INSERT INTO CUSTOMER VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
		cursor.execute(ins, (customer_name,customer_email, password, customer_address, buidling_number,street,state,phone_number, passport_number, passport_expiration,passport_country))
		conn.commit()
		cursor.close()
		return render_template('index.html')




#Authenticates the register
@app.route('/staffRegisterAuth', methods=['GET', 'POST'])
def staffRegisterAuth():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	dob = request.form['dob']
	phone_number = request.form['phoneNumber']
	email = request.form['email']
	airline_name = request.form['airline_name']
	

	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM Airline_Staff WHERE username = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = 'INSERT INTO Airline_Staff VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
		cursor.execute(ins, (username,password, first_name, last_name, dob,phone_number,email,airline_name))
		conn.commit()
		cursor.close()
		return render_template('index.html')

@app.route('/home')
def home():  
    customer_name = session['customer_name']
    cursor = conn.cursor();
    cursor.close()
    return render_template('home.html', customer_name=customer_name)

@app.route('/staffHome')
def staffHome():  
    username = session['username']
    cursor = conn.cursor();
    cursor.close()
    return render_template('staffHome.html', username=username)

@app.route('/flightSearch', methods = ['GET','POST'])	
def flightSearch():
	departure = request.form['source_airport']
	arrival = request.form['destination_airport']
	date = request.form['departure_date'] 
	cursor = conn.cursor()
	querry= 'SELECT * FROM FLIGHT WHERE departure_airport = %s AND arrival_airport = %s AND departure_date = %s '
	cursor.execute(querry,(departure,arrival,date))
	data = cursor.fetchall()
	#conn.commit()
	cursor.close()
	print(data)
	return render_template('index.html', flight_info = data)

@app.route('/view_flight', methods = ['GET','POST'])
def viewFlights():
	customer_name = session['customer_name']
	s = str(session['customer_name'])
	print(s)
	cursor = conn.cursor()
	querry = 'SELECT Flight.flight_number,airline,departure_airport,departure_time,departure_date, arrival_airport,arrival_time,arrival_date,base_price,flight_id,status FROM Flight,Customer,Ticket WHERE Ticket.customer_email= Customer.customer_email AND Ticket.flight_number = Flight.flight_number AND Customer.customer_name = %s'
	cursor.execute(querry,(s))
	data = cursor.fetchall()
	cursor.close()
	print(data)
	
	return render_template('view_flight.html', customer_name = customer_name, flight_info = data)

@app.route('/view_staff_flights', methods = ['GET','POST'])
def view_staff_flights():
	username= session['username']
	#s = str(session['username'])
	airline_name = request.form['airline_name']
	#print(s)
	cursor = conn.cursor()
	querry = 'SELECT * FROM Flight WHERE airline_name = %s'
	cursor.execute(querry,(airline_name))
	data = cursor.fetchall()
	cursor.close()
	print(data)
	
	return render_template('view_staff_flights.html', username = username, flight_info = data)

@app.route('/cancel_trip', methods = ['GET','POST'])
def cancel():
	customer_name = session['customer_name']
	ticket_id = request.form['ticket_id']
	cursor = conn.cursor()
	querry = 'DELETE FROM TICKET WHERE ticket_id = %s'
	cursor.execute(querry,(ticket_id))
	data = cursor.fetchall()
	cursor.close()
	print(data)
	return render_template('cancel.html',customer_name = customer_name)

@app.route('/view_spending', methods = ['GET','POST'])
def spending():
	customer_name = session['customer_name']
	s = str(session['customer_name'])
	cursor = conn.cursor()
	querry = 'SELECT SUM(sold_price) FROM TICKET, CUSTOMER WHERE Ticket.customer_email = Customer.customer_email AND Customer.customer_name = %s'
	cursor.execute(querry,(s))
	data = cursor.fetchall()
	cursor.close()
	return render_template('view_spending.html', customer_name = customer_name, spending = data)

	
@app.route('/flightStatus', methods = ['GET','POST'])	
def flightStatus():
	airline= request.form['airline']
	flight_number = request.form['flight_number']
	departure_date = request.form['departure_date'] 
	cursor = conn.cursor()
	querry= 'SELECT * FROM FLIGHT WHERE airline = %s AND flight_number = %s AND departure_date = %s '
	cursor.execute(querry,(airline,flight_number,departure_date))
	data = cursor.fetchall()
	#conn.commit()
	cursor.close()
	print(data)
	return render_template('index.html', flight_info = data)
			
@app.route('/purchase_ticket', methods = ['GET','POST'])
def purchase():
	customer_name = session['customer_name']
	cursor= conn.cursor()
	querry = 'SELECT * FROM FLIGHT'
	cursor.execute(querry)
	data = cursor.fetchall()
	cursor.close()
	#print(data)
	
	return render_template('purchase.html',customer_name=customer_name,flight_info = data)

@app.route('/purch',methods= ['GET','POST'])
def purch():
	customer_name = session['customer_name']
	return render_template('purchase_page.html',customer_name=customer_name)

@app.route('/purchAuth',methods=['GET','POST'])
def purchAuth():
	email = request.form['email']
	address = request.form['customer_address']
	airline = request.form['airline_name']
	flight_number = request.form['flight_number']
	sold_price = request.form['sold_price']
	payment = request.form['payment_information']
	time = request.form['purchase_time']
	date = request.form['purchase_date']
	id = request.form['ticket_id']

	cursor= conn.cursor()

	ins = 'INSERT INTO Ticket VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %i)'
	cursor.execute(ins, (email,address, airline, flight_number, sold_price,payment,time,date, id))
	conn.commit()
	cursor.close()
	return render_template('home.html')

@app.route('/create_new_flight',methods=['GET','POST'])
def create_new_flight():

	
	username = session['username']

	flight_number = request.form['flight_number']
	airline = request.form['airline']
	departure_airport = request.form['departure_airport']
	departure_time = request.form['departure_time']
	departure_date = request.form['departure_date']
	arrival_airport= request.form['arrival_airport']
	arrival_time = request.form['arrival_time']
	arrival_date = request.form['arrival_date']
	base_price = request.form['base_price']
	flight_id = request.form['flight_id']
	status = request.form['status']

	cursor= conn.cursor()
	ins = 'INSERT INTO Flight VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)'
	cursor.execute(ins, (flight_number,airline, departure_airport, departure_time, departure_date,arrival_airport,arrival_time,arrival_date, base_price, flight_id, status))
	conn.commit()
	cursor.close()
	
	return render_template('createFlight.html',username = username)

@app.route('/add_new_airport',methods=['GET','POST'])
def add_new_airport():

	
	username = session['username']
	
	name = request.form['name']
	city = request.form['city']
	country = request.form['country']
	type = request.form['type']


	cursor= conn.cursor()
	ins = 'INSERT INTO Airport VALUES(%s, %s, %s)'
	cursor.execute(ins, (name,city, country,type))
	conn.commit()
	cursor.close()
	
	
	return render_template('add_airport.html',username = username)

@app.route('/update_status',methods=['GET','POST'])
def update_satus():

	
	username = session['username']

	flight_number = request.form['flight_number']
	status = request.form['status']
	cursor= conn.cursor()
	upd = 'UPDATE Flight STATUS = %s WHERE flight_number = %s'
	cursor.execute(upd, (status,flight_number))
	conn.commit()
	cursor.close()
	
	
	
	return render_template('update_status.html',username = username)

@app.route('/add_new_airplane',methods=['GET','POST'])
def add_new_airplane():

	username = session['username']

	airline_name = request.form['airline_name']
	airplane_id = request.form['airplane_id']
	number_of_seats = request.form['number_of_seats']
	manufac = request.form['manufac']
	age = request.form['age']

	cursor= conn.cursor()
	ins = 'INSERT INTO Airplane VALUES(%s, %s, %s, %s, %s)'
	cursor.execute(ins, (airline_name,airplane_id, number_of_seats, manufac, age))
	conn.commit()
	cursor.close()
	
	return render_template('add_airplane.html',username = username)

@app.route('/logout')
def logout():
	session.pop('customer_name')
	return redirect('/')
		
app.secret_key = 'e8630617f1484108fbabbd267dc0bb54'

#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)
