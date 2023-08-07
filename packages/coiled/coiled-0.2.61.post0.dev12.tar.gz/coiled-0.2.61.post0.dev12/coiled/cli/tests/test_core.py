from coiled.cli.core import cli


def test_available_commands():
    assert set(cli.commands) == {
        "cluster",
        "login",
        "setup",
        "install",
        "upload",
        "env",
        "diagnostics",
        "package-sync",
        "curl",
    }
