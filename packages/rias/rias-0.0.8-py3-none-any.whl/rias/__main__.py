"""
 Start Code
"""
from hausbauen import startcode
import sys


def main() -> None:
    """
    Simple Test Function
    """
    user_data = sys.argv
    startcode()
    print(user_data)
    sys.exit(0)


if __name__ == "__main__":
    main()
