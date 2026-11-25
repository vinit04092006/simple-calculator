import re


def check_password_strength(password):
    problems = []

    if len(password) < 8:
        problems.append("at least 8 characters")
    if not re.search(r"[A-Z]", password):
        problems.append("at least 1 uppercase letter")
    if not re.search(r"[0-9]", password):
        problems.append("at least 1 number")
    if not re.search(r"[^A-Za-z0-9]", password):
        problems.append("at least 1 special character")

    return problems


def main():
    password = input("Enter a password: ")
    problems = check_password_strength(password)

    if len(problems) == 0:
        print("Strong")
    else:
        print("Weak")
        print("Your password needs:")
        for p in problems:
            print(f"- {p}")


main()
