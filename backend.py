import sqlite3

def connect():
	conn=sqlite3.connect("jwl.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS jwl (id INTEGER PRIMARY KEY, name text, material text, type text, weight real, price real, purity real)")
	conn.commit()
	conn.close()

def insert(name,material,type,weight,price,purity):
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO jwl VALUES (NULL,?,?,?,?,?,?)",(name,material,type,weight,price,purity))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",material="",type="",weight="",price="",purity=""):
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE name=? OR material=? OR type=? OR weight=? OR price=? OR purity=?", (name,material,type,weight,price,purity))
    rows=cur.fetchall()
    conn.close()
    return rows

def g_search():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE material='gold' OR material = 'Gold' ")
    rows=cur.fetchall()
    conn.close()
    return rows

def d_search():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE material='diamond' OR material = 'Diamond' ")
    rows=cur.fetchall()
    conn.close()
    return rows

def s_search():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE material='silver' OR material = 'Silver' ")
    rows=cur.fetchall()
    conn.close()
    return rows

def e_search():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE type='earring' OR material = 'Earring' ")
    rows=cur.fetchall()
    conn.close()
    return rows

def r_search():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE type='ring' OR material = 'Ring' ")
    rows=cur.fetchall()
    conn.close()
    return rows

def n_search():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE type='necklace' OR material = 'Necklace' ")
    rows=cur.fetchall()
    conn.close()
    return rows

def b_search():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl WHERE type='bracelet' OR material = 'Bracelet' ")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM jwl WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,material,type,weight,price,purity):
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("UPDATE jwl SET name=?, material=?, type=?, weight=?, price=?, purity=? WHERE id=?",(name,material,type,weight,price,purity,id))
    conn.commit()
    conn.close()

def view_asc():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl ORDER BY price ASC")
    rows=cur.fetchall()
    conn.close()
    return rows

def view_desc():
    conn=sqlite3.connect("jwl.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jwl ORDER BY price DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()