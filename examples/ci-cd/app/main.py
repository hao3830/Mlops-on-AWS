from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Testing CI/CD"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)