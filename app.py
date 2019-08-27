from flask import Flask, render_template, request, jsonify
from Stocks import StockCalculation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/_background_process')
def background_process():
    Balance = request.args.get('amount', 0)
    YearStart = request.args.get('beginning', 0)
    NumbOfYears = request.args.get('years', 0)
    try:
        Balance = float(Balance)
    except:
        ScriptResult = "Your initial balance must be a valid number of dollars, such as 1000 or 15354.46"
        return jsonify(result=ScriptResult)
    try:
        YearStart = int(YearStart)
    except:
        ScriptResult = "Your starting year must be a whole number, such as 1940"
        return jsonify(result=ScriptResult)
    try:
        NumbOfYears = int(NumbOfYears)
    except:
        ScriptResult = "The number of years you withdraw from your funds must be a whole number, such as 30"
        return jsonify(result=ScriptResult)
    ScriptResult = StockCalculation(Balance,YearStart,NumbOfYears)
    return jsonify(result=ScriptResult)
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)