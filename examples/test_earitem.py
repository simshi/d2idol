import sys
import os

from lib import EarItem
from lib import OBitStream

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT_DIR, "output", "ear")


def generate_ear_simon():
    s = OBitStream()
    item = EarItem("Simon")
    item.writeStream(s)

    with open(os.path.join(DIR, "simon.d2i"), "wb") as f:
        s.writeBytes(f)


if __name__ == "__main__":
    os.makedirs(DIR, exist_ok=True)
    generate_ear_simon()
    print("Ear items generated successfully!")
