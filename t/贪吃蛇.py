import random
import tkinter
import threading
import queue
import time


class Food():
    def __init__(self, queue):
        self.queue = queue
        self.new_food()

    def new_food(self):
        x = random.randrange(50, 480, 10)
        y = random.randrange(50, 380, 10)
        self.position = x, y

        self.queue.put({"food": self.position})


class Snake(threading.Thread):

    def __init__(self, world, queue):
        threading.Thread.__init__(self)

        self.world = world
        self.queue = queue
        self.points_earned = 0
        self.food = Food(self.queue)
        self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]

        self.start()

    def run(self):
        if self.world.is_game_over:
            self._delete()

        while not self.world.is_game_over:
            self.queue.put({"move": self.snake_points})
            time.sleep(0.5)
            self.move()

    def move(self):
        new_snake_point = self.cal_new_position()

        if self.food.position == new_snake_point:
            self.points_earned += 1
            self.queue.put({"point_earned": self.points_earned})
            self.food.new_food()
        else:
            self.snake_points.pop(0)
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)

    def cal_new_position(self):


        last_x, last_y = self.snake_points[-1]

        if self.direction == "Up":
            new_snake_point = last_x, last_y - 10
        elif self.direction == "Down":
            new_snake_point = last_x, last_y + 10
        elif self.direction == "Right":
            new_snake_point = last_x + 10, last_y
        elif self.direction == "Left":
            new_snake_point = last_x - 10, last_y

        return new_snake_point

    def key_pressed(self, e):
        self.direction = e.keysym2

    def check_game_over(self, snake_point):
        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over': True})


class World(tkinter.Tk):

    def __init__(self, queue):
        tkinter.Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False

        self.canvas = tkinter.Canvas(self, width=500, height=300, bg='green')
        self.canvas.pack()

        self.snake = self.canvas.create_line((0, 0), (0, 0), fill='black', width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill='#FFCC4C', outline='#FFCC4C')

        self.points_earned = self.canvas.create_text(450, 20, fill='white', text='SCORE:0')

        self.queue_handler()

    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)

                if task.get("game_over"):
                    self.game_over()
                elif task.get("move"):
                    points = [x for point in task['move'] for x in point]

                    self.canvas.coords(self.snake, *points)

        except queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text("Game Over")
        qb = tkinter.Button(self, text="Quit", command=self.destroy)
        rb = tkinter.Button(self, text="Again", command=self.__init__)


if __name__ == "__main__":
    q = queue.Queue()
    world = World(q)

    snake = Snake(world, q)
    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Up>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)

    world.mainloop()