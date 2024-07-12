from flask import Flask, render_template, flash, request, session, send_file from flask import render_template, redirect, url_for, request
# from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField from werkzeug.utils import secure_filename
import datetime
import mysql.connector


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize import nltk
import pandas as pd nltk.download('stopwords') nltk.download('punkt') import sys
app = Flask(_name_) app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/") def homepage():
return render_template('index.html')


@app.route("/AdminLogin") def AdminLogin():
return render_template('AdminLogin.html')


@app.route("/UserLogin") def UserLogin()
 
return render_template('UserLogin.html')


@app.route("/NewUser") def NewUser():
return render_template('NewUser.html')


@app.route("/AdminHome") def AdminHome():
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM regtb ") data = cur.fetchall()
return render_template('AdminHome.html', data=data)


@app.route("/NewProduct") def NewProduct():
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM protb ") data = cur.fetchall()
return render_template('NewProduct.html', data=data)


@app.route("/AProductInfo") def AProductInfo():
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM protb ")
 
data = cur.fetchall()
return render_template('AProductInfo.html', data=data)


@app.route("/msearch", methods=['GET', 'POST']) def msearch():
if request.method == 'POST':
if request.form["submit"] == "Search": Cname = request.form['Cname'] #import matplotlib.pyplot as plt #import matplotlib #matplotlib.use('Agg')
#conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
#mycursor = conn.cursor() # mycursor.execute(
# "select ProductType, sum(Qty) as Qty from protb where CompanyName='" + Cname + "' group by ProductType ")
#result = mycursor.fetchall #Month = []
#MSales = [] #Month.clear() #MSales.clear() #for i in mycursor:
#Month.append(i[0]) #MSales.append(i[1])
#print("ProductType = ", Month) #print("Quantity = ", MSales)
# Visulizing Data using Matplotlib
#plt.bar(Month, MSales, color=['yellow', 'red', 'green', 'blue', 'cyan']) # plt.ylim(0, 5)
#ax = plt.gca() #plt.draw()
#ax.tick_params(axis='x', rotation=70)
 
#plt.xlabel("Type") #plt.ylabel("Total Product") #plt.title("Quantity") #import random
#n = random.randint(1111, 9999) #plt.savefig('static/plott/' + str(n) + '.jpg') #iimg = 'static/plott/' + str(n) + '.jpg' #print()
#plt.show()
import pandas as pd
import matplotlib.pyplot as plt
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
query = "select ProductType, sum(Qty) as Qty from protb where CompanyName='" + Cname + "' group by ProductType"
result_dataFrame = pd.read_sql(query, conn) result_dataFrame.head() print(result_dataFrame.head())
fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144) colors = plt.cm.Dark2(range(16))
y = result_dataFrame['ProductType'] width = result_dataFrame['Qty'] ax.barh(y=y, width=width, color=colors); plt.show()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor() cur.execute(
"SELECT * FROM protb where CompanyName='" + Cname + "' ") data = cur.fetchall()
return render_template('AProductInfo.html', data=data)


@app.route("/dsearch", methods=['GET', 'POST'])
 
def dsearch():
if request.method == 'POST':
if request.form["submit"] == "Search": sdate = request.form['sdate']
edate = request.form['edate'] import matplotlib.pyplot as plt import matplotlib #matplotlib.use('Agg')
#conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
#mycursor = conn.cursor() #mycursor.execute(
#"select ProductName, sum(Qty) as Qty from booktb where date between '" + sdate
+ "' and '"+ edate +"' group by ProductName ") #result = mycursor.fetchall
#Month = [] #MSales = [] #Month.clear() #MSales.clear() #for i in mycursor:
#Month.append(i[0]) #MSales.append(i[1])
#print("ProductName = ", Month) #print("Quantity = ", MSales)
# Visulizing Data using Matplotlib #plt.figure()
#plt.bar(MSales,Month, color=['yellow', 'red', 'green', 'blue', 'cyan']) # plt.ylim(0, 5)
#ax = plt.gca() #plt.draw()
#ax.tick_params(axis='y', rotation=90) #plt.xlabel("Quantity")
#plt.ylabel(" TotalProduct")
 
