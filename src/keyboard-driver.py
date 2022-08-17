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
        self.keyboard_sprite.attempts += 1
        if self.keyboard_sprite.last_key == self.keyboard_sprite.expected_key:
            if self.keyboard_sprite.attempts <= 1:
                self.score += 10
                self.keyboard_sprite.attempts = 0
            elif self.keyboard_sprite.attempts == 2:
                self.score += 5
                self.keyboard_sprite.attempts = 0
            elif self.keyboard_sprite.attempts == 3:
                self.score += 2
                self.keyboard_sprite.attempts = 0
            elif self.keyboard_sprite.attempts > 3:
                self.score += 1
                self.keyboard_sprite.attempts = 0


def main():
    mygame = KeyboardDriver()
    mygame.setup()

    # Prefeed everything.
    #   TODO:  How can we make like a game?  adding random words/keys while playing?
    mygame.keyboard_sprite.add_expected_word("a")
    mygame.keyboard_sprite.add_expected_word("b")
    mygame.keyboard_sprite.add_expected_word("c")
    mygame.keyboard_sprite.add_expected_word("d")
    mygame.keyboard_sprite.add_expected_word("hello")
    mygame.keyboard_sprite.add_expected_word(",")
    mygame.keyboard_sprite.add_expected_word("world")

    arcade.run()   # this loop will run 60 frames/sec.


if __name__ == '__main__':
    main()
