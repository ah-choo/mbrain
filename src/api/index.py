from src.api import app


@app.api.get("/")
def index():
    """The welcome home page.

    Returns:
        dict: welcome message.
    """
    return {"Hello": "World"}
