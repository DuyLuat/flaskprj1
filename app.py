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