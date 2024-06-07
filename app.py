from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rezervacija', methods=['GET', 'POST'])
def rezervacija():
    if request.method == 'POST':
        location = request.form['location']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        vehicle_type = request.form['vehicleType']
        vehicle_brand = request.form['vehicleBrand']
        name = request.form['name']
        email = request.form['email']
                
        flash('Reservation submitted successfully!', 'success')
        return redirect(url_for('rezervacija'))
        
    return render_template('rezervacija.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
