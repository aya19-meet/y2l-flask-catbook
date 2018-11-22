from flask import *
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_id>', methods=['GET', 'POST'])
def cat_details(cat_id):
if request.method == 'GET':
	cat = get_cat(cat_id)
	return render_template("cat.html", cat=cat)
else:
	def vote(id):
	vote(id)
	cat = get_cat(cat_id)
	return render_template("cat.html", cat=cat)
	# return redirect('/')



# @app.route('/vote_cat/<int:cat_id>', methods=['POST'])
# def vote(id):
# 	vote(id)
# 	return redirect('/')


@app.route('/add_cat', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET': 
        return render_template('addcat.html')
    else:
        name = request.form['name']
        create_cat(name)        
        return render_template('response.html',
            name = name)

if __name__ == '__main__':
   app.run(debug = True)
