from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import get_db

bp = Blueprint('reservation', __name__, url_prefix='/reservation')

@bp.route('/', methods=['GET', 'POST'])
def rezervacija():
    if request.method == 'POST':
        location = request.form['location']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        vehicle_type = request.form['vehicleType']
        vehicle_brand = request.form['vehicleBrand']
        name = request.form['name']
        email = request.form['email']

        db = get_db()
        db.execute(
            'INSERT INTO reservations (vehicle_type, vehicle_brand, start_date, end_date, name, email)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (vehicle_type, vehicle_brand, start_date, end_date, name, email)
        )
        db.commit()

        flash('Rezervacija uspješna!', 'success')
        return redirect(url_for('reservation.rezervacija'))

    return render_template('rezervacija.html')
