"""
 Start Code
"""

import sys
from rias.helper import loader


def main() -> None:
    """
    Simple Test Function
    """
    # Simple Test
    x = 0
    for i in sys.argv:
        print(f"{x} -> {i}")
        x += 1
    loader("compimage")


if __name__ == "__main__":
    main()
