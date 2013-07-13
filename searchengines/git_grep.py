import sublime

if int(sublime.version()) >= 3000:
    from . import base
else:
    import base

class GitGrep (base.Base):
    pass

engine_class = GitGrep
