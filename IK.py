#!/usr/bin/env python3

import arcade
# from arcade.experimental.uislider import UISlider
# from arcade.gui import UILabel
# from arcade.gui.events import UIOnChangeEvent

import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Inverse Kinematics"

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
RADIANS_PER_FRAME = 0.02


class Joint:
    def __init__(self, x, y, length=100, angle=0, colour=arcade.color.WHITE):
        self.x = x
        self.y = y
        self.length = length
        self.angle = math.radians(angle)
        self.colour = colour
        self.end_x = 0
        self.end_y = 0

    def update(self, angle):
        self.angle = angle
        self.end_x = self.length * math.sin(self.angle+1.570796) + self.x
        self.end_y = self.length * math.cos(self.angle+1.570796) + self.y

    def draw(self):
        arcade.draw_line(self.x, self.y, self.end_x, self.end_y, self.colour, 10)

    def getAngle(self):
        return math.degrees(self.angle)


class Point:
    def __init__(self, x=-100, y=-100):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 10, arcade.color.YELLOW, num_segments=20)


class IK(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.joints = {
            Joint((CENTER_X/2), CENTER_Y, 100, 20, arcade.color.RED),
            Joint((CENTER_X/2) + 100, CENTER_Y, 150, 45, arcade.color.BLUE),
            Joint((CENTER_X/2) + 250, CENTER_Y, 100, 90, arcade.color.GREEN)
        }

        self.point = Point()

        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, delta_time):
        for joint in self.joints:
            joint.update(0)

    def on_draw(self):
        self.clear()

        arcade.start_render()
        for joint in self.joints:
            joint.draw()

        for joint in self.joints:
            arcade.draw_circle_filled(joint.end_x, joint.end_y, 12, arcade.color.WHITE, num_segments=20)
        
        self.point.draw()

    def on_mouse_press(self, x, y, button, key_modifier):
        print(f"Adding new point to get (X: {x}, Y: {y})")
        self.point.update(x, y)


def main():
    IK(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
