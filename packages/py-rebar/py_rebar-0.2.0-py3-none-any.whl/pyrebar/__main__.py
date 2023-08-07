"""Initialize and run the application."""
import sys
from .application import main


def run_main():
    """Run the main application."""
    rc = main()
    sys.exit(rc)


if __name__ == "__main__":
    run_main()
