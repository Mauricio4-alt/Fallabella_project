FROM python:3.10

WORKDIR /fallabella_users

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "routes.py"]

