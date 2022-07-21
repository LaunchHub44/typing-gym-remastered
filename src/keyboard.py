import arcade

# Sprite official API document:
#   - https://api.arcade.academy/en/latest/api/sprites.html#arcade.Sprite
#

class Keyboard(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="../resource/real-keyboard.jpg")
        self.recent_key = []
        self.last_key = None

    def draw(self):
        super().draw()
        if self.recent_key:
            self.last_key = self.recent_key[0]
            self.recent_key = self.recent_key[1:]
            print(self.last_key)

        if self.last_key == arcade.key.A:
            # arcade.draw_circle_outline(100, 100, 25, arcade.color.ORANGE, 3)
            arcade.draw_circle_outline(210, 273, 15, arcade.color.ORANGE, 3)
        elif self.last_key == arcade.key.B:
            arcade.draw_circle_outline(380, 235, 15, arcade.color.ORANGE, 3)


