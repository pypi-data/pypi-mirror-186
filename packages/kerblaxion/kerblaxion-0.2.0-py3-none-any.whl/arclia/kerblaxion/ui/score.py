
import pygame

from ..assets import FONTS_PATH

class Scoreboard(object):
  def __init__(self):
    self._score = 0
    self._needs_redraw = True

    self.font = pygame.font.Font(FONTS_PATH / "Silkscreen-Regular.ttf", 8)

    # Figure out how much space we actually need
    estimated_surface = self._render_digits(0)

    self._image = pygame.surface.Surface(
      size = estimated_surface.get_size(),
    )

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value: int):
    if self._score != value:
      self._score = value
      self._needs_redraw = True

  @property
  def image(self):
    if self._needs_redraw:
      self.redraw()
    return self._image

  def _render_digits(self, value: int):
    return self.font.render(
      f"{value:08d}",
      False,
      (255, 255, 0),
    )

  def redraw(self):
    self._image.fill(
      color = (32, 32, 32),
    )

    score_text = self._render_digits(self.score)

    self._image.blit(
      source = score_text,
      dest = score_text.get_rect(
        center = self._image.get_rect().center,
      ),
    )

    self._needs_redraw = False
