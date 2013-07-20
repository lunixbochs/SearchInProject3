import os
import platform
import sublime

if int(sublime.version()) >= 3000:
    from . import ack
    from . import base
    from . import grep
    from . import git_grep
    from . import the_silver_searcher
    from . import find_str


def can_exec(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)


def which(cmd):
    for base in os.getenv('PATH', '').split(os.pathsep):
        path = os.path.join(base, cmd)
        if can_exec(path):
            return path

    return None


class fastest:
    @classmethod
    def engine_class(cls, *args, **kwargs):
        if platform.system() == 'Windows':
            best = find_str.engine_class(*args, **kwargs)
        else:
            best = grep.engine_class(*args, **kwargs)

        for other in (grep, git_grep, ack, the_silver_searcher):
            c = other.engine_class(*args, **kwargs)
            if which(c.path_to_executable):
                best = c

        print('best was:', best)
        return best


# __all__ = ["base", "grep", "ack", "the_silver_searcher", "git_grep"]
