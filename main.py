from controller import *

def main():
    application = QApplication([])
    window = Television()
    window.show()
    application.exec_()

if __name__ == '__main__':
    main()

# https://youtu.be/PtneQf1pXk4 used as guide for images
# https://youtu.be/aP4q36l1m8U where the idea came from