import tkinter as tk

# Инициализация на прозореца
root = tk.Tk()
root.title("Проблемът с 8те царици")
# Добавяне на рамки за показване на цифрите от 1 до 8 за всяка колона и ред
row_frame = tk.Frame(root, width=50, height=400)
row_frame.pack(side="left")

for i in range(1, 9):
    label = tk.Label(row_frame, text=str(i))
    label.pack(fill="y", pady=10)

col_frame = tk.Frame(root, width=400, height=50)
col_frame.pack()
for i in range(1, 9):
    label = tk.Label(col_frame, text=str(i), width=2)
    label.pack(side="left", padx=10)
# Създаване на шахматната дъска
board = tk.Canvas(root, width=400, height=400)
board.pack()

for i in range(8):
    for j in range(8):
        x1 = j * 50
        y1 = i * 50
        x2 = x1 + 50
        y2 = y1 + 50
        if (i + j) % 2 == 0:
            board.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            board.create_rectangle(x1, y1, x2, y2, fill="gray")

def queens_conflict(queens, depth=0):
    """
    Функцията проверява дали има конфликти между цариците
    queens - списък от координати на цариците (tuple с две числа)
    depth - текущата дълбочина на рекурсията
    """
    n = len(queens)
    conflicting_queens = []
    for i in range(n):
        for j in range(i+1, n):
            # Проверка за пресичане на редове и колони
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
                conflicting_queens.extend([i, j])
            # Проверка за пресичане на диагонали
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                conflicting_queens.extend([i, j])
            if depth >= 100:
                # Прекъсване на рекурсията, за да се избегне безкраен цикъл
                return []

    conflicting_queens = list(set(conflicting_queens))  # Изключване на повтарящите се индекси
    conflicting_queens.sort()
    return conflicting_queens
   

# Създаване на етикет за показване на конфликтите
conflict_label = tk.Label(root, text="")
conflict_label.pack(side="bottom")
conflicting_queens_label = tk.Label(root, text="")
conflicting_queens_label.pack(side="bottom")
# Функция за добавяне на царица
def add_queen():
    conflict_label.config(text="")  # Изтриване на предишната стойност на етикета
    try:
        row = int(entry_row.get())
        col = int(entry_col.get())
    except ValueError:
        conflict_label.config(text="Невалидни данни за ред или колона!")
        return

    if row < 0 or row > 7:
        conflict_label.config(text="Невалиден ред!")
        return

    if col < 0 or col > 7:
        conflict_label.config(text="Невалидна колона!")
        return

    queens = [(int(text[0]), int(text[1])) for text in board.find_withtag("Q")]
    conflicting_queens = queens_conflict(queens)
    if conflicting_queens:
        if queens:
            x, y = queens[-1]
            board.delete(board.find_closest(x*50+25, y*50+25))
        conflict_label.config(text="Конфликт между цариците: " + str(conflicting_queens))
    else:
        board.create_text(col*50+25, row*50+25, text="Q", font=("Arial", 32))

def remove_queen():
    conflict_label.config(text="")
    try:
        row = int(entry_row.get())
        col = int(entry_col.get())
    except ValueError:
        conflict_label.config(text="Невалидни данни за ред или колона!")
        return

    if row < 0 or row > 7:
        conflict_label.config(text="Невалиден ред!")
        return

    if col < 0 or col > 7:
        conflict_label.config(text="Невалидна колона!")
        return

    queens = [(int(text[0]), int(text[1])) for text in board.find_withtag("Q")]
    conflicting_queens = queens_conflict(queens)
    if (row, col) not in queens:
        conflict_label.config(text="Няма царица на посоченото място!")
    else:
        board.delete(board.find_closest(col*50+25, row*50+25))
        if conflicting_queens:
            conflict_label.config(text="Конфликт между цариците: " + str(conflicting_queens))
        else:
            conflict_label.config(text="")

# Текстово поле за въвеждане на ред и колона на царицата
entry_row = tk.Entry(root, width=3)
entry_row.pack(side="left")
entry_col = tk.Entry(root, width=3)
entry_col.pack(side="left")
# Бутон за добавяне на царица
button = tk.Button(root, text="Добави царица", command=add_queen)
button.pack(side="left")
#текстово поле за изтриване на ред и колона на царица
remove_entry_row = tk.Entry(root, width=3)
remove_entry_row.pack(side="left")
remove_entry_col = tk.Entry(root, width=3)
remove_entry_col.pack(side="left")

remove_button = tk.Button(root, text="Изтрий царица", command=remove_queen)
remove_button.pack(side="left")



root.mainloop()