#plt.title("ProductName") #plt.legend()
#plt.show() #import random
#n = random.randint(1111, 9999) #plt.savefig('static/plott/' + str(n) + '.jpg') #iimg = 'static/plott/' + str(n) + '.jpg' #print()
#plt.close()
import pandas as pd
import matplotlib.pyplot as plt
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
query = "select ProductName, sum(Qty) as Qty from booktb where date between '" + sdate + "' and '"+ edate +"' group by ProductName"
result_dataFrame = pd.read_sql(query, conn) result_dataFrame.head() print(result_dataFrame.head())
fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144) colors = plt.cm.Dark2(range(16))
y = result_dataFrame['ProductName'] width = result_dataFrame['Qty'] ax.barh(y=y, width=width, color=colors); plt.show()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor() cur.execute(
"SELECT * FROM booktb where date between '" + sdate + "' and '"+ edate +"' ") data = cur.fetchall()
return render_template('ABookInfo.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
 
def adminlogin(): error = None
if request.method == 'POST':
if request.form['uname'] == 'admin' and request.form['password'] == 'admin': conn = mysql.connector.connect(user='root', password='', host='localhost',
database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM regtb ") data = cur.fetchall()
return render_template('AdminHome.html', data=data) else:
alert = 'Username or Password is wrong'
return render_template('goback.html', data=alert)


@app.route("/newproduct1", methods=['GET', 'POST']) def newproduct1():
if request.method == 'POST': # cname = session['Cname']
Cname = request.form['Cname'] Ptype = request.form['Ptype'] Pname = request.form['Pname'] color = request.form['color'] price = request.form['price'] Uvideo = request.form['Uvideo'] spec = request.form['spec']
file = request.files['file']
file.save("static/upload/" + secure_filename(file.filename))
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
 
"INSERT INTO protb VALUES ('','" + Cname + "','" + Ptype + "','" + Pname + "','" +
color + "','" + price + "','" + Uvideo + "','" + spec + "','" + file.filename + "')") conn.commit()
conn.close()
alert = 'Product register successfully'
return render_template('goback.html', data=alert)


@app.route("/newproduct", methods=['GET', 'POST']) def newproduct():
if request.method == 'POST':
if request.form["submit"] == "Submit": Cname = request.form['Cname'] Ptype = request.form['Ptype']
Pname = request.form['Pname'] color = request.form['color'] price = request.form['price'] Uvideo = request.form['Uvideo'] spec = request.form['spec']
Qty = request.form['Qty']
tprice = float(Qty) * float(price) file = request.files['file']
file.save("static/upload/" + file.filename)
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"INSERT INTO protb VALUES ('','" + Cname + "','" + Ptype + "','" + Pname + "','"
+ color + "','" + price + "','" + Uvideo + "','" + spec + "','" + file.filename + "','"+ str(Qty)
+"','"+ str(tprice) +"')")
conn.commit() conn.close()
alert = 'Product register successfully'
return render_template('goback.html', data=alert)
 
elif request.form["submit"] == "Update": Pid = request.form['Pid']
Cname = request.form['Cname'] Ptype = request.form['Ptype'] Pname = request.form['Pname'] color = request.form['color'] price = request.form['price'] Uvideo = request.form['Uvideo'] spec = request.form['spec']
Qty = request.form['Qty']
tprice = float(Qty) * float(price)
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"update protb set CompanyName ='" + Cname + "',ProductType='" + Ptype + "',ProductName='" + Pname + "',Color='" + color + "',Price='" + price + "',VideoUrl='" + Uvideo + "',Specifications='" + spec + "',Qty='"+ str(Qty) +"',Tprice='"+ str(tprice) +"' where id='" + Pid + "' ")
conn.commit() conn.close()
alert = 'Record Updated!'
return render_template('goback.html', data=alert) elif request.form["submit"] == "Search":
Pid = request.form['Pid']
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM protb where id='" + Pid + "' ") data = cur.fetchone()
if data:
pid = data[0] Cname = data[1]
 
Ptype = data[2] Pname = data[3] color = data[4] price = data[5] Uvideo = data[6] spec = data[7] Qty = data[9]
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM protb ") data = cur.fetchall()
return render_template('Newproduct.html', Pid=pid, Cname=Cname, Ptype=Ptype, Pname=Pname, color=color, price=price, Uvideo=Uvideo, spec=spec)
else:
return 'Incorrect username / password !' elif request.form["submit"] == "Delete":
Pid = request.form['Pid']
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"delete from protb where id='" + Pid + "' ") conn.commit()
conn.close()
alert = 'Record Deleted!'
return render_template('goback.html', data=alert) return render_template('goback.html')

@app.route("/newuser", methods=['GET', 'POST']) def newuser():
if request.method == 'POST':
 
