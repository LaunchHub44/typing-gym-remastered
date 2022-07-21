"""
filename:  keyboard-driver.py

This file is a test driver file, to check keyboard.py visually.
But, this is only for test.  Not part of our typing-gym.

"""

import arcade
import keyboard


class KeyboardDriver(arcade.Window):
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

    def on_key_press(self, key, modifiers):
        self.keyboard_sprite.recent_key.append(key)


def main():
    mygame = KeyboardDriver()
    mygame.setup()

    arcade.run()

if __name__ == '__main__':
    main()
