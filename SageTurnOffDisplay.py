import ctypes
import time

# Define constants
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MONITOR_OFF = 2
MONITOR_ON = -1

# Get the handle to the primary monitor
hwnd = ctypes.windll.kernel32.GetConsoleWindow()

# Turn off the display
def turn_off_display():
    ctypes.windll.user32.SendMessageW(hwnd, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)
    print("Display turned off.")

# Turn on the display
def turn_on_display():
    ctypes.windll.user32.SendMessageW(hwnd, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)
    print("Display turned on.")

# Example usage
if __name__ == "__main__":
    print("Screen will turn off in 5 seconds...")
    time.sleep(5)       # Wait for 5 seconds
    turn_off_display()  # Turn off the display
