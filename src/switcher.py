import pyautogui
import configparser
import time

class MonitorSwitcher:
    '''Simple object for switching show only mode between monitors.'''
    # Path to config file
    config_path = None

    def __init__(self):
        '''Initialise the object and read the config file.'''
        self._config_path = self.__class__.config_path
        self._config = configparser.ConfigParser() 
        self.active_display = self._get_active_display()

    def _get_active_display(self) -> int:
        '''Get the active display from the config file on init.'''
        self._config.read(self._config_path)
        # Return active display in config file if it exists
        if active_display := self._config['show_only_on']['active_display']:
            return int(active_display)
        # Return -1 if no config file value exists
        else:
            return -1

    def _update_active_display(self, display_num: int) -> None:
        '''Update the object and config active display values.'''
        self.active_display = display_num
        self._config.set(
            'show_only_on', 'active_display', str(self.active_display)

            )
        with open(self._config_path, 'w') as configfile:
            self._config.write(configfile)

    def switch(self, display_num: int = 0):
        '''
        Switch show only to another monitor.
        1 = Show only on main monitor.
        2 = Show only on secondary monitor.
        0 = Toggle based on current value in config file.
        ! If toggle is out of sync then specify 1 or 2 to reset.
        '''
        # Toggle active display if display_num is 0
        if display_num == 0:
            display_num = 2 if self.active_display == 1 else 1
        # Or default to main monitor if display_num is invalid
        elif display_num not in [0, 1, 2]:
            display_num = 1
        # Show only on specific monitor
        self.show_on_display_only(display_num)
        # Update the active display and config file
        self._update_active_display(display_num)

    def show_on_display_only(self, display_num: int):
        '''Show on main monitor only.'''
        # Press the Windows key + P to open display settings
        pyautogui.hotkey('win', 'p')
        # Wait for the display settings window to open
        time.sleep(1)
        # Press the end key to move to secondary option
        if display_num == 2:
            pyautogui.press('end')
        # Press the home key to move to main option
        else:
            pyautogui.press('home')
        # Press Enter to apply to select option
        pyautogui.press('enter')
        # Press Esc to exit the display menu
        pyautogui.press('esc')
        # Wait for display to change
        time.sleep(1)
        # Wait afor display settings to close
        time.sleep(1)
