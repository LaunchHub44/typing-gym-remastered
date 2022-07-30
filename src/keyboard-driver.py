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
        self.score = 0

    def setup(self):
        self.keyboard_sprite = keyboard.Keyboard()
        self.keyboard_sprite.set_location(400, 200)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((50, 50, 50))
        self.keyboard_sprite.draw()
        arcade.draw_text(f"Score: {self.score:06}", 560, 550, arcade.color.WHITE, 24)
        if self.last_key:
            arcade.draw_text(chr(self.last_key), 400, 450, arcade.color.CORNFLOWER_BLUE, 24, True)

    def on_key_press(self, key, modifiers):
        self.keyboard_sprite.add_key_queue(key)
        self.score += 10


def main():
    mygame = KeyboardDriver()
    mygame.setup()

    # Prefeed everything.
    #   TODO:  How can we make like a game?  adding random words/keys while playing?
    mygame.keyboard_sprite.add_expected_key("a")
    mygame.keyboard_sprite.add_expected_key("b")
    mygame.keyboard_sprite.add_expected_key("c")
    mygame.keyboard_sprite.add_expected_key("d")
    mygame.keyboard_sprite.add_expected_key("hello")
    mygame.keyboard_sprite.add_expected_key(",")
    mygame.keyboard_sprite.add_expected_key("world")

    arcade.run()   # this loop will run 60 frames/sec.


if __name__ == '__main__':
    main()
