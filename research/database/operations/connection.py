import psycopg2

hostname = 'localhost'
username = 'demo'
passwd =  'admion1234'
port_id= 4435
conn=None
cur=None

try:
    conn= psycopg2.connect(
        host=hostname,  
        user=username,
        dbname='demo',
        password=passwd,
        port= port_id)
    
    cur= conn.cursor()
    curr.execute('DROP TABLE IF EXISTS employee')

    create_script = '''CREATE TABLE IF NOT EXISTS employee(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        department VARCHAR(100) NOT NULL
    )'''

    cur.execute(create_script)

    insert_script = '''INSERT INTO employee(name, age, department) VALUES(%s, %s, %s)'''
    insert_values = [('John Doe', 30, 'HR'),
                     ('Jane Doe', 25, 'IT'),
                     ('James Smith', 35, 'Finance'),
                     ('Judy Smith', 40, 'Operations')]
    
    for record in insert_values:
        cur.execute(insert_script, record)

    curr.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        print(record)

    


    cur.executemany(insert_script, insert_values)   
    conn.commit()



    cur.close()
    conn.close()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    conn.close()
