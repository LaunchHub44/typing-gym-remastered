import arcade
import keyboard

# TODO: write actual module_1 here.


class FirstMod(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Typing Gym: Module 1")

    def setup(self):
        self.onscreen_keyboard = keyboard.Keyboard()
        self.onscreen_keyboard.center_x = 400
        self.onscreen_keyboard.center_y = 200

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((50, 50, 50))
        self.onscreen_keyboard.draw()


def main():
    module1 = FirstMod()
    module1.setup()

    arcade.run()

if __name__ == '__main__':
    main()
