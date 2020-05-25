import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#setup database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

#tables
measurement = Base.classes.measurement
station = Base.classes.station

#flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start date (YYYY-MM-DD)<br/>"
        f"/api/v1.0/start date/end date (YYYY-MM-DD)<br/>")


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= '2016-08-23').all()

    session.close()

    all_prcp = list(np.ravel(results))

    return jsonify(all_prcp)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    results = session.query(measurement.station.distinct()).all()

    session.close()

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    results = session.query(measurement.station, measurement.date, measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
            filter(measurement.date >= '2016-08-23').all()

    session.close()

    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)

    results = session.query(func.min(measurement.tobs), func.round(func.avg(measurement.tobs),2), func.max(measurement.tobs)).\
        filter(measurement.date >= start).all()

    session.close()

    start_date = list(np.ravel(results))

    return jsonify(start_date)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)

    results = session.query(func.min(measurement.tobs), func.round(func.avg(measurement.tobs),2), func.max(measurement.tobs)).\
        filter(measurement.date >= start).\
            filter(measurement.date <= end).all()

    session.close()

    dates = list(np.ravel(results))

    return jsonify(dates)




if __name__ == '__main__':
    app.run(debug=True)