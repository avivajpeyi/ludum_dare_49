from .ui import ptext
from . import constants as const
from .ui import ptext
from . colors import WHITE

class ScoreManager:
    def __init__(self):
        self._points = 0

    def increase_score(self):
        self._points += 1

    def draw_score_on_top_right(self):
        text = f'Score {self._points:03d}'
        ptext.draw(
            text, topleft=(0, 0),
            color=WHITE,
            fontname=const.FONT_MAIN
        )
