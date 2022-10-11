from pyfirmata import Arduino
import time

if __name__ == '__main__':
    board = Arduino('COM3')
    print('communication started')

while True:
    board.digital[8].write(1)
    time.sleep(1)
    board.digital[8].write(0)
    time.sleep(1)
