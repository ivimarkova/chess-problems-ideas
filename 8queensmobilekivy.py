from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color, Ellipse

# Recursive function to find all solutions
def find_queens_solutions(row, queens):
    if row == 8:
        # Solution found, add it to the list
        solutions.append(queens[:])
    else:
        for col in range(8):
            if not any(row == r or col == queens[r] or abs(row - r) == abs(col - queens[r]) for r in range(row)):
                queens[row] = col
                find_queens_solutions(row + 1, queens)

# Function to display a solution on the chessboard
def display_solution(solution):
    board.canvas.clear()
    with board.canvas:
        for row, col in enumerate(solution):
            Color(1, 0, 0, 1)  # Set the color to red
            Ellipse(pos=(col * square_size, row * square_size), size=(square_size, square_size))
            Color(1, 1, 1, 1)  # Set the color back to white
            Ellipse(pos=((col + 0.25) * square_size, (row + 0.25) * square_size), size=(square_size // 2, square_size // 2))

# Function to display the next solution
def display_next_solution(button):
    global solution_index
    if solution_index < num_solutions:
        display_solution(solutions[solution_index])
        solution_index += 1
    else:
        button.disabled = True

# Create the main widget
class MainWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create the chessboard
        self.square_size = self.width // 8
        with self.canvas:
            for row in range(8):
                for col in range(8):
                    x = col * self.square_size
                    y = row * self.square_size
                    if (row + col) % 2 == 0:
                        Color(1, 1, 1, 1)  # Set the color to white
                    else:
                        Color(0.2, 0.2, 0.2, 1)  # Set the color to gray
                    Rectangle(pos=(x, y), size=(self.square_size, self.square_size))

        # Find all solutions to the 8 queens problem
        global solutions
        solutions = []
        find_queens_solutions(0, [0] * 8)
        global num_solutions
        num_solutions = len(solutions)
        
        # Create the next button
        next_button = Button(text="Next Solution", size_hint=(None, None), size=(150, 50), pos=(self.width // 2 - 75, 0))
        next_button.bind(on_press=display_next_solution)
        self.add_widget(next_button)

# Create the app
class MyApp(App):
    def build(self):
        return MainWidget()

# Run the app
if __name__ == '__main__':
    MyApp().run()
