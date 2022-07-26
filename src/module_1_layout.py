import arcade
import keyboard


class GameLayout(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Typing Gym: Module 1")

    def setup(self):
        arcade.start_render()
        arcade.set_background_color((50, 50, 50))
        gui_keyboard = keyboard.Keyboard()
        gui_keyboard.center_x = 400
        gui_keyboard.center_y = 200
        gui_keyboard.draw()
        gui_keyboard.load_offset()
        score = 0
        arcade.draw_text(f"Score: {score:06}", 590, 550, arcade.color.WHITE, 20)


def main():
    layout = GameLayout()
    layout.setup()
    layout.run()


if __name__ == '__main__':
    main()
