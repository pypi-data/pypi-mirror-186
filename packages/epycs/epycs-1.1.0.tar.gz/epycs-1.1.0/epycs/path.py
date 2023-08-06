import os

# Windows supports both \ and / as path separators
pathseps = ("/",) if os.name == "posix" else ("\\", "/")


def parts(p):
    r = [""]
    for c in str(p):
        if c in pathseps:
            r.append("")
        else:
            r[-1] += c
    return r
