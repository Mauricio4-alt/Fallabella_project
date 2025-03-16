FROM python:3.10

WORKDIR /fallabella_products

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["python", "routes.py"]

