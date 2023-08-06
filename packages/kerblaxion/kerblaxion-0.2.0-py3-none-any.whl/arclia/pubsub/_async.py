
from typing import Any, Awaitable, Callable, Collection, Generic, Optional, ParamSpec

import asyncio

P = ParamSpec('P')

AsyncSubscriber = Callable[P, Awaitable[Any]]

class AsyncPublisher(Generic[P]):
  @classmethod
  def methods(cls):
    p = cls()
    return (p, p._emit)

  def __init__(self, subscribers: Optional[Collection[AsyncSubscriber[P]]] = None):
    self.subscribers = [] if subscribers is None else list(subscribers)

  def add(self, s: AsyncSubscriber[P]):
    self.subscribers.append(s)

  __call__ = add

  def remove(self, s: AsyncSubscriber[P]):
    self.subscribers.remove(s)

  async def _emit(self, *args: P.args, **kwargs: P.kwargs):
    await asyncio.gather(*[
      s(*args, **kwargs) for s in self.subscribers
    ])