name1 = request.form['name'] gender1 = request.form['gender'] Age = request.form['age']
email = request.form['email'] pnumber = request.form['phone'] address = request.form['address'] uname = request.form['uname'] password = request.form['psw']
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"INSERT INTO regtb VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" +
email + "','" + pnumber + "','" + address + "','" + uname + "','" + password + "')") conn.commit()
conn.close()
# return 'file register successfully' return render_template('UserLogin.html')

@app.route("/userlogin", methods=['GET', 'POST']) def userlogin():
error = None
if request.method == 'POST': username = request.form['uname'] password = request.form['password']
session['uname'] = request.form['uname']
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor()
cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
data = cursor.fetchone() if data is None:
 
alert = 'Username or Password is wrong'
return render_template('goback.html', data=alert) else:
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
data = cur.fetchall()
return render_template('UserHome.html', data=data) def recommend():
# 'Recommend' neg = 0
pas = 0
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute("Truncate table temptb") conn.commit()
conn.close()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor()
cur.execute("SELECT Distinct ProductId,Image,ProductName,Price FROM reviewtb where Result='Postive' ")
data1 = cur.fetchall() for row in data1:
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"SELECT count(*) as count FROM reviewtb WHERE ProductId ='" + row[0] + "' and Result='Postive'  ")
 
data2 = cursor.fetchone() if data2:
pas = data2[0] else:
pas = 0
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"SELECT count(*) as count FROM reviewtb WHERE ProductId ='" + row[0] + "' and Result='negative'  ")
data3 = cursor.fetchone() if data3:
neg = data3[0] else:
neg = 0
if pas >= neg:
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor() cur.execute(
"SELECT ProductId,CompanyName,ProductType,ProductName,Price,Image FROM reviewtb where ProductId  ='" +
row[0] + "' ")
data22 = cur.fetchone() if data22:
s1 = data22[0] s2 = data22[1] s3 = data22[2] s4 = data22[3] s5 = data22[4] s6 = data22[5]
else:
 
neg = 0
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"insert into temptb values('" + s1 + "','" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "')")
conn.commit() conn.close()

@app.route("/Search") def Search():
recommend()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor() cur.execute("SELECT * FROM protb ") data = cur.fetchall()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor()
cur.execute("SELECT ProductId,Image,ProductName,Price FROM temptb ") data1 = cur.fetchall()
return render_template('Search.html', data=data, data1=data1)


@app.route("/typesearch", methods=['GET', 'POST']) def typesearch():
cname = request.form['Cname'] ptype = request.form['Ptype']
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor()
cursor.execute("SELECT * from protb where CompanyName='" + cname + "' and ProductType='" + ptype + "'")
 
data = cursor.fetchone() if data is None:
alert = 'Product Not Found!'
return render_template('goback.html', data=alert) else:
recommend()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor()
cur.execute("SELECT * FROM protb where CompanyName='" + cname + "' and ProductType='" + ptype + "' ")
data = cur.fetchall()
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor() cur.execute(
"SELECT ProductId,Image,ProductName,Price FROM temptb where CompanyName='" + cname + "' and ProductType='" + ptype + "' ")
data1 = cur.fetchall()
return render_template('Search.html', data=data, data1=data1)


@app.route("/fullInfo") def fullInfo():
pid = request.args.get('pid') session['pid'] = pid
rat1 = '' rat2 = '' rat3 = '' rat4 = '' rat5 = ''
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
 
"SELECT ROUND(AVG(Rate), 1) as numRating FROM reviewtb WHERE ProductId
='" + pid + "' ")
data2 = cursor.fetchone() print(data2[0])
if data2 is None: avgrat = 0
else:
if data2[0] == 'None': avgrat = 0
if (int(avgrat) == 1): rat1 = 'checked'
if (int(avgrat) == 2): rat2 = 'checked'
if (int(avgrat) == 3): rat3 = 'checked'
if (int(avgrat) == 4): rat4 = 'checked'
if (int(avgrat) == 5): rat5 = 'checked'
else:
avgrat = data2[0] if (avgrat == 1):
rat1 = 'checked' if (avgrat == 2):
rat2 = 'checked' if (avgrat == 3):
rat3 = 'checked' if (avgrat == 4):
rat4 = 'checked' if (avgrat == 5):
rat5 = 'checked'
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
 
