import pytest
import epycs.subprocess as esp
from epycs.subprocess import find_program, OS_PATHENV_SEP, cmd

esp.verbose = True
esp.exit_on_error = True


ls = find_program("/usr/bin/ls", "ls")
pwd = find_program("pwd")
false = find_program("false")
echo = find_program("echo").with_default_kw(out_filter="text")
env = cmd.env
python = cmd.python


def test_echo():
    r = echo("hello, world!")
    assert r == "hello, world!\n"


def test_with_arg():
    r = echo.arg("a")("hello, world!")
    assert r == "a hello, world!\n"


def test_with_two_arg():
    r = echo.arg("a").arg("b")("hello, world!")
    assert r == "a b hello, world!\n"


def test_verbose_on_stderr(capsys):
    esp.verbose = True
    ls("-al", "/")
    captured = capsys.readouterr()
    assert captured.err == f"+ {ls.exe} -al /\n"
    assert captured.out == ""


def test_verbose_and_cwd(capsys):
    esp.verbose = True
    pwd(cwd="/")
    captured = capsys.readouterr()
    assert captured.err == f"+ {pwd.exe}\n"


def test_quiet_no_error(capsys):
    esp.verbose = False
    esp.exit_on_error = False
    python(
        "-c",
        """
import sys
print("hello", file=sys.stderr)
sys.exit(0)""",
        quiet=True,
    )
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


def test_quiet_and_stdout_tee_no_error(capsys):
    esp.verbose = False
    esp.exit_on_error = False
    python(
        "-c",
        """
import sys
print("hello", file=sys.stderr)
print("hello", file=sys.stdout)
sys.exit(0)""",
        quiet=True,
        stdout_tee=True,
    )
    captured = capsys.readouterr()
    assert captured.out == "hello\nhello\n"  # stderr (quiet) + stdout (stdout_tee)
    assert captured.err == ""


def test_not_quiet_no_error(capsys):
    esp.verbose = False
    esp.exit_on_error = False
    python(
        "-c",
        """
import sys
print("hello", file=sys.stderr)
sys.exit(0)""",
        quiet=False,
    )
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""
    # That is complicated: the subprocess will indeed print something
    # and you'll see it on the terminal but it is not captured by capsys
    # TODO find a better test


def test_quiet_error(capsys):
    esp.verbose = False
    esp.exit_on_error = False
    python(
        "-c",
        """
import sys
print("hello", file=sys.stderr)
sys.exit(1)""",
        quiet=True,
    )
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "hello\n"


def test_quiet_and_stdout_tee_error(capsys):
    esp.verbose = False
    esp.exit_on_error = False
    python(
        "-c",
        """
import sys
print("hello", file=sys.stderr)
print("hello", file=sys.stdout)
sys.exit(1)""",
        quiet=True,
        stdout_tee=True,
    )
    captured = capsys.readouterr()
    assert captured.out == "hello\nhello\n"  # stderr (quiet) + stdout (stdout_tee)
    assert captured.err == "hello\nhello\n"  # stderr + stdout (quiet, on error)
    # NB since stderr is redirected to stdout (quiet), there is no more way to capture
    # both separatly with this set of options


def test_no_exit_on_error():
    esp.exit_on_error = False
    r = false()
    assert r.returncode != 0


def test_exit_on_error():
    with pytest.raises(SystemExit, match=str(false().returncode)):
        esp.exit_on_error = True
        false()


def test_json_out_filter():
    js = echo('{"foo": "bar", "oof": 3}', out_filter="json")
    assert js["foo"] == "bar"
    assert js["oof"] == 3


def test_xml_out_filter():
    x = echo('<foo bar="yo"><oof>3</oof></foo>', out_filter="xml")
    assert x.tag == "foo"
    assert x.attrib == {"bar": "yo"}
    assert x[0].tag == "oof"
    assert x[0].text == "3"


def test_csv_out_filter():
    c = echo(
        """1,2,3
4,5,6""",
        out_filter="csv",
    )
    assert c == [["1", "2", "3"], ["4", "5", "6"]]


def test_csv_dict_out_filter():
    c = echo(
        """date,value,name
2021-05-13,100,Hercule
2021-05-14,90,Daphne""",
        out_filter="csv_dict",
    )
    assert c == [
        {"date": "2021-05-13", "value": "100", "name": "Hercule"},
        {"date": "2021-05-14", "value": "90", "name": "Daphne"},
    ]


def test_additional_env():
    r = {
        lines.split("=")[0]: lines.split("=")[1]
        for lines in env(additional_env={"TEST_FOR_EPYCS": "OK"})
    }
    assert r["TEST_FOR_EPYCS"] == "OK"


def test_additional_pathenv_from_empty():
    r = {
        lines.split("=")[0]: lines.split("=")[1]
        for lines in env(
            additional_env={"PATH": ""}, additional_pathenv={"PATH": ["/test"]}
        )
    }
    assert r["PATH"] == "/test"


def test_additional_pathenv_from_simple_composite():
    CLASSPATH_VAL = f"toto{OS_PATHENV_SEP}tata"
    r = {
        lines.split("=")[0]: lines.split("=")[1]
        for lines in env(
            additional_env={"CLASSPATH": CLASSPATH_VAL},
            additional_pathenv={"CLASSPATH": ["/test"]},
        )
    }
    assert r["CLASSPATH"].split(OS_PATHENV_SEP) == ["toto", "tata", "/test"]
