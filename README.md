
# File Analyzer (CLI + REST API)

A Python-based file analysis tool that reads numbers from a text file and does basic statistical calculations. The same core logic is executed via both a **CLI tool** and a
**Flask REST API**, demonstrating clean backend architecture


## Features

- Analyze `.txt` files containing integers
- Calculate:
  - Count of Integers
  - Average
  - Minimum
  - Maximum
  - Product
- REST API built with Flask
- Command-line interface (CLI)
- SQLite database to store analysis reports
- Centralized configuration using `.env`
- Clean, modular project structure
## API Usage

#### Start the server:

```bash
python run.py
```
#### Analyze File:

```bash
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d "{\"file\": \"filename.txt\"}"
```

#### CLI Usage:

```bash
python cli.py
```
## Project Structure

- `app/` – Flask application (routes, services, database)
- `cli.py` – Command-line interface
- `run.py` – API entry point
- `config.py` – Environment-based configuration

## Database

- Uses SQLite
- Reports are stored automatically on each API request
- Database file is excluded from version control
## Tech Stack

- Python
- Flask
- SQLite
- dotenv