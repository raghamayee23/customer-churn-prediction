FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install pandas numpy scikit-learn xgboost fastapi uvicorn sqlalchemy psycopg2-binary

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
