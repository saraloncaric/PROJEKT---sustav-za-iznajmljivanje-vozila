from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import get_db

bp = Blueprint('reservation', __name__, url_prefix='/rezervacija')

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

@bp.route('/list', methods=['GET'])
def list_reservations():
    db = get_db()
    reservations = db.execute('SELECT * FROM reservations').fetchall()
    return render_template('list.html', reservations=reservations)

@bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    db = get_db()
    reservation = db.execute('SELECT * FROM reservations WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        location = request.form['location']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        vehicle_type = request.form['vehicleType']
        vehicle_brand = request.form['vehicleBrand']
        name = request.form['name']
        email = request.form['email']

        db.execute(
            'UPDATE reservations SET vehicle_type = ?, vehicle_brand = ?, start_date = ?, end_date = ?, name = ?, email = ?'
            ' WHERE id = ?',
            (vehicle_type, vehicle_brand, start_date, end_date, name, email, id)
        )
        db.commit()

        flash('Rezervacija ažurirana!', 'success')
        return redirect(url_for('reservation.rezervacija'))

    return render_template('update.html', reservation=reservation)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    db = get_db()
    db.execute('DELETE FROM reservations WHERE id = ?', (id,))
    db.commit()
    flash('Rezervacija izbrisana!', 'success')
    return redirect(url_for('reservation.rezervacija'))
