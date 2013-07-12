try:
  from . import base
except ImportError:
  import base

class Ack (base.Base):
    pass

engine_class = Ack
