__author__ = 'Reuven'


def get_name():
    u_name = ""
    while u_name.isalpha() is False:
        u_name = raw_input("Please enter your name:")[:20]
        if u_name == "exit":
            return False
    return u_name


def get_age():
    age = ""
    while age.isdigit() is False or int(age) not in range(1, 120):
        age = raw_input("Please enter your age:")
        if age == "exit":
            return False
    return age


def get_user_id():
    uid = ""
    while len(uid) != 6 or uid.isdigit() is False or int(uid) not in range(1, 1000000):
        uid = raw_input("Please enter your User ID:")
        if uid == "exit":
            return False
    return uid


def print_info():
    name = get_name()
    if name is False:
        return
    age = get_age()
    if age is False:
        return
    uid = get_user_id()
    if uid is False:
        return
    print "You are %s, aged %s. next year you will be %d, with user id %s, the next user is %s."\
        % (name, age, int(age)+1, uid, int(uid)+1)

print_info()
