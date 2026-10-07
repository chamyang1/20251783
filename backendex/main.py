from fastapi import FastAPI

app = FastAPI()


todos = [
    {"id": 1, "title": "자료구조 공부하기", "completed": False},
    {"id": 2, "title": "백엔드 체험하기", "completed": True}
]
@app.get("/")
def home():
    return {"message": "Hello Backend!"}


@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: dict):
    todos.append(todo)
    return todo