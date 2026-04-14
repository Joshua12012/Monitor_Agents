FROM python:3.11-slim

RUN useradd -m -u 1000 user
USER user
WORKDIR /code

COPY --chown=user:user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user:user . .

EXPOSE 8000

# Correct CMD for src/ folder structure
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]