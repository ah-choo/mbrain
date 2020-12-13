from src.api import app

@app.api.get("/posts")
def get_post_list():
    return {}
