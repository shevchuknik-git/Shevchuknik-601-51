from fastapi import FastAPI
from itertools import islice
import uvicorn
from my_package.lab6_logic import prime_gen

app = FastAPI(
    title="Lab 7 Web API",
    description="Веб-приложение для генерации простых чисел на основе пакета my_package"
)

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать! Перейдите на /docs для просмотра документации API."}

@app.get("/api/primes/")
def get_primes(count: int = 10):
    """
    Возвращает список из заданного количества простых чисел.
    """
    if count <= 0 or count > 10000:
        return {"error": "Количество должно быть от 1 до 10000"}
        
    gen = prime_gen()
    result = list(islice(gen, count))
    
    return {
        "requested_count": count,
        "result": result
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)