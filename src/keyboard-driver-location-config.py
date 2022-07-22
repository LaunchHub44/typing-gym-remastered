"""
filename:  keyboard-driver.py

This file is a test driver file, to check keyboard.py visually.
But, this is only for test.  Not part of our typing-gym.

"""

import arcade
import keyboard


class KeyboardDriverLocation(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "keyboard test")
        self.keyboard_sprite = None

    def setup(self):
        self.keyboard_sprite = keyboard.Keyboard()
        self.keyboard_sprite.center_x = 400
        self.keyboard_sprite.center_y = 300

    def on_draw(self):
        arcade.start_render()
        self.keyboard_sprite.draw()

        # home row, starting from (210, 273)
        spacing = 38
        for i in range(11):
            x = 210 + i * spacing
            y = 273
            arcade.draw_circle_outline(x, y, 15, arcade.color.ORANGE, 3)
            print(f' {x} {y}')

        # qwerty row, starting from (200, 310)
        for i in range(13):
            x = 200 + i * spacing
            y = 310
            arcade.draw_circle_outline(x, y, 15, arcade.color.ORANGE, 3)
            print(f' {x} {y}')

        # zxcvb row, starting from (229, 236)
        for i in range(10):
            x = 229 + i * spacing
            y = 236
            arcade.draw_circle_outline(x, y, 15, arcade.color.ORANGE, 3)
            print(f' {x} {y}')

        # number row, starting from (143, 347)
        for i in range(13):
            x = 143 + i * spacing
            y = 347
            arcade.draw_circle_outline(x, y, 15, arcade.color.ORANGE, 3)
            print(f' {x} {y}')

        print("----------")


    def on_key_press(self, key, modifiers):
        self.keyboard_sprite.recent_key.append(key)


def main():
    mygame = KeyboardDriverLocation()
    mygame.setup()

    arcade.run()

if __name__ == '__main__':
    main()
