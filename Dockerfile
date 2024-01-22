FROM python:3.11.4-slim-buster
WORKDIR /app
COPY . .


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application uses
EXPOSE 8000

CMD ["python", "bot.py"]
