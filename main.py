from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from math import gcd

app = FastAPI()


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


@app.get("/{email_path}", response_class=PlainTextResponse)
def calculate_lcm(email_path: str, x: str = None, y: str = None):
    # Проверяем, что x и y переданы и являются натуральными числами (>= 1)
    try:
        x_int = int(x)
        y_int = int(y)
        if x_int <= 0 or y_int <= 0:
            raise ValueError
        # Проверка, что строки не содержат дробей или лишних символов
        if str(x_int) != x or str(y_int) != y:
            raise ValueError
    except (TypeError, ValueError):
        return "NaN"

    result = lcm(x_int, y_int)
    return str(result)