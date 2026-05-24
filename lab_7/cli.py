import typer
from itertools import islice
import ast

from my_package.lab4_logic import unpack_recursive
from my_package.lab5_logic import make_line_reader
from my_package.lab6_logic import prime_gen

app = typer.Typer(help="CLI приложение для Лабораторной №7 (Пакеты и модули)")

@app.command()
def primes(count: int = typer.Option(10, help="Количество простых чисел для генерации")):
    """Лаб 6: Генерирует заданное количество простых чисел."""
    gen = prime_gen()
    result = list(islice(gen, count))
    typer.secho(f"Сгенерировано {count} простых чисел:", fg=typer.colors.GREEN)
    typer.echo(result)

@app.command()
def unpack(data: str = typer.Argument(..., help="Строка с вложенной структурой, например: '[1, [2, 3]]'")):
    """Лаб 4: Распаковывает вложенные структуры данных."""
    try:
        parsed_data = ast.literal_eval(data)
        result = unpack_recursive(parsed_data)
        typer.secho("Результат распаковки:", fg=typer.colors.BLUE)
        typer.echo(result)
    except Exception as e:
        typer.secho(f"Ошибка парсинга данных: {e}", fg=typer.colors.RED)

@app.command()
def read_file(filename: str = typer.Argument(..., help="Путь к текстовому файлу"),
              lines: int = typer.Option(3, help="Количество строк для чтения")):
    """Лаб 5: Читает заданное количество строк из файла с помощью замыкания."""
    try:
        reader = make_line_reader(filename)
        typer.secho(f"Чтение первых {lines} строк из файла '{filename}':", fg=typer.colors.CYAN)
        for i in range(lines):
            line = reader()
            if line is None:
                typer.secho("--- Конец файла ---", fg=typer.colors.YELLOW)
                break
            typer.echo(f"{i+1}: {line}")
    except Exception as e:
        typer.secho(f"Ошибка при чтении файла: {e}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()