import nox

@nox.session(reuse_venv=True)
def unit_tests(session):
    session.run("flit", "install", "--deps", "develop")
    session.run("pytest", "tests/unit")

@nox.session(reuse_venv=True)
def integration_tests(session):
    session.run("flit", "install", "--deps", "develop")
    session.run("pytest", "tests/integration")


@nox.session(reuse_venv=True)
def tests_with_coverage(session):
    session.run("flit", "install", "--deps", "develop")
    session.run("python", "-m", "pytest", "tests", "--cov=cli_help_maker", "--cov-report=term-missing", "--cov-config=pyproject.toml")


@nox.session
def format(session):
    session.run("flit", "install", "--deps", "develop")
    session.run("isort", "cli_help_maker", "examples", "tests")
    session.run("black", "cli_help_maker", "examples", "tests")
