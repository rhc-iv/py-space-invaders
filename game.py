# Import statements:
import math
import random
import turtle

# Create the main game screen:
wn = turtle.Screen()
wn.bgcolor('#393939')
wn.title('Space Invaders using Turtle Graphics!')

# Create a border for the game screen:
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('#B4B7B4')
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

# Create a function to draw the border:
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Initialize the game score to 0:
score = 0

# Add the score to the game screen:
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('#B4B7B4')
score_pen.penup()
score_pen.setposition(-290, -270)

# Create the score string in Python:
scorestring = 'Score: %s' % score
score_pen.write(
    scorestring,
    False,
    align='left',
    font=(
        'SF Pro Display',
        14,
        'bold'
    ),
)
score_pen.hideturtle()

# Create the player sprite:
player = turtle.Turtle()
player.color('#66CCCC')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Set up the player speed when moving:
player_speed = 15

# Set up number of invaders on-screen:
number_of_invaders = 10

# Create an empty list of invaders:
invaders = []

# Add invaders to the empty list:
for i in range(number_of_invaders):
    # Create an invader:
    invaders.append(turtle.Turtle())

for invader in invaders:
    invader.color('#F2777A')
    invader.shape('square')
    invader.penup()
    invader.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    invader.setposition(x, y)

# Set invader speed while moving:
invader_speed = 2

# Create the player's laser sprite:
laser = turtle.Turtle()
laser.color('#FFCC66')
laser.shape('triangle')
laser.penup()
laser.speed(0)
laser.setheading(90)
laser.shapesize(0.5, 0.5)
laser.hideturtle()

# Set the laser speed when fired:
laser_speed = 20

# Define the state of the laser:
# 'ready' – ready to fire.
# 'fire' – bullet is firing.
laser_state = 'ready'


# Create player left/right movement:
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


# Create a function to fire player's laser:
def fire_laser():
    # Declare laser_state as a global so that it can be changed:
    global laser_state
    if laser_state == 'ready':
        laser_state = 'fire'
        # Have laser fire from player sprite:
        x = player.xcor()
        y = player.ycor() + 10
        laser.setposition(x, y)
        laser.showturtle()


# Create a function to detect invader/laser/player collisions:
def is_collision(t1, t2):
    distance = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Make the keyboard bindings for gameplay:
turtle.listen()
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkeypress(fire_laser, 'space')

# Create the main game loop:
while True:
    # Move the invaders on the screen:
    for invader in invaders:
        x = invader.xcor()
        x += invader_speed
        invader.setx(x)
        # Move the invaders back and down:
        if invader.xcor() > 280:
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
            invader_speed *= -1
        if invader.xcor() < -280:
            for i in invaders:
                y = i.ycor()
                y -= 40
                i.sety(y)
            invader_speed *= -1
        # Check for invader/laser collisions:
        if is_collision(laser, invader):
            # Reset the bullet to fire again:
            laser.hideturtle()
            laser_state = 'ready'
            laser.setposition(0, -400)
            # Reset and place the replacement invader:
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            invader.setposition(x, y)
            # Update the score for killing an invader:
            score += 10
            scorestring = 'Score: %s' % score
            score_pen.clear()
            score_pen.write(
                scorestring,
                False,
                align='left',
                font=(
                    'SF Pro Display',
                    14,
                    'bold',
                ),
            )
        # Check for invader/player collision:
        if is_collision(player, invader):
            player.hideturtle()
            invader.hideturtle()
            print('Game Over!')
            break
    # Create the bullet movement on-screen:
    if laser_state == 'fire':
        y = laser.ycor()
        y += laser_speed
        laser.sety(y)
    # Check to see if laser misses all invaders:
    if laser.ycor() > 275:
        laser.hideturtle()
        laser_state = 'ready'

# Run the main game loop:
wn.mainloop()