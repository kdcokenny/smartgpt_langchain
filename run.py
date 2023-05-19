import subprocess


def main() -> None:
    """
    Run the Daphne server with the specified host, port, and FastAPI app.
    """

    subprocess.run(
        [
            "daphne",
            "-b",
            "0.0.0.0",
            "-p",
            "8000",
            "--websocket_timeout",
            "1200",
            "app.api.main:app",
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
