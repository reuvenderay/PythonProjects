__author__ = 'Reuven'
import sys


class GetInfo():

    def __init__(self):
        self.u_name = ""
        self.age = ""
        self.uid = ""

    def get_name(self):
        while self.u_name.isalpha() is False:
            self.u_name = raw_input("Please enter your name:")[:20]
            if self.u_name == "exit" or self.u_name == "quit":
                sys.exit()
        return self.u_name

    def get_age(self):
        while self.age.isdigit() is False or int(self.age) not in range(1, 120):
            self.age = raw_input("Please enter your age:")
            if self.age == "exit" or self.age == "quit":
                sys.exit()
        return self.age

    def get_user_id(self):
        while len(self.uid) != 6 or self.uid.isdigit() is False or int(self.uid) not in range(1, 1000000):
            self.uid = raw_input("Please enter your User ID:")
            if self.uid == "exit" or self.uid == "quit":
                sys.exit()
        return self.uid

    def print_info(self):
        name = self.get_name()
        age = self.get_age()
        uid = self.get_user_id()
        print "You are %s, aged %s. next year you will be %d, with user id %s, the next user is %s."\
            % (name, age, int(age)+1, uid, int(uid)+1)

if __name__ == "__main__":
    get_stuff = GetInfo()
    get_stuff.print_info()

