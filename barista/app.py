from flask import *
from coffee import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', coffees=COFFEES, machines=MACHINES)

@app.route("/coffee")
def coffee():
    amount = int(request.args.get('amount'))
    coffee = int(request.args.get('coffee'))
    machine = int(request.args.get('machine'))

    order = make_coffee(amount, COFFEES[coffee], MACHINES[machine])
    
    return render_template('coffee.html', order=order)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
