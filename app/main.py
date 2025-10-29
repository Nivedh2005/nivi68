from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Grade Calculator API is running!"}

@app.post("/calculate")
def calculate_grade(scores: dict):
    total = sum(scores.values())
    average = total / len(scores)
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return {"average": average, "grade": grade}
