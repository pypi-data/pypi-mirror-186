import subprocess
import sys
import os
import io
import re
import epycs.path
from pathlib import Path
from functools import lru_cache

"""
Global epycs arguments

* `verbose`: Print all command to stderr
* `exit_on_error`: In case of error, exit immediately the program with an error
                   code.
"""
verbose = False
exit_on_error = True


class ShellProgramError(Exception):
    pass


class ShellProgramNotFoundError(ShellProgramError):
    pass


def extract_overloaded_kw(kw):
    """
    We define a set of kwargs that are not present in the standard
    :function:`subprocess.run()` argument list (and hopefully wont be in the
    future).
    We call those overloaded arguments, to differenciate them from the
    standards subprocess keyword arguments.

    The arguments come with two names: the *short name*, which is used below,
    and the *long name*, which is :py:`epycs_<short_name>`.
    The short name can be used if you don't expect it to conflict with the
    subprocess module, the long name is guaranteed to work over all versions
    of the subprocess module.

    For forward compatibility, the guarantees is that in case of an update of
    the subprocess module, and conflict between the short name and long name,
    the proper *:module:`subprocess`* keyword argument will be set, and the
    argument will be ignored by :module:`epycs.subprocess`.
    This implies three things:

    * In case a short name is passed on but know by epycs to be used by
      :function:`subprocess.run()`, it will be passed-on.
    * In case both a short and long name are passed on, the short name will be
      transfered to subprocess, and the long name will be used by epycs.
    * In case an overloaded argument is set to None, it is ignored.

    TL;DR: if you plan on using your script with arbitrary python versions,
    be verbose and use the long name.

    The list of epycs arguments is

    * `quiet`: The output is hidden unless the call fails, at which point it is
               output to the stderr.
    * `out_filter`: The output is parsed with the given filter.
                    A filter is defined as a function
                    :py:`filt(s : string) -> arbitrary_object` that is provided
                    with the string output of the program call.
                    This option implies that stdout is captured.
    * `additional_env`: The given dictionnary is passed-on as additional env to
                        the current env.
    * `additional_pathenv`: Each key in the given dictionnary will be treated
           as an PATH-like environement variable which should be "enriched" by
           adding new entries.
           Most obvious use is to add elements to PATH, but it also works for
           java's CLASSPATH etc...
           Depending on the OS, an ';' or ':' is used as separator.
           The entries are added at the end of the current value.

    In this function we replace those in the entry kw with three operations:

    * getting the proper value for the overloaded argument, including solving
      cases of long vs short and undefined names
    * adding standards arguments to the subprocess call for the overloaded
      arguments to make more sense. Please note: this is done in
      a non-intrusive way, in that if you gave a value to those, it is kept,
      and a warning is printed.
    * removing all traces of the overloaded argument in the keyword list that
      is passed on to subprocess.
    """
    # quiet mode: no output unless the call fails
    # overriden by verbose global
    quiet = kw.get("quiet", False) and not verbose
    if "quiet" in kw:
        # subprocess would not be able to handle it
        del kw["quiet"]

    return quiet


class ShellProgramFilters:
    """
    Filters
    -------

    Available filters are

    * :py:`text(s : str) -> s : str`
    * :py:`text_lines(s : str) -> s : list(str)`
    * :py:`json(s : str) -> json`
    * :py:`xml(s : str) -> etree.ETree`
    * :py:`csv(s : str) -> list(list)`
    * :py:`csv_dict(s : str) -> {}`  *NB*: first line is taken as header
    * :py:`filelist(s : str) -> list(pathlib.Path)`
    * :py:`file_and_lines_list(s : str) -> list(epycs.PathAndLine)`
    * :py:`diff(s : str) -> list(epycs.PathLineInLineOut)`
    """

    @classmethod
    def find(cls, name_or_callable):
        return (
            name_or_callable
            if callable(name_or_callable)
            else getattr(cls, str(name_or_callable).lower())
        )

    @classmethod
    def text(cls, s):
        return s

    @classmethod
    def text_lines(cls, s):
        return s.splitlines()

    @classmethod
    def json(cls, s):
        import json

        return json.loads(s)

    @classmethod
    def xml(cls, s):
        import xml.etree.ElementTree

        return xml.etree.ElementTree.fromstring(s)

    @classmethod
    def csv(cls, s):
        import csv

        return list(csv.reader(io.StringIO(s)))

    @classmethod
    def csv_dict(cls, s):
        import csv

        return list(csv.DictReader(io.StringIO(s)))


