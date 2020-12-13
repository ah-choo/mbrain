from src.api import app


@app.api.get("/chats")
def get_chats():
    return {}
