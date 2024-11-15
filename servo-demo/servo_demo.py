import os
import time
import random
from colorama import Fore as color
from cmd import Cmd
from pyfiglet import Figlet
from joint_drive import JointDrive

class SubCmd1(Cmd):
    prompt = 'Level2# '

    def do_recover(self, args):
        pass

    def do_quit(self, args):
        return -1

class MyPrompt(Cmd):

    servo = JointDrive()

    def do_level2(self, args):
        sub_cmd = SubCmd1()
        sub_cmd.cmdloop()
        self.cmd_ui()

    def cmd_ui(self):
        os.system('cls')
        f = Figlet(font='slant')
        print(f.renderText('Servo Demo'))

        r = random.randint(0, 10)
        print('-' * f.width)

        print("*" + (' ' * 5) + 'Servo ID: %s' % self.servo.id)
        print("*" + (' ' * 5) + 'Firmware Version: %s' % -1)
        print("*" + (' ' * 5) + 'Return Delay Time: %s' % -1)
        print("*" + (' ' * 5) + 'Status Return Level: %s' % -1)
        print("*" + (' ' * 5) + 'Goal Position (radian): %s' % self.servo.get_angle())
        print("*" + (' ' * 5) + 'Moving Speed (rpm): %s' % self.servo.get_speed())
        print("*" + (' ' * 5) + 'Temperature: %s°C' % -1)

        print('-' * f.width)
        print()
        print('Use \'help\' to see available commands')

    def do_update(self, args):
        """update menu screen"""
        self.cmd_ui()

    def do_show(self, args):
        """
Documented commands (type help <topic>)
========================================
devices
"""
        def devices():
            print()
            print("Devices found:")
            print("-------------")
            print()

        if len(args) == 0 or args == '?' or args == 'help':
            print()
            print("Use \'? show\' to see available commands")
        elif args == 'devices':
            devices()

    def do_set(self, *args):
        """
Documented commands (type help <topic>)
========================================
id angle speed
    """
        _args = args[0].split(' ')

        if len(args) == 0:
            print()
            print("Use \'? set\' to see available commands")
        elif _args[0] == 'id':
            self.servo.id = int(_args[1])
        elif _args[0] == 'angle':
            self.servo.set_angle(float(_args[1]))
        elif _args[0] == 'speed':
            self.servo.set_speed(float(_args[1]))
        # self.cmd_ui()

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        os.system('exit')
        return -1
        # raise SystemExit

    def do_pytest(self, args):
        """Run predefined pytest"""
        myCmd = 'pytest -v'
        os.system(myCmd)

    def do_action(self, args):
        """Execute servo commands"""
        os.system('cls')
        f = Figlet(font='slant')
        print(f.renderText('Active Demo'))
        print('-' * f.width)

        for i in range(0, 6):
            r = random.randint(0, 1023)
            os.system('cls')
            print(f.renderText('Active Demo'))
            print('-' * f.width)
            print("*" + (' ' * 5) + 'Servo ID: %s' % self.servo.id)
            print("*" + (' ' * 5) + 'Firmware Version: %s' % -1)
            print("*" + (' ' * 5) + 'Return Delay Time: %s' % -1)
            print("*" + (' ' * 5) + 'Status Return Level: %s' % -1)
            print("*" + (' ' * 5) + 'Current Angle: ' + (color.LIGHTMAGENTA_EX + '%s' + color.RESET + ' rad') % r)
            print("*" + (' ' * 5) + 'Current Speed: ' + (color.LIGHTMAGENTA_EX + '%s' + color.RESET + ' rpm') % r)
            print("*" + (' ' * 5) + 'Temperature: ' + (color.LIGHTMAGENTA_EX + '%s' + color.RESET + '°C') % r)
            print('-' * f.width)
            time.sleep(0.4)
        self.cmd_ui()

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.cmd_ui()
    prompt.prompt = '>> '
    prompt.cmdloop()


