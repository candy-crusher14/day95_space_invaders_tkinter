from turtle import Turtle
from random import choice, sample, randint


class EnemySpaceShips:
    def __init__(self):
        self.all_enemies = []
        self.lasers = []
        self.laser_amount = 3

    def respawn_enemy(self, enemy_types):
        rows = 3
        cols = 6
        cell_width = 160
        cell_height = 100

        # Generate grid positions
        positions = [(randint(-450, 450), randint(0, 300)) for _ in range(rows * cols * 3)]
        available_positions = [pos for pos in positions if
                               all(enemy['enemy'].distance(pos) > 70 for enemy in self.all_enemies)]

        if available_positions:
            pos = choice(available_positions)
            enemy_type = choice(enemy_types)
            enemy_ships = Turtle()
            enemy_ships.shape(f'{enemy_type}')
            enemy_ships.shapesize(stretch_wid=1, stretch_len=4)
            enemy_ships.penup()
            enemy_ships.goto(pos)
            hits = 4 if enemy_type == 'images/enemyship6.gif' else 3 if enemy_type == 'images/enemyship5.gif' else 2 if enemy_type == 'images/enemyship4.gif' else 2 if enemy_type == 'images/enemyship3.gif' else 1
            enemy_structure = {'hits': hits, 'enemy': enemy_ships}
            self.all_enemies.append(enemy_structure)

    def enemy_shoot_laser(self, laser_shape):
        if len(self.lasers) <= self.laser_amount:
            shooter = choice(self.all_enemies)['enemy']  # Choose a random enemy to shoot
            shoot_laser = Turtle()
            shoot_laser.penup()
            shoot_laser.shape(f'{laser_shape}')
            shoot_laser.goto(x=shooter.xcor(), y=shooter.ycor())
            self.lasers.append(shoot_laser)




    def increase_laser_amount(self, amount):
        self.laser_amount += amount

    # def make_enemies(self, enemy_types):
    #     rows = 3
    #     cols = 6
    #     cell_width = 160
    #     cell_height = 100
    #
    #     # Generate grid positions
    #     positions = [(x, y) for x in range(-450, 450, cell_width) for y in
    #                  range(250, 250 - rows * cell_height, -cell_height)]
    #
    #     # Ensure we do not sample more positions than available
    #     num_positions = min(rows * cols, len(positions))
    #     random_positions = sample(positions, num_positions)
    #
    #     for index, pos in enumerate(random_positions):
    #         enemy_ships = Turtle()
    #         enemy_ships.shape(f'{enemy_types[index % len(enemy_types)]}')
    #         enemy_ships.shapesize(stretch_wid=1, stretch_len=4)
    #         enemy_ships.penup()
    #         enemy_ships.goto(pos)
    #         hits = 4 if enemy_types[index % len(enemy_types)] == 'images/enemyship6.gif' else 3 if enemy_types[
    #                                                                                                    index % len(
    #                                                                                                        enemy_types)] == 'images/enemyship5.gif' else 2 if \
    #         enemy_types[index % len(enemy_types)] == 'images/enemyship4.gif' else 2 if enemy_types[index % len(
    #             enemy_types)] == 'images/enemyship3.gif' else 1
    #         enemy_structure = {'hits': hits, 'enemy': enemy_ships}
    #         self.all_enemies.append(enemy_structure)