cursor = conn.cursor() cursor.execute(
"SELECT count(Rate) as numRating FROM reviewtb WHERE ProductId ='" + pid +
"' ")
data3 = cursor.fetchone() if data3:
avgrat = data3[0] else:
return 'Incorrect username / password !'
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"SELECT sum(Smile1) as count1,sum(Smile2) as count2, sum(Smile3) as count3, sum(Smile4) as count4, sum(Smile5) as count5, sum(Smile6) as count6 FROM reviewtb where ProductId='" + pid + "' ")
data = cursor.fetchone() if data:
smile1 = data[0] smile2 = data[1] smile3 = data[2] smile4 = data[3] smile5 = data[4] smile6 = data[5]
else:
return 'Incorrect username / password !'
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor()
cur.execute("SELECT UserName,Review FROM reviewtb where ProductId='" + pid + "'
")
reviewdata = cur.fetchall()
conn = mysql.connector.connect(user='root', password='', host='localhost',
database='4productrecomdb')
 
cur = conn.cursor()
cur.execute("SELECT * FROM protb where id='" + pid + "' ") data1 = cur.fetchall()
return render_template('ProductFullInfo.html', data=data1, avgrat=avgrat, rat1=rat1, rat2=rat2, rat3=rat3, rat4=rat4, rat5=rat5, smile1=smile1, smile2=smile2, smile3=smile3, smile4=smile4, smile5=smile5, smile6=smile6, reviewdata=reviewdata)


@app.route("/Book", methods=['GET', 'POST']) def Book():
if request.method == 'POST':
from uuid import getnode as get_mac # mac = get_mac()
uname = session['uname'] pid = session['pid']
qty = request.form['qty'] ctype = request.form['ctype']
cardno = request.form['cardno'] cvno = request.form['cvno'] Bookingid = ''
ProductName = '' UserName = uname Mobile = ''
Email = '' Qty = qty Amount = ''
Mac = get_mac() CardType = ctype CardNo = cardno CvNo = cvno import datetime
date = datetime.datetime.now().strftime('%Y-%m-%d')
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
 
cursor = conn.cursor()
cursor.execute("SELECT * FROM protb where id='" + pid + "'") data = cursor.fetchone()
if data:
ProductName = data[3] price = data[5]
Amount = float(price) * float(Qty) print(Amount)
else:
return 'Incorrect username / password !'
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor()
cursor.execute("SELECT * FROM regtb where UserName='" + uname + "'") data = cursor.fetchone()
if data:
Mobile = data[4] Email = data[3]
else:
return 'Incorrect username / password !'
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor()
cursor.execute("SELECT count(*) as count FROM booktb ") data = cursor.fetchone()
if data:
count = data[0] if count == 0:
count = 1; else:
count += 1
else:
return 'Incorrect username / password !'
 
print(count)
Bookingid = "BOOKID00" + str(count)
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"INSERT INTO booktb VALUES ('','" + Bookingid + "','" + pid + "','" + ProductName + "','" + uname + "','" + Mobile + "','" + Email + "','" + Qty + "','" + str(
Amount) + "','" + str(Mac) + "','" + CardType + "','" + CardNo + "','" + CvNo + "','"
+ date + "')")
conn.commit() conn.close()
# return 'file register successfully'
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cur = conn.cursor()
cur.execute("SELECT * FROM booktb where UserName= '" + uname + "' ") data = cur.fetchall()
return render_template('UbookInfo.html', data=data) @app.route("/NewReview")
def NewReview():
from uuid import getnode as get_mac Mac = get_mac()
return render_template('NewReview.html', mac=Mac)


@app.route("/ureview", methods=['GET', 'POST']) def ureview():
if request.method == 'POST':
from uuid import getnode as get_mac


feedr = 0
starr = 0
emojr = 0
 
result = ''
bookid = request.form['bookid'] email = request.form['email'] Mac = get_mac()
star = request.form['star'] emoj = request.form['ar'] uname = session['uname']
feedback = request.form['feed'] sta = 0
example_sent = feedback
stop_words = set(stopwords.words('english')) word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words] filtered_sentence = []
for w in word_tokens:
if w not in stop_words: filtered_sentence.append(w)
print(word_tokens) print(filtered_sentence) def listToString(s):
# initialize an empty string str1 = " "
# return string return (str1.join(s))
# Driver code
s = filtered_sentence print(listToString(s)) sentence = listToString(s)
s11 = listToString(word_tokens) print('	')
print(s11)
 
