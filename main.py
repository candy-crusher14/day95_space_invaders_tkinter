import time
from random import randint, choice
from turtle import Turtle, Screen
from player import Player
from enemies import EnemySpaceShips
from scoreboard import ScoreBoard
from powerups import PowerUp
from bricks import Bricks

screen = Screen()
screen.setup(width=1024, height=690)
screen.bgcolor('black')
screen.title('Space Invaders')
screen.tracer(0)

screen.listen()
player = Player((0, -290))  # Create Paddle Class instance
score = ScoreBoard()
enemies = EnemySpaceShips()
bricks = Bricks()

# Set background image
screen.bgpic("images/background.gif")  # Ensure you have a background.gif image
# # Register custom shapes

################## PLAYER

screen.addshape("images/ourship1.gif")
screen.addshape("images/playerlaser1.gif")
screen.addshape("images/enemylaser1.gif")
screen.addshape("images/enemylaser2.gif")

################## ENEMIES
screen.addshape("images/enemyship1.gif")
screen.addshape("images/enemyship2.gif")
screen.addshape("images/enemyship3.gif")
screen.addshape("images/enemyship4.gif")
screen.addshape("images/enemyship5.gif")
screen.addshape("images/enemyship6.gif")

############## POWERS
screen.addshape("images/live1.gif")
screen.addshape("images/score1.gif")
screen.addshape("images/speed1.gif")
screen.addshape("images/explosion1.gif")

screen.addshape("images/brick1.gif")
screen.addshape("images/brick2.gif")
screen.addshape("images/brick3.gif")
screen.addshape("images/brick4.gif")
screen.addshape("images/brick5.gif")

player.shape("images/ourship1.gif")

screen.onkeypress(fun=player.move_right, key='d')
screen.onkeypress(fun=player.move_left, key='a')
screen.onkeypress(fun=player.move_forward, key='w')
screen.onkeypress(fun=player.move_backward, key='s')
screen.onkeypress(fun=lambda: player.shoot_laser(lasers_type[0]), key='space')

lives = 3
powers_list = []
milestone_reached = False  # To track if milestone score was reached

power_style = ['images/live1.gif', "images/score1.gif", "images/speed1.gif"]

power_types = ['increase_life', "increase_score", "increase_speed"]

space_ships = ['images/enemyship1.gif', 'images/enemyship2.gif', 'images/enemyship3.gif', 'images/enemyship4.gif',
               'images/enemyship5.gif', 'images/enemyship6.gif']

lasers_type = ['images/playerlaser1.gif', 'images/enemylaser1.gif',
               'images/enemylaser2.gif'
               ]

bricks_colors = ['images/brick1.gif', 'images/brick2.gif', 'images/brick3.gif', 'images/brick4.gif',
                 'images/brick5.gif']

