from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("snake game")
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food = Food()
scoreboard = ScoreBoard()

difficulty = screen.textinput("choose difficulty", "type 's' for easy, 'm' for median, 'h' for hard")
if difficulty:
    game_is_on = True
if difficulty == "s":
    sleep_time = 0.2
elif difficulty == "m":
    sleep_time = 0.15
else:
    sleep_time = 0.1
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()
        scoreboard.update_score()
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    #detect collision with tail
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 5:
            game_is_on = False
            scoreboard.game_over()















screen.exitonclick()