d = ["careless", "together", "criminal", "corrupt", "depressed", "Overcritical", "Aggressive","Armchair","critic", "Cynical", "Impulsive", "Tactless", "Thoughtless", "badmood", "hurtful", "lose","lousy", "lumpy", "naive", "nasty", "naughty", "negate",
"negative", "never", "nobody", "non","descript", "noxious", "sad", "stupid", "stressful",
"upset", "worthless", "zero", "ugly","undermine","unfair", "unfavorable", "unhappy", "unhealthy", "not+good"]
s1 = set(sentence.split()) s2 = set(d)
s111 = set(s11.split()) print(s1.intersection(s2)) print(len(s1.intersection(s2))) cn = len(s111.intersection(s2)) print(cn)
feed = [] feed.append(feedback) sentence1 = feed print(sentence1)
def check_all(sentence1, ws):
return all(w in sentence1 for w in ws) for sentences in sentence1:
if any(check_all(sentences, word.split('+')) for word in d): print(sentence1)
sta = 'negative' break
else:
print('not fount') sta = "positive" break
# print(sta)
if str == 'positive': feedr = 0
else:
feedr = 1
if (int(star) > 2):
 
starr = 1 else:
starr = 0
if (int(emoj) >= 3): emojr = 1
else:
emojr = 0
total = int(feedr) + int(starr) + int(emojr) if (total > 1):
result = 'Postive' else:
result = 'negative' print(result)
em1 = 0
em2 = 0
em3 = 0
em4 = 0
em5 = 0
em6 = 0
if (int(emoj) == 6): em1 = 1
if (int(emoj) == 5): em2 = 1
if (int(emoj) == 4): em3 = 1
if (int(emoj) == 3): em4 = 1
if (int(emoj) == 2): em5 = 1
if (int(emoj) == 1): em6 = 1
print(em1, em2, em3, em4, em5, em6)
 
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"SELECT * FROM booktb where Bookingid='" + bookid + "' and Email='" + email
+ "' and Mac='" + str(
Mac) + "'")
data = cursor.fetchone() if data:
proid = data[2]
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor()
cursor.execute("SELECT * FROM protb where id='" + proid + "'") data = cursor.fetchone()
if data:
cname = data[1] ptype = data[2] pname = data[3] price = data[5] img = data[8]
else:
alert = 'No Record Found!'
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"SELECT * FROM reviewtb where Bookid='" + bookid + "' and Email='" + email + "' and MacAddress='" + str(
Mac) + "'")
data = cursor.fetchone() if data:
alert = 'Already Your Review Enter This Product' return render_template('goback.html', data=alert)
 
else:
print(proid)
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
cursor = conn.cursor() cursor.execute(
"INSERT INTO reviewtb VALUES ('','" + str(proid) + "','" + str(cname) + "','" +
 
str(






"','" + str(








else:
 

ptype) + "','" + str(pname) + "','" + str(price) + "','" + str(img) + "','" + str( bookid) + "','" + str(email) + "','" +
str(Mac) + "','" + str(uname) + "','" + str(star) + "','" + str(feedback) + "','" + str(
em1) + "','" + str(em2) + "','" + str(em3) + "','" + str(em4) + "','" + str(em5) +

em6) + "','" + str(result) + "')") conn.commit()
conn.close()
alert = 'Review Enter Successfully'
return render_template('goback.html', data=alert)
 
alert = 'No Record Found'
return render_template('goback.html', data=alert) @app.route("/UBookInfo")
def UBookInfo():
uname = session['uname']
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM booktb where UserName='" + uname + "' ") data = cur.fetchall()
return render_template('UBookInfo.html', data=data)


@app.route("/ABookInfo")
 
def ABookInfo():
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor()
cur.execute("SELECT * FROM booktb ") data = cur.fetchall()
return render_template('ABookInfo.html', data=data)


@app.route("/UReviewInfo") def UReviewInfo():
uname = session['uname']
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor() cur = conn.cursor() cur.execute(
"SELECT Bookid,ProductId,ProductName,UserName,MacAddress,Rate,Review FROM reviewtb where UserName='" + uname + "'  ")
data = cur.fetchall()
return render_template('UReviewInfo.html', data=data)


@app.route("/AReviewInfo") def AReviewInfo():
conn = mysql.connector.connect(user='root', password='', host='localhost', database='4productrecomdb')
# cursor = conn.cursor()
cur = conn.cursor() cur.execute("SELECT
Bookid,ProductId,ProductName,UserName,MacAddress,Rate,Review FROM reviewtb ") data = cur.fetchall()
return render_template('AReviewInfo.html', data=data) if _name_ == '_main_':
app.run(debug=True, use_reloader=True)