def escaped_str(string_convertible):
    s = str(string_convertible)
    return f'"{s}"' if re.match(r"\s", s) else s


OS_PATHENV_SEP = ";" if os.name == "nt" else ":"


def str_args(args):
    """
    Transform the arguments into a list of strings.
    """
    return [str(a) for a in args]


def run(
    exe,
    *args,
    out_filter=None,
    additional_env={},
    additional_pathenv={},
    **kw,
):
    cmd = [exe] + str_args(args)
    cmd_str = " ".join(escaped_str(c) for c in cmd)

    quiet = extract_overloaded_kw(kw)

    exe_env = os.environ.copy()
    exe_env.update(additional_env)
    for k, v in additional_pathenv.items():
        prevenv_txt = exe_env.get(k, "")
        if prevenv_txt != "":
            prevenv = prevenv_txt.split(OS_PATHENV_SEP)
        else:
            prevenv = []
        exe_env[k] = OS_PATHENV_SEP.join(prevenv + v)

    exe_kw = {}

    if quiet:
        exe_kw["stdout"] = subprocess.PIPE
        exe_kw["stderr"] = subprocess.STDOUT
    delayed_quiet_stderr = quiet

    if out_filter:
        exe_kw["stdout"] = subprocess.PIPE

    if verbose:
        print("+", cmd_str, file=sys.stderr)

    # user-defined argument always take precedence
    exe_kw.update(kw)

    r = subprocess.run(cmd, **exe_kw, env=exe_env)

    if r.returncode:
        if delayed_quiet_stderr:
            print(r.stdout, file=sys.stderr, end="")

        if exit_on_error:
            sys.exit(r.returncode)
    elif out_filter:
        r = ShellProgramFilters.find(out_filter)(r.stdout)

    return r


class ShellProgram:
    def __init__(self, exe, *args, **kw):
        self.exe = exe
        self.prefix_a = str_args(args)
        self.default_kw = {"text": True}
        self.default_kw.update(kw)

    def copy(self):
        return ShellProgram(self.exe, *self.prefix_a, **self.default_kw)

    def __call__(self, *args, **kw):
        ckw = self.default_kw.copy()
        ckw.update(kw)
        return run(self.exe, *(self.prefix_a + str_args(args)), **ckw)

    def arg(self, *args):
        r = self.copy()
        r.prefix_a += str_args(args)
        return r

    def with_default_kw(self, **kw):
        r = self.copy()
        r.default_kw.update(kw)
        return r

    def __str__(self):
        astr = " ".join(escaped_str(c) for c in self.prefix_a)
        return f"{self.exe} {astr} <args>"


def which(program):
    """
    Shamelessly stolen and adapted from
    https://stackoverflow.com/a/377028/647828
    """

    def is_exe(fpath):
        return fpath.is_file() and os.access(fpath, os.X_OK)

    parts = epycs.path.parts(program)
    program = Path(program)  # /!\ throws away any "./" prefix
    if len(parts) > 1:
        # given an executable with its path, no PATH search
        if is_exe(program):
            return program
        else:
            return None

    for path in os.environ["PATH"].split(os.pathsep):
        exe_file = Path(path) / program
        if is_exe(exe_file):
            return exe_file

    return None


def find_program(name, *aliases):
    p = which(name)

    if not p:
        for a in aliases:
            p = which(a)

            if p:
                break

        if not p:
            raise ShellProgramNotFoundError(f"{name} and its aliases {aliases}")
    return ShellProgram(p)


class MagicCommandsShell:
    def __getattr__(self, name):
        return find_program(name)


def command_property(f):
    return property(lru_cache(maxsize=1)(f))


class PredefinedCommandsShell(MagicCommandsShell):
    @command_property
    def editor(self):
        return getattr(self, os.environ.get("EDITOR", "vi"))

    @command_property
    def shell(self):
        return getattr(self, os.environ["SHELL"])

    @command_property
    def python(self):
        return getattr(self, sys.executable)

    @command_property
    def env(self):
        return find_program("env").with_default_kw(out_filter="text_lines")


cmd = PredefinedCommandsShell()
