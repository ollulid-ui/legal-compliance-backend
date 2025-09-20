FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

#   r e d e p l o y   f o r c e  
 