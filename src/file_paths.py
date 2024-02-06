import  subprocess

def main():
    print("in run!!!")
    subprocess.run('dir', shell=True)


if __name__ == "__main__":
    main()
