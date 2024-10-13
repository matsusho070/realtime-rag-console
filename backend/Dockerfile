FROM python:3.11-slim

WORKDIR /app/src

RUN apt-get update && apt-get install --no-install-recommends -y gcc g++ git procps

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0" , "--port", "8000", "--reload"]