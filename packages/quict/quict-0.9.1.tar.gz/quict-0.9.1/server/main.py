from flask import Flask

from job import job_blueprint
from env import env_blueprint


app = Flask(__name__)
app.register_blueprint(blueprint=job_blueprint)
app.register_blueprint(blueprint=env_blueprint)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
