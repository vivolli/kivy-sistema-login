import datetime
import os

class DataBase:

    def __init__(self, filename):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(base_path, filename)
        
        if not os.path.exists(self.filename):
            self.filename = filename
        
        self.users = None
        self.file = None
        self.load()

    def load(self):
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()
        
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            if line.strip():
                email, password, name, created = line.strip().split(";")
                self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        email = email.strip()

        if email not in self.users:
            self.users[email] = (
                password.strip(),
                name.strip(),
                DataBase.get_date()
            )
            self.save()
            return 1

        else:
            print("Email ja registrado")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(
                    user + ";" +
                    self.users[user][0] + ";" +
                    self.users[user][1] + ";" +
                    self.users[user][2] + "\n"
                )

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
