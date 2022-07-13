# (A) INIT
# (A1) LOAD MODULES
import itertools

from flask import Flask, render_template, request, make_response, json
from openpyxl import load_workbook
import pyodbc
import pandas as pd
cnxn=pyodbc.connect('Driver={SQL Server};Server=10.174.98.220;Database=IP_ANALYTICS;Trusted_Connection=yes')
cursor=cnxn.cursor()
# cursor.execute('select top 100 transaction_data_source,major_account_id,major_account_name from dbo.unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')

cursor.execute('select top 100 transaction_data_source,major_account_id,major_account_name,cost_center,set_of_books_name,invoice_number,invoice_description,invoice_date , invoice_source,spend_usd,po_number,po_description,paid_date, spend_category_id,spend_category_L1,spend_category_L2,spend_category_L3,supplier_number,supplier_name,parent_supplier,mopm,COMMODITY_TYPE,Fiscal_Month,Fiscal_Quartr,Fiscal_Year, L1_CLASSIFICATION , L2_CLASSIFICATION , L3_CLASSIFICATION from dbo.unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
records=cursor.fetchall()
cursor.execute('select distinct transaction_data_source from unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
transaction_source=cursor.fetchall()
#print(records)
# (A2) FLASK SETTINGS + INIT
HOST_NAME = "127.0.0.1"
HOST_PORT = 5000
app = Flask(__name__)


# app.debug = True

# (B) DEMO - READ EXCEL & GENERATE HTML TABLE
@app.route("/")
def index():
    # (B1) OPEN EXCEL FILE + WORKSHEET
    # book = load_workbook("cfs_trial.xlsx")
    # sheet = book.active
    # print(sheet)
    # (B2) PASS INTO HTML TEMPLATE
    cursor1 = cnxn.cursor()
    cursor1.execute('select distinct new_l1, new_l2, new_l3 from dbo.legacy_mopm ')
    portfolios = cursor1.fetchall()


    #print(list(portfolios))
    # id_list = []
    # for index in range(len(portfolios)):
    #     id_list.append(portfolios[index][0])
    ans=list(itertools.chain.from_iterable(portfolios))
    res=[]

    for j in range(0, len(ans), 3):
        res2=[]
        for i in range(0,3, 1):
            res2.append(ans[j+i])
        res.append((res2))
    print(len(res))

    ans1 = list(itertools.chain.from_iterable(transaction_source))
    transaction_source1 = []

    for j in range(0, len(ans1)):
        transaction_source1.append((ans1[j]))
    print(transaction_source1)

    cursor1 = cnxn.cursor()
    cursor1.execute('select distinct major_Account_id from unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
    majoracc = cursor1.fetchall()
    ma = list(itertools.chain.from_iterable(majoracc))
    maacc = []
    print(ma)
    for j in range(0, len(ma)):
        if ma[j] != None:
            maacc.append((ma[j]))
    print(len(maacc))

    cursor1 = cnxn.cursor()
    cursor1.execute('select distinct major_Account_name from unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
    majoraccname = cursor1.fetchall()
    maname = list(itertools.chain.from_iterable(majoraccname))
    maaccn = []
    for j in range(0, len(maname)):
        if maname[j] != None:
            maaccn.append((maname[j]))
    print(maaccn)
    #
    # cursor2 = cnxn.cursor()
    # cursor2.execute(
    #     'select distinct cost_center from unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
    # CostCenter = cursor2.fetchall()
    # maname = list(itertools.chain.from_iterable(CostCenter))
    # CostCenter1 = []
    # for j in range(0, len(maname)):
    #     if CostCenter[j] != None:
    #         CostCenter1.append((CostCenter[j]))
    #
    #
    # print(CostCenter1)
    # cursor1 = cnxn.cursor()
    # cursor1.execute(
    #     'select distinct set_of_books_name from unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
    # set_of_books_name = cursor1.fetchall()
    # maname = list(itertools.chain.from_iterable(set_of_books_name))
    # set_of_books_name1 = []
    # for j in range(0, len(maname)):
    #     if set_of_books_name[j] != None:
    #         set_of_books_name1.append((set_of_books_name[j]))
    #
    # cursor1 = cnxn.cursor()
    # cursor1.execute(
    #     'select distinct Invoice_Number from unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
    # InvoiceNumber = cursor1.fetchall()
    # maname = list(itertools.chain.from_iterable(InvoiceNumber))
    # InvoiceNumber1 = []
    # for j in range(0, len(maname)):
    #     if InvoiceNumber[j] != None:
    #         InvoiceNumber1.append((InvoiceNumber[j]))
    #
    # cursor1 = cnxn.cursor()
    # cursor1.execute(
    #     'select distinct Invoice_Description from unified_spend where fiscal_month=\'M04: MayFY23\' and transaction_data_source =\'Dell_Portfolio\' or transaction_data_source =\'emc_Portfolio\'')
    # InvoiceDescription = cursor1.fetchall()
    # maname = list(itertools.chain.from_iterable(InvoiceDescription))
    # InvoiceDescription1 = []
    # for j in range(0, len(maname)):
    #     if InvoiceDescription[j] != None:
    #         InvoiceDescription1.append((InvoiceDescription[j]))

    return render_template("base.html", records=records, res=res, transaction_source=transaction_source1,major_account=maacc, major_name=maaccn)
    #return render_template("base.html", records=records, res=res, transaction_source=transaction_source1, major_account=maacc, major_name=maaccn, CostCenter=CostCenter1, set_of_books_name=set_of_books_name1, InvoiceNumber=InvoiceNumber1, InvoiceDescription=InvoiceDescription1)

@app.route("/rest", methods=['POST'])
def rest():
    output = request.get_json()
    print(output)  # This is the output that was stored in the JSON within the browser
    print(type(output))
    result = json.loads(output)  # this converts the json output to a python dictionary
    print(result)  # Printing the new dictionary
    print(type(result))  # this shows the json converted as a python dictionary
    str=""
    for key in result:
        inner=""
        # inner=key+"=\""+result[key]+"\" and "
        # print(inner)
        str+=key+"=\'"+result[key]+"\' and "
    # print(str.removesuffix("and"))
    sstring="and"
    reso=''
    # if str.endswith(sstring):
    #     reso = str[:-(len(sstring))]
    print(str[:-(len("and")+1)])
    reso=str[:-(len("and")+1)]
    print(reso)
    cursor2 = cnxn.cursor()
    query='select sum(spend_usd) from dbo.unified_spend where '+ reso
    print (query)
    cursor2.execute(query)
    spend = cursor2.fetchall()
    sp=[float(d[0]) for d in spend]
    # print(sp)
    #print(int(spend[0]))
    return json.dumps(sp)


if __name__ == "__main__":
    app.debug = True
    app.run(HOST_NAME, HOST_PORT)