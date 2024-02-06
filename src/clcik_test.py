import click
from pathlib import PureWindowsPath
import os
@click.command()
@click.option('--name', default='umesh', help='The person to greet.')
def greet(name):
    click.echo(f'Hello, {name}!')
    test_path = os.path.join(".msde-train/train/", "{}/logs")
    os.environ["WS_LOG_FILES_PATH"] = test_path
    linux_path = str(PureWindowsPath(test_path).as_posix())

    print("linux path:" + linux_path)
    print("env variable value:" + os.environ["WS_LOG_FILES_PATH"])

if __name__ == '__main__':
    greet()
