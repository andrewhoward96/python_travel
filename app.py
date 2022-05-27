from flask import Flask, render_template

from controllers.visit_controller import visits_blueprint
from controllers.location_controller import locations_blueprint
from controllers.traveler_controller import travelers_blueprint

app = Flask(__name__)

app.register_blueprint(visits_blueprint)
app.register_blueprint(locations_blueprint)
app.register_blueprint(travelers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)