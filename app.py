from flask import Flask, escape, request, render_template, redirect, url_for, flash
import pymysql

db = pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='test',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)

@app.route('/')
def index():
   cur = db.cursor()
   sql = "SELECT * FROM users"
   cur.execute(sql)
   results = cur.fetchall()
   cur.close()
   return render_template('index.html', results=results)


@app.route('/delete/<int:id>')
def delete(id):
   cur = db.cursor()
   sql = "delete FROM users where id=%s"
   cur.execute(sql,(id))
   db.commit()
   return redirect(url_for('index'))


@app.route('/one')
def one():
  
   cur = db.cursor()
   sql = "SELECT * FROM users"
   cur.execute(sql)
   result = cur.fetchone()
   cur.close()
   return render_template('one.html', result=result)

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
   if request.method =='POST':
      firstname=request.form['firstname']
      lastname=request.form['lastname']
      email=request.form['email']
      cur = db.cursor()
      sql = 'update users set firstname=%s, lastname=%s, email=%s where id=%s'
      cur.execute(sql, (firstname, lastname, email, id))
      db.commit()
      cur.close()
      return redirect(url_for('index'))
   else:
      cur = db.cursor()
      sql = "SELECT * FROM users where id=%s"
      cur.execute(sql, id)
      result = cur.fetchone()
      return render_template('update.html', result=result)

@app.route('/adduser', methods=['POST', 'GET'])
def adduser():
   if request.method =='POST':
      firstname=request.form['firstname']
      lastname=request.form['lastname']
      email=request.form['email']
      cur = db.cursor()
      sql = "INSERT INTO users(firstname, lastname, email) VALUES (%s, %s, %s)"
      cur.execute(sql, (firstname, lastname, email))
      cur.close()
      return redirect(url_for('index'))
   else:
      return render_template('adduser.html')
