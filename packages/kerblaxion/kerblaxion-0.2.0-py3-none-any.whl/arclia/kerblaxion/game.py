
import logging

from enum import Enum
from contextlib import contextmanager

import pygame
from pygame.locals import *

from arclia.pubsub import Publisher

from .assets import MUSIC_PATH
from .ui.score import Scoreboard

LOGGER = logging.getLogger(__name__)

@contextmanager
def pygame_session():
  pygame.display.init()
  pygame.mixer.init()
  pygame.font.init()  

  yield

  pygame.quit()


class UpdateContext:
  def __init__(self, t: int, dt: int):
    self.t = t
    self.dt = dt
    # self.scale = (self.dt / 40)

class Scene(object):
  def update(self, ctx: UpdateContext):
    pass

  def draw(self, surface: pygame.surface.Surface):
    surface.fill(
      color = (0, 0, 0),
    )



class ExecutionState(Enum):
  STOPPED = 0
  STARTING = 1
  RUNNING = 2
  STOPPING = 3


class GameManager(object):
  def __init__(self,
    scale: int = 4,
    fps: int = 30,
  ):
    [self.on_event, self._emit_event] = Publisher[pygame.event.Event].methods()

    self._render_surface = pygame.surface.Surface(
      size = (320, 180),
    )

    self._display_surface = pygame.display.set_mode(
      size = (
        self._render_surface.get_width() * scale,
        self._render_surface.get_height() * scale,
      ),
    )

    pygame.display.set_caption("KERBLAXION")

    self.clock = pygame.time.Clock()
    self.fps = fps

    self.scene = Scene()
    self.execution_state = ExecutionState.STOPPED

  def request_shutdown(self):
    if self.execution_state == ExecutionState.RUNNING:
      self.execution_state = ExecutionState.STOPPING
    else:
      LOGGER.warn(f"Shutdown was requested while {type(self)} was in {self.execution_state} state")

  def run(self):
    if self.execution_state != ExecutionState.STOPPED:
      raise ValueError(f"`run()` cannot be invoked unless the {type(self)} is in the {ExecutionState.STOPPED} state")


    self.execution_state = ExecutionState.STARTING

    # TODO: Extract this logic
    pygame.mixer.music.load(MUSIC_PATH.joinpath("level01.mp3").open())
    pygame.mixer.music.play(-1)

    previous_update_at = pygame.time.get_ticks()

    self.execution_state = ExecutionState.RUNNING
    while self.execution_state == ExecutionState.RUNNING:
      for event in pygame.event.get():
        self._emit_event(event)

      update_at = pygame.time.get_ticks()
      update_context = UpdateContext(
        t = update_at,
        dt = (update_at - previous_update_at),
      )
      previous_update_at = update_at
      self.scene.update(update_context)

      self.scene.draw(self._render_surface)

      pygame.transform.scale(
        surface = self._render_surface,
        size = (
          self._display_surface.get_width(),
          self._display_surface.get_height(),
        ),
        dest_surface = self._display_surface,
      )

      pygame.display.update()

      self.clock.tick(self.fps)

