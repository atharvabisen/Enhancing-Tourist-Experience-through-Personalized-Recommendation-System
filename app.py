# importing Flask and other modules
from flask import Flask, request, render_template
import mysql.connector
import pandas as pd

from naive_bayes import naive_bayes_algo
from places import find_places
from source_to_destination import src_to_dis
from tsp import tsp
from nested_list_to_list import flat
from display_map import display

app = Flask(__name__,template_folder='templates')

# Connect to MySQL
cnx = mysql.connector.connect(user='root', password='atharva',
                                  host='localhost',
                                  database='userhistory',
                                  auth_plugin = 'mysql_native_password')

bnx = mysql.connector.connect(user='root', password='atharva',
                                  host='localhost',
                                  database='user',
                                  auth_plugin = 'mysql_native_password')


@app.route('/')
def index():
    return render_template("Registration Page.html")

@app.route('/register')
def register():
    return render_template("login.html")

@app.route('/login',methods=['POST','GET'])
def login():
    msg = ''
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        cursor = bnx.cursor()
        cursor.execute('SELECT * FROM user WHERE username=%s AND password=%s',(username,password))
        record = cursor.fetchone()
        if record:
            return render_template("Hobby Page.html")
        else:
            msg = 'Incorrect username/password. Try Again!'
            return msg

# Route for processing form submission
@app.route('/process_form', methods=['POST','GET'])
def result():
    mood_1 = request.form.get('mood')
    age_1 = request.form.get('age')
    qualification_1 = request.form.get('qualification')
    gender_1 = request.form.get('gender')
    hobby_1 = request.form.get('hobby')
    budget_1 = request.form.get('budget')
    climate_1 = request.form.get('climate')
    address = request.form['current location']
    selected_chips = request.form.getlist('area_of_interest')
    selected_chips = selected_chips[0].split(',')
    #return render_template('selected.html', chips=selected_chips, mood=mood_1, age=age_1,gender=gender_1)

    # Execute a query (Fetching rows from MySQL)
    cursor = cnx.cursor()
    query = ("SELECT * FROM history")
    cursor.execute(query)
    rows = cursor.fetchall()

    # Close the connection
    cursor.close()

    # Convert rows to a Pandas dataframe
    df = pd.DataFrame(rows, columns=['Mood', 'Age', 'Qualification', 'Gender','Hobby',
                                     'Budget','Climate','Area_of_Interest'])
    #print(df)
    nb_result = naive_bayes_algo(mood_1,age_1,qualification_1,
                              gender_1,hobby_1,budget_1,climate_1,df)
    
    # Places to recommend (Recommendation Algo)
    places = find_places(nb_result[1],selected_chips)
    places = flat(places)

    #Printing the places to be recommended
    print(places)

    # source has d-matrix row. A list that contains the distance from users current address to list of places to recommend.  
    source = src_to_dis(address, places)


    order_path = tsp(places, source, address)

    # Return the query results
    #return str(rows)
    result = display(order_path)
    print(result)

    # Inserting into User history database
    categories = {"Historical":"H1", "Religious":"H2", "Wildlife":"H3", "Adventure":"H4", "Shopping":"H5"}
    areas_of_interest = []
    areas_of_interest.append(nb_result[1])
    for i in selected_chips:
        areas_of_interest.append(i)
    s_areas = set(areas_of_interest)
    l_areas = list(s_areas)
    print(l_areas)
 
    mycursor = cnx.cursor()
    for i in l_areas:
        mycursor.execute("INSERT INTO history(Mood,Age,Qualification,Gender,Hobby,Budget,Climate,Area_of_Interest) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (mood_1,age_1,qualification_1,gender_1,hobby_1,budget_1,climate_1,i))
    cnx.commit()

    mycursor.close()

    # Displaying result on the result page
    return render_template('result_map.html', places=order_path, url=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=50100,debug=True)
