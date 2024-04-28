import os

def main():
    path = "./images"
    #count = 1

    for root, dirs, files in os.walk(path):
        count = 1
        for i in files:
            os.rename(os.path.join(root, i), os.path.join(root, str(count) + ".jpg"))
            count += 1
if __name__ == '__main__':
    main()
