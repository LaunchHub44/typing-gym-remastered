import arcade

# Sprite official API document:
#   - https://api.arcade.academy/en/latest/api/sprites.html#arcade.Sprite
#

class Keyboard(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="../resource/real-keyboard.jpg")
        self.recent_key = []
        self.last_key = None
        self.locations = self.load_location()   # location:  'a': (210, 273)

    def load_location(self) -> dict:
        rtn = {}
        with open('location.dat') as fh:
            for line in fh:
                line = line.strip()
                if len(line) == 0:
                    continue
                tok = line.split()
                rtn[tok[0]] = (int(tok[1]), int(tok[2]))
        return rtn

    def draw(self):
        super().draw()
        if self.recent_key:
            self.last_key = self.recent_key[0]
            self.recent_key = self.recent_key[1:]
            print(self.last_key)

        if self.last_key:
            # TODO map all possible case
            # ( https://api.arcade.academy/en/latest/arcade.key.html )

            # case 1:  alphabet
            key2char: int = None
            if arcade.key.A <= self.last_key <= arcade.key.Z:
                key2char = chr(self.last_key)

            # case 2: numeric
            pass

            # case 3: special characters
            pass


            (x, y) = self.locations[key2char]
            arcade.draw_circle_outline(x, y, 15, arcade.color.ORANGE, 3)


