try:
  from . import base
except ImportError:
  import base

class GitGrep (base.Base):
    pass

engine_class = GitGrep
