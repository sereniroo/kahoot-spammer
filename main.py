#! /usr/bin/python3
from selenium.webdriver import Chrome, ChromeOptions

from time import sleep
import sys, random
import threading

if len(sys.argv) != 3:
    print("Usage: kahootspam.py <game pin> <number of bots>")
    sys.exit()

options = ChromeOptions()
options.binary_location = '/usr/bin/chromium'
options.add_argument('headless')

numofthreads = int(sys.argv[2])
driver_count = 0
pin_count = 0
username_count = 0
done_count = 0

def new_game(i):
    """Launches a new kahoot login with selenium
    new_game(<number to display on error>)"""
    global driver_count, pin_count, username_count, done_count
    driver = Chrome(chrome_options=options)
    driver.get('https://kahoot.it/')
    driver_count+= 1
    sleep(3)
    try:
        driver.find_element_by_id('inputSession').send_keys(sys.argv[1])
        driver.find_element_by_class_name('btn-greyscale').click()
        pin_count+= 1
        sleep(3)
        driver.find_element_by_id('username').send_keys(str(random.randint(0,1000000000)))
        username_count+= 1
        driver.find_element_by_class_name('btn').click()
        done_count+= 1
    except TypeError:
        print("Thread #%i has errored!" % i)

def spawn(numofthreads):
    threads = []
    for i in range(numofthreads):
        threads.append(threading.Thread(target=new_game, args=[i]))
        threads[-1].start()
        print("\r[%i/%i] Starting threads" % (i+1, numofthreads), end='')

spawn(numofthreads)
print()

while driver_count < numofthreads:
    sleep(1)
    print("\r[%i/%i] Starting webdriver" % (driver_count, numofthreads), end='')
while pin_count < numofthreads:
    sleep(1)
    print("\r[%i/%i] Entering game pin." % (pin_count, numofthreads), end='')
while username_count < numofthreads:
    sleep(1)
    print("\r[%i/%i] Entering in nickname" % (username_count, numofthreads), end='')
while done_count < numofthreads:
    sleep(1)
    print("\r%i/%i threads done.      " % (done_count, numofthreads), end='')

input('\n[*] Press enter to exit')
