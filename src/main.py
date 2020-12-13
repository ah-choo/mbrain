from src.api import app
from uvicorn import run

server = app.api


def main():
    run(app=server, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
