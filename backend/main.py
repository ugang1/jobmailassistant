from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Email(BaseModel):
    subject: str
    from_: str  # Use 'from_' because 'from' is a Python keyword

@app.get("/emails", response_model=List[Email])
def get_emails():
    # Example dummy data for now
    return [
        {"subject": "Interview with Google", "from_": "recruiter@google.com"},
        {"subject": "Job application received", "from_": "hr@apple.com"},
        {"subject": "Follow up on your resume", "from_": "talent@openai.com"},
    ]
