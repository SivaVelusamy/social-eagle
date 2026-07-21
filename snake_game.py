import random
import tkinter as tk

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
DELAY = 100


def opposite_direction(dir1, dir2):
    opposites = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
    return opposites.get(dir1) == dir2


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(
            root,
            width=GRID_WIDTH * CELL_SIZE,
            height=GRID_HEIGHT * CELL_SIZE,
            bg="black",
        )
        self.canvas.pack()

        self.score = 0
        self.direction = "Right"
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.food = None
        self.game_over = False
        self.text_id = None

        self.place_food()
        self.draw_board()
        self.root.bind("<Key>", self.on_key_press)
        self.update()

    def place_food(self):
        while True:
            position = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1),
            )
            if position not in self.snake:
                self.food = position
                return

    def draw_board(self):
        self.canvas.delete("all")
        self.draw_food()
        self.draw_snake()
        self.draw_score()
        if self.game_over:
            self.draw_game_over()

    def draw_snake(self):
        for index, (x, y) in enumerate(self.snake):
            color = "lime" if index == 0 else "green"
            self.draw_cell(x, y, color)

    def draw_food(self):
        x, y = self.food
        self.draw_cell(x, y, "red")

    def draw_cell(self, x, y, color):
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def draw_score(self):
        score_text = f"Score: {self.score}"
        self.canvas.create_text(
            10,
            10,
            anchor="nw",
            fill="white",
            font=("Arial", 14, "bold"),
            text=score_text,
        )

    def draw_game_over(self):
        self.canvas.create_text(
            GRID_WIDTH * CELL_SIZE / 2,
            GRID_HEIGHT * CELL_SIZE / 2,
            fill="white",
            font=("Arial", 24, "bold"),
            text="Game Over",
        )
        self.canvas.create_text(
            GRID_WIDTH * CELL_SIZE / 2,
            GRID_HEIGHT * CELL_SIZE / 2 + 30,
            fill="white",
            font=("Arial", 14),
            text=f"Final Score: {self.score}",
        )
        self.canvas.create_text(
            GRID_WIDTH * CELL_SIZE / 2,
            GRID_HEIGHT * CELL_SIZE / 2 + 60,
            fill="white",
            font=("Arial", 12),
            text="Press R to restart",
        )

    def on_key_press(self, event):
        if self.game_over:
            if event.keysym.lower() == "r":
                self.restart()
            return

        new_direction = event.keysym
        if new_direction in ["Up", "Down", "Left", "Right"]:
            if not opposite_direction(self.direction, new_direction):
                self.direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Left":
            head_x -= 1
        elif self.direction == "Right":
            head_x += 1
        elif self.direction == "Up":
            head_y -= 1
        elif self.direction == "Down":
            head_y += 1

        new_head = (head_x, head_y)

        if self.detect_collision(new_head):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop()

    def detect_collision(self, head):
        x, y = head
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            return True
        if head in self.snake:
            return True
        return False

    def update(self):
        if not self.game_over:
            self.move_snake()
        self.draw_board()
        self.root.after(DELAY, self.update)

    def restart(self):
        self.score = 0
        self.direction = "Right"
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.place_food()
        self.game_over = False
        self.draw_board()


def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
