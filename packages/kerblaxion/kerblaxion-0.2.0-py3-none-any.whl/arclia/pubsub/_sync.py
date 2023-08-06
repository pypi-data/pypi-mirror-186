
from typing import Any, Awaitable, Callable, Collection, Generic, Optional, ParamSpec

P = ParamSpec('P')

Subscriber = Callable[P, Any]

class Publisher(Generic[P]):
  @classmethod
  def methods(cls):
    p = cls()
    return (p, p._emit)

  def __init__(self, subscribers: Optional[Collection[Subscriber[P]]] = None):
    self.subscribers = [] if subscribers is None else list(subscribers)

  def add(self, s: Subscriber[P]):
    self.subscribers.append(s)

  __call__ = add

  def remove(self, s: Subscriber[P]):
    self.subscribers.remove(s)

  def _emit(self, *args: P.args, **kwargs: P.kwargs):
    for s in self.subscribers:
      s(*args, **kwargs)
