from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def status():
    return {
        "status": "ok",
        "response": "200",
        "message": "Service is running...",
        "description": "Building a GitOps structure with GitHub, Actions, DockerHub, and Helm Repository",
        "version": "0.0.2"
    }


@app.get("/status")
def read_root():
    return {
        "status": "ok",
        "response": "200",
        "message": "Service is running...",
        "description": "Building a GitOps structure with GitHub, Actions, DockerHub, and Helm Repository",
        "version": "0.0.1"
    }


@app.get("/about")
def read_root():
    return {
        "title": "Building a GitOps structure with GitHub, Actions, DockerHub, and Helm Repository"
    }
