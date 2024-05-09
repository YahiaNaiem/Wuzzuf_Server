from fastapi import FastAPI
import json


app = FastAPI()

@app.get("/jobs/{search}")
def get_job_data(search : str):
    try:
        with open('jobs_data.json', 'r') as json_file:
            jobs_data = json.load(json_file)
    except FileNotFoundError:
        jobs_data = {"not found" : True}
    
    return jobs_data.get(f"{search}")

@app.get("/jobs/")
def get_all_jobs():
    try:
        with open('jobs_data.json', 'r') as json_file:
            jobs_data = json.load(json_file)
    except FileNotFoundError:
        jobs_data = {}
    
    return jobs_data



