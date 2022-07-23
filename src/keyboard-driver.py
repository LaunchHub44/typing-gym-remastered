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
        self.last_key = None

    def setup(self):
        self.keyboard_sprite = keyboard.Keyboard()
        self.keyboard_sprite.center_x = 400
        self.keyboard_sprite.center_y = 200
        self.keyboard_sprite.expected_key.append('u')    # just for fun

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((50, 50, 50))
        self.keyboard_sprite.draw()
        if self.last_key:
            arcade.draw_text(chr(self.last_key), 400, 500, arcade.color.CORNFLOWER_BLUE, 24, True)

    def on_key_press(self, key, modifiers):
        self.keyboard_sprite.recent_key.append(key)
        self.last_key = key



def main():
    mygame = KeyboardDriver()
    mygame.setup()

    arcade.run()

if __name__ == '__main__':
    main()
