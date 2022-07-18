import arcade

# Sprite official API document:
#   - https://api.arcade.academy/en/latest/api/sprites.html#arcade.Sprite
#

class Keyboard(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="../resource/real-keyboard.jpg")
        self.recent_key = []

    def draw(self):
        super().draw()
        if self.recent_key:
            #arcade.draw_circle_outline(100, 100, 25, arcade.color.ORANGE, 3)
            arcade.draw_circle_outline(210, 273, 15, arcade.color.ORANGE, 3)
            