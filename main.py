
import pandas as pd
from flask import Flask
app=Flask(__name__)


@app.route("/")
def cfsdata():
    cfs=pd.read_excel('C:\\Users\\angel_paul\\Documents\\cfs_trial.xlsx')
    return cfs.to_html()

if __name__=="__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)