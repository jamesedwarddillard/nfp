import os
from flask import Flask, render_template
from bls_reader.bls_reader import bls_reader
from written_months import written_months
from current_report import current_report
from twitter.guestimator import response_aggregator
from twitter.twitter_search import nfp_tweets

port = int(os.environ.get('Port', 5000))

app = Flask(__name__)

@app.route("/")
def placeholder():
	return "Transmission of material in #nfpguesses is embargoed."

@app.route("/current")
def nfp():
	mos, year = current_report()
	month = written_months(mos)
	jobs = bls_reader(mos, year)
	sign = ''
	if jobs < 0:
		sign = '-'
	else:
		sign = '+'
	return "The jobs number for the most recent report ({}, {}) is {}{:,}. - #nfpguesses".format(month, year, sign, jobs)

@app.route("/guesses")
def guesses():
	entry_list = response_aggregator('#nfpguesses', '')
	guesses = len(entry_list)
	first_entry = entry_list[0]
	return render_template('guesses.html', first_entry = first_entry)


if __name__ == "__main__":
	app.run()