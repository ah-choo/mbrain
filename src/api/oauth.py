from src.api import app


@app.api.get("/me")
def get_my_info():
    return {}


@app.api.get("/sign-in")
def get_signin():
    return {}


@app.api.post("/sign-in")
def create_signin():
    return {}


@app.api.delete("/sign-in")
def delete_signin():
    return {}
