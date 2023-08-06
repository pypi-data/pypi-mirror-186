
import argparse

import pygame
from pygame.locals import *

from .game import GameManager, pygame_session
from .hero import prepare

def create_parser():
  parser = argparse.ArgumentParser("KERBLAXION")

  parser.add_argument(
    "-s",
    "--scale",
    type = int,
    default = 4,
    help="Scale factor for the display (Default: 4)",
  )

  parser.add_argument(
    "--fps",
    type = int,
    default = 30,
    help="Frames per second (Default: 30)",
  )

  return parser


def main():
  args = create_parser().parse_args()

  with pygame_session():
    game = GameManager(
      scale = args.scale,
      fps = args.fps,
    )

    def handle_quit(event: pygame.event.Event):
      if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        game.request_shutdown()

    game.on_event(handle_quit)

    game.scene = prepare()

    game.run()
