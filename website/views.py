from flask import Blueprint, render_template, request, flash, url_for,redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        print(len(note))
        print(note)
        if len(note) < 2:
            flash('Note is too short!', category = 'error')
        else:
            new_note = Note(data = note, user_id= current_user.id )
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully.' , category='success')
    return render_template("home.html", user = current_user)

# @views.route('/delete-note', methods= ['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)

#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#         return jsonify({})
    
@views.route('/delete/<int:id>')
def delete_note(id):
    note_to_delete = Note.query.get_or_404(id)
    db.session.delete(note_to_delete)
    db.session.commit()
    flash('Note Delete Successfully!', category='success')
    return redirect(url_for('views.home'))