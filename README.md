## Celery Memory Leak

This is a simple project to demonstrate a memory leak in Celery.

### Setup

1. Clone this repo
2. Create a virtualenv
3. Install requirements with `pip install -r requirements.txt`

### Run

Run RabbitMQ:

```bash
docker-compose up -d
```

Run the web server:

```bash
python main.py
```

Run the Celery worker:

```bash
memray run -m celery -A main.worker worker --loglevel=info -P prefork --concurrency 1
```

This repository includes a `.bin` file generated from [`memray`](https://bloomberg.github.io/memray/getting_started.html).
Around 5000 tasks were executed to generate that file.
