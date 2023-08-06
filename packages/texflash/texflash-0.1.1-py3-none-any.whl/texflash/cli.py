import sys
from pathlib import Path
from streamlit.web import cli as stcli


def main() -> None:
    here = Path(__file__).resolve().parent
    file = str(here / "app.py")
    sys.argv = ["streamlit", "run", file]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
