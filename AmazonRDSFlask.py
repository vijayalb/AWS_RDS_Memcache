from flask import Flask, render_template
import pymysql
from flask import request
import time
import memcache

app = Flask(__name__)

conn = pymysql.connect(host="aws-rds-cloud.cyojiua7ocnj.us-west-2.rds.amazonaws.com", database="RDSCloud",
                               user="vijayalb6", password="*******")
mc = memcache.Client(['aws-memcached-cloudt.hzr8cf.cfg.usw2.cache.amazonaws.com:11211'], debug=1)


@app.route('/')
def Welcome():
    return render_template('awsrds.html')


@app.route('/execute', methods=['POST', 'GET'])
def execute():
    sql = str(request.form['my_query'])
    command = sql + ' LIMIT 1'
    ukey = str(request.form['key'])
    rows_no_parameter = []
    cursor = conn.cursor()
    mcobj = mc.get(ukey)
    if not mcobj:
        start_time = time.time()
        for i in range(5000):
            cursor.execute(command)
            cursor.execute("SELECT NAME FROM RDSCloud.FeedGrains WHERE `SC_GroupCommod_ID` > " + i)
            rows_no_parameter.append(cursor.fetchall())
        mc.set(ukey, rows_no_parameter)
        print (len(rows_no_parameter))
        return "Time taken without Memcache (in seconds): " + str(time.time() - start_time)
    start_time = time.time()
    mcobj = mc.get(ukey)
    return "Time taken using Memcache (in seconds): " + str(time.time() - start_time)

if __name__ == '__main__':
    app.run(debug=True)


