from flask import *
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:cat_id>')
def cat_details(cat_id):
	cat = get_cat(cat_id)
	return render_template("cat.html", cat=cat)


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
