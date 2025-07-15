from flask import Flask, request
from jobspy import scrape_jobs
from datetime import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    search_term = request.args.get('search_term', 'power bi')
    google_search_term = f"{search_term} jobs montreal depuis hier"

    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "google"],
        search_term=search_term,
        google_search_term=google_search_term,
        location="Montreal",
        results_wanted=20,
        hours_old=24,
        country_indeed='Canada',
        linkedin_fetch_description=True,
    )

    return jobs.to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)