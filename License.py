import random

# ---------------- USER CLASS ----------------
class User:
    def __init__(self, name, age, test_passed):
        self.name = name
        self.age = age
        self.test_passed = test_passed

# ---------------- LICENSE SYSTEM ----------------
class LicenseSystem:
    def __init__(self):
        self.licenses = {}

    def check_eligibility(self, user):
        if user.age >= 18 and user.test_passed:
            return True
        return False

    def generate_license_number(self):
        return "DL-" + str(random.randint(10000, 99999))

    def issue_license(self, user):
        if self.check_eligibility(user):
            license_no = self.generate_license_number()
            self.licenses[user.name] = license_no
            print(f"✅ License Issued to {user.name}")
            print(f"🪪 License Number: {license_no}")
        else:
            print(f"❌ {user.name} is NOT eligible for a license.")

# ---------------- MAIN PROGRAM ----------------
system = LicenseSystem()

name = input("Enter your name: ")
age = int(input("Enter your age: "))
test = input("Did you pass driving test? (yes/no): ").lower()

test_passed = True if test == "yes" else False

user = User(name, age, test_passed)

system.issue_license(user)
