from flask import Flask
from bls_reader.bls_reader import bls_reader
import os
port = int(os.environ.get('Port', 33507))

app = Flask(__name__)

@app.route("/")
def nfp():
	jobs = bls_reader(6, 2015)
	return "Welcome to #nfpguesses. The most recent jobs number is {:,}.".format(jobs)

if __name__ == "__main__":
	app.run()