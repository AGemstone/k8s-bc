FROM python:3.12-alpine

WORKDIR app_fastapi
COPY backend/src .
RUN pip install -r requirements.txt
CMD ["fastapi", "run", "main.py"]
