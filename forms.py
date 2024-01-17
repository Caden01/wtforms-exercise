from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form that allows user to add pets"""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("dog", "Dog"), ("cat", "Cat"), ("porcupine", "Porcupine")])
    photo = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form that allows user to edit pet info"""

    photo = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Note", validators=[Optional()])
    available = BooleanField("Available?")