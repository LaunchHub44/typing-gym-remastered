import arcade

# Sprite official API document:
#   - https://api.arcade.academy/en/latest/api/sprites.html#arcade.Sprite
#

class Keyboard(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="../resource/real-keyboard.jpg")
        self.recent_key: list[arcade.key] = []
        self.expected_key: list[str] = []
        self.last_key: arcade.key  = None
        self.offsets = self.load_offset()

    def load_offset(self) -> dict:
        rtn = {}
        with open('key-offset.dat') as fh:
            for line in fh:
                line = line.strip()
                if len(line) == 0:
                    continue
                tok = line.split()
                rtn[tok[0]] = (int(tok[1]), int(tok[2]))
        return rtn

    def set_location(self, x:int, y:int):
        self.center_x = x
        self.center_y = y

    def add_expected_key(self, keychar: str):
        for c in keychar:
            self.expected_key.append(c)

    def draw_key_circle(self, x:int, y:int, color:arcade.color, radius:int=15, thickness:int=3):
        arcade.draw_circle_outline(x, y, radius, color, thickness)

    def draw(self):
        super().draw()
        if self.expected_key:
            ekey = self.expected_key[0]
            ex, ey = self.offsets[ekey]
            self.draw_key_circle(ex + self.center_x, ey + self.center_y, arcade.color.BLUE)
            arcade.draw_text(ekey, 400, 500, arcade.color.CORN, 24)

        if self.recent_key:
            # pop the first character.
            self.last_key = self.recent_key[0]
            self.recent_key = self.recent_key[1:]
            print(self.last_key)

        if self.last_key:
            key2char: int = None

            # Map all the cases:  case 1, 2, 3.
            # case 1:  alphabet
            if arcade.key.A <= self.last_key <= arcade.key.Z:   # python specific, "range-boolean" operators.
                key2char = chr(self.last_key)
            # case 2: numeric
            elif arcade.key.KEY_0 <= self.last_key <= arcade.key.KEY_9:
                # arcade.key.KEY_0 <= self.last_key   and
                #   self.last_key <= arcade.key.KEY_9
                key2char = chr(self.last_key)

            # case 3: special characters:  DIFFICULT
            else:
                if self.last_key == arcade.key.QUOTELEFT:
                    key2char = '`'
                elif self.last_key == arcade.key.MINUS:
                    key2char = '-'
                elif self.last_key == arcade.key.EQUAL:
                    key2char = '='
                elif self.last_key == arcade.key.SEMICOLON:
                    key2char = ';'
                elif self.last_key == arcade.key.APOSTROPHE:
                    key2char = "'"
                elif self.last_key == arcade.key.COMMA:
                    key2char = ','
                elif self.last_key == arcade.key.PERIOD:
                    key2char = '.'
                elif self.last_key == arcade.key.SLASH:
                    key2char = '/'
                elif self.last_key == arcade.key.SPACE:
                    key2char = ' '
                elif self.last_key == arcade.key.BRACKETLEFT:
                    key2char = '['
                elif self.last_key == arcade.key.BRACKETRIGHT:
                    key2char = ']'
                elif self.last_key == arcade.key.BACKSLASH:
                    key2char = '\\'


            ( offset_x, offset_y ) = self.offsets[key2char]
            x = self.center_x + offset_x
            y = self.center_y + offset_y

            # POP the matching expected characters
            if self.expected_key:
                if self.last_key == ord(self.expected_key[0]):
                    # user matched key with the expected char.  POP the expected key!
                    self.expected_key = self.expected_key[1:]     # chop off the first one.
                    self.draw_key_circle(x, y, arcade.color.ORANGE, 15, 3)
                    self.last_key = None
                else:
                    self.draw_key_circle(x, y, arcade.color.RED, 15, 3)

            # Please read: access list item by index:  https://www.w3schools.com/python/python_lists_access.asp