game_finished = False
while not game_finished:
    time.sleep(0.04)
    screen.update()

    # Update laser positions and check for collisions
    if player.lasers:
        for laser in player.lasers[:]:  # Copy list to avoid modification during iteration
            laser.sety(laser.ycor() + 10)

            # Check if laser has gone beyond the screen
            if laser.ycor() > 400:
                laser.goto(900, 900)  # place outside of screen
                player.lasers.remove(laser)
                continue

            # Check for collisions with enemies
            for enemy in enemies.all_enemies[:]:  # Copy list to avoid modification during iteration
                if laser.distance(enemy['enemy']) < 40:
                    laser.goto(900, 900)  # place outside of screen
                    player.lasers.remove(laser)
                    enemy['hits'] -= 1
                    if enemy['hits'] < 1:
                        # enemy.shape('images/explosion1.gif')
                        score.points()  # Increase Score When get hit
                        random_chance = [True, False]
                        random_chance2 = randint(2, 7)
                        if random_chance2 == 6:
                            random_enemy = choice(enemies.all_enemies)
                            random_enemy['enemy'].goto(x=enemy['enemy'].xcor(),
                                                       y=enemy['enemy'].ycor())
                        # if random_chance2 == 7:
                        #     random_enemy = choice(enemies.all_enemies)
                        #     random_enemy['enemy'].goto(x=player.xcor(),
                        #                                 y=enemy['enemy'].ycor())
                        if choice(random_chance):
                            random_enemy = choice(enemies.all_enemies)
                            random_enemy['enemy'].goto(x=player.xcor() + randint(10, 20),
                                                       y=player.ycor() + randint(200, 250))

                        if choice(random_chance):  # Make powers very rare so it becomes challanging
                            power = PowerUp((enemy['enemy'].xcor(), enemy['enemy'].ycor()), choice(power_types),
                                            power_style=power_style)
                            powers_list.append(power)
                        enemy['enemy'].goto(900, 900)  # place outside of screen
                        enemies.all_enemies.remove(enemy)  # Remove the enemy from list

    if enemies.lasers:
        for laser in enemies.lasers[:]:  # Copy list to avoid modification during iteration
            laser.sety(laser.ycor() - 10)
            # Check if laser has gone beyond the screen
            if laser.ycor() < -310:
                laser.goto(900, 900)  # place outside of screen
                enemies.lasers.remove(laser)
                continue

            for enemy in enemies.all_enemies[:]:  # Copy list to avoid modification during iteration
                if laser.distance(player) < 40:
                    laser.goto(900, 900)  # place outside of screen
                    player.goto(x=0, y=-290)
                    score.decrease_lives()
                    enemies.lasers.remove(laser)

    if bricks.all_bricks:
        for brick in bricks.all_bricks[:]:
            for laser in player.lasers:
                if laser.distance(brick) < 40:
                    brick.goto(900, 900)
                    laser.goto(900, 900)  # place outside of screen
                    player.lasers.remove(laser)
                    bricks.all_bricks.remove(brick)

            for laser in enemies.lasers:
                if laser.distance(brick) < 40:
                    brick.goto(900, 900)
                    laser.goto(900, 900)  # place outside of screen
                    enemies.lasers.remove(laser)
                    bricks.all_bricks.remove(brick)

    for enemy in enemies.all_enemies[:]:
        if enemy['enemy'].distance(player) < 40:
            player.goto(0, -290)
            score.decrease_lives()
            break

    if powers_list:
        for power in powers_list:
            power.move_powers()
            if power.distance(player) < 40:
                if power.power_type == 'increase_life':
                    score.increase_lives()
                elif power.power_type == 'increase_score':
                    score.points()
                elif power.power_type == 'increase_speed':
                    player.increase_speed()
                    # screen.after(10000, player.reset_speed)

                power.goto(900, 900)  # Move it out of screen
                powers_list.remove(power)  # Remove after point gain

    if not enemies.all_enemies:
        if score.levels <= 3:
            score.level_up()
            if score.levels == 1:
                bricks.place_bricks(brick_rows=2, bricks_columns=8, bricks_colors=bricks_colors)
                for i in range(10):
                    enemies.respawn_enemy(space_ships)
            elif score.levels == 2:
                bricks.place_bricks(brick_rows=1, bricks_columns=8, bricks_colors=bricks_colors)
                enemies.increase_laser_amount(7)
                for i in range(16):
                    enemies.respawn_enemy(space_ships)
            elif score.levels == 3:
                enemies.increase_laser_amount(10)
                for i in range(20):
                    enemies.respawn_enemy(space_ships)


    if enemies.all_enemies:
        if len(enemies.all_enemies) < 2:
            if score.levels < 3:
                if randint(1,30) == 5:
                    enemies.enemy_shoot_laser(laser_shape=lasers_type[1])
            else:
                if randint(1,20) == 5:
                    enemies.enemy_shoot_laser(laser_shape=lasers_type[1])
        elif choice([False, False, True]):
            enemies.enemy_shoot_laser(laser_shape=lasers_type[1])


    if not enemies.all_enemies and score.levels >= 3:
        score.game_finished()
        game_finished = True

    lives = score.lives  # Manage lives
    if lives < 1:
        game_finished = True
        score.game_over()

screen.exitonclick()
