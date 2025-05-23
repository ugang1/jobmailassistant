from fastapi import FastAPI
from backend.email_reader import fetch_job_emails  # make sure this line is below the import above

app = FastAPI()

@app.get("/emails")
def read_all_emails():
    email = "ujjwalgangolu7@gmail.com"
    try:
        return fetch_job_emails(email)
    except Exception as e:
        return {"error": str(e)}
