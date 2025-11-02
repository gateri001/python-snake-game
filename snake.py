from turtle import Turtle
POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for part in POSITIONS:
            self.add_snake_part(part)
    def add_snake_part(self, part ):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(part)
        self.snake_parts.append(snake_part)
    def move(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            x = (self.snake_parts[part - 1]).xcor()
            y = (self.snake_parts[part - 1]).ycor()
            self.snake_parts[part].goto(x, y)
        self.head.forward(MOVE_DISTANCE)
    def down(self):
        if self.head.heading() !=  UP:
            self.head.setheading(DOWN)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def extend(self):
        self.add_snake_part(self.snake_parts[-1].position())
