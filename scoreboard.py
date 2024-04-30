from turtle import Turtle
# Change scoreboard variables here: (self.write______)
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

# use turtle.write and turtle.clear


class Scoreboard(Turtle):

    def __init__(self):
        """Adds attributes to the scoreboard class"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()  # this is the scoreboard

    def update_scoreboard(self):
        """The scoreboard is if a different function so that its easier and scoreboards dont overlap"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Generate GAME OVER text in the middle."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()  # clears the scoreboard
        self.update_scoreboard()  # updates the scoreboard with self.score += 1 being the new score.
