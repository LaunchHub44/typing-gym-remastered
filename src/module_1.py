import arcade
import keyboard

# TODO: write actual module_1 here.


class FirstMod(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Typing Gym: Module 1")

    def setup(self):
        arcade.start_render()
        onscreen_keyboard = keyboard.Keyboard()
        onscreen_keyboard.center_x = 400
        onscreen_keyboard.center_y = 200


def main():
    module1 = FirstMod()
    module1.setup()


if __name__ == '__main__':
    main()
