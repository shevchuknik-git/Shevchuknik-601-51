from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import sqlite3
import uvicorn

app = FastAPI()

conn = sqlite3.connect("web_tictactoe.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        winner TEXT
    )
''')
conn.commit()

class GameResult(BaseModel):
    winner: str

@app.post("/api/save_result")
def save_result(result: GameResult):
    """API эндпоинт для сохранения результата игры"""
    cursor.execute("INSERT INTO history (winner) VALUES (?)", (result.winner,))
    conn.commit()
    return {"status": "success"}

@app.get("/api/stats")
def get_stats():
    """API эндпоинт для получения статистики"""
    cursor.execute("SELECT winner, COUNT(*) FROM history GROUP BY winner")
    return [{"winner": row[0], "count": row[1]} for row in cursor.fetchall()]

@app.get("/", response_class=HTMLResponse)
def get_game_ui():
    """Возвращает HTML-страницу с игрой"""
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Крестики-нолики (FastAPI)</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; flex-direction: column; align-items: center; margin-top: 50px; }
            .board { display: grid; grid-template-columns: repeat(3, 100px); gap: 5px; margin-bottom: 20px; }
            .cell { width: 100px; height: 100px; font-size: 48px; font-weight: bold; text-align: center; cursor: pointer; background-color: white; border: 2px solid #ccc; }
            .cell:hover { background-color: #f0f0f0; }
            .blue { color: blue; }
            .red { color: red; }
            .btn { padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; }
            #stats { margin-top: 20px; font-size: 18px; }
        </style>
    </head>
    <body>
        <h1>Крестики-нолики</h1>
        <h2 id="status">Ход игрока: X</h2>
        
        <div class="board" id="board"></div>
        
        <div>
            <button class="btn" onclick="resetGame()">Перезапустить</button>
            <button class="btn" onclick="loadStats()">Статистика</button>
        </div>
        
        <pre id="stats"></pre>

        <script>
            let board = ["", "", "", "", "", "", "", "", ""];
            let currentPlayer = "X";
            let gameActive = true;

            function createBoard() {
                const boardDiv = document.getElementById("board");
                boardDiv.innerHTML = "";
                for (let i = 0; i < 9; i++) {
                    let cell = document.createElement("button");
                    cell.className = "cell";
                    cell.onclick = () => makeMove(i, cell);
                    boardDiv.appendChild(cell);
                }
            }

            function makeMove(index, cell) {
                if (board[index] !== "" || !gameActive) return;
                
                board[index] = currentPlayer;
                cell.innerText = currentPlayer;
                cell.classList.add(currentPlayer === "X" ? "blue" : "red");
                
                if (checkWin()) {
                    document.getElementById("status").innerText = `Победил игрок ${currentPlayer}!`;
                    gameActive = false;
                    saveResult(currentPlayer);
                } else if (!board.includes("")) {
                    document.getElementById("status").innerText = "Ничья!";
                    gameActive = false;
                    saveResult("Ничья");
                } else {
                    currentPlayer = currentPlayer === "X" ? "O" : "X";
                    document.getElementById("status").innerText = `Ход игрока: ${currentPlayer}`;
                }
            }

            function checkWin() {
                const winCombos = [
                    [0,1,2], [3,4,5], [6,7,8], // Строки
                    [0,3,6], [1,4,7], [2,5,8], // Столбцы
                    [0,4,8], [2,4,6]           // Диагонали
                ];
                return winCombos.some(combo => {
                    return combo.every(i => board[i] === currentPlayer);
                });
            }

            function resetGame() {
                board = ["", "", "", "", "", "", "", "", ""];
                currentPlayer = "X";
                gameActive = true;
                document.getElementById("status").innerText = `Ход игрока: X`;
                document.getElementById("stats").innerText = "";
                createBoard();
            }

            async function saveResult(winner) {
                await fetch("/api/save_result", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({winner: winner})
                });
            }

            async function loadStats() {
                let res = await fetch("/api/stats");
                let data = await res.json();
                let text = "Статистика побед:\\n";
                data.forEach(d => text += `${d.winner}: ${d.count} раз(а)\\n`);
                document.getElementById("stats").innerText = text || "История пуста";
            }

            createBoard();
        </script>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)