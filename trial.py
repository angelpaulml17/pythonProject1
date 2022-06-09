# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template, request, make_response
from openpyxl import load_workbook

# (A2) FLASK SETTINGS + INIT
HOST_NAME = "127.0.0.1"
HOST_PORT = 5000
app = Flask(__name__)


# app.debug = True

# (B) DEMO - READ EXCEL & GENERATE HTML TABLE
@app.route("/")
def index():
    # (B1) OPEN EXCEL FILE + WORKSHEET
    book = load_workbook("cfs_trial.xlsx")
    sheet = book.active

    # (B2) PASS INTO HTML TEMPLATE
    return render_template("trial.html", sheet=sheet)


# (C) START
if __name__ == "__main__":
    app.debug = True
    app.run(HOST_NAME, HOST_PORT)