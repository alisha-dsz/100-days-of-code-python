from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


BODY_COLORS = [
    "#145A32",  # Head
    "#196F3D",
    "#1E8449",
    "#229954",
    "#28B463",
    "#2ECC71",
]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

        # Head
        self.head.shapesize(stretch_wid=1.25, stretch_len=1.25)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("circle")
        segment.penup()

        # Give each segment a slightly different green
        color_index = min(len(self.segments), len(BODY_COLORS) - 1)
        segment.color(BODY_COLORS[color_index])

        segment.shapesize(stretch_wid=0.9, stretch_len=1.05)
        segment.goto(position)

        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)