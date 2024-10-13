from fastapi import FastAPI

app = FastAPI()

# Include any necessary configurations or middleware here

# Import and include the API endpoints
from .api.v1.endpoints import example

# Include any additional setup or initialization code here