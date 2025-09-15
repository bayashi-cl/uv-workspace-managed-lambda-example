import nox

packages = [
    "example-lambda-a",
    "example-lambda-b",
    "example-common",
]


@nox.session(venv_backend="uv")
@nox.parametrize("package", packages)
def type_check(session: nox.Session, package: str) -> None:
    session.run_install(
        "uv",
        "sync",
        "--active",  # noxによって作成された仮想環境にパッケージを追加する
        "--frozen",
        f"--package={package}",  # 指定されたパッケージの依存関係のみをインストールする
    )
    session.run("mypy", "--strict", f"packages/{package}")
