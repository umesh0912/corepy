import logging
import argparse
from pathlib import Path

def main():
    print("hellow")
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tokentype', type=str, choices=["scv", "path"], default="path", help="ready snyk token from")
    args=parser.parse_args()

    print("token --> " + args.tokentype)
    print(Path.home())


if __name__ == "__main__":
    main()

