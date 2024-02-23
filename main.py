from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route using a decorator
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Define another route
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# This block allows running the FastAPI application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
