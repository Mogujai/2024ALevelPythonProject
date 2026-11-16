import tkinter as tk
import LoginScreen
from time import sleep


def logout(window):
    window.destroy()    #Destroying main window and returning to login screen
    sleep(1)
    LoginScreen.login()
    