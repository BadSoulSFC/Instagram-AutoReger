# MIT License

# Copyright (c) 2024 K

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import names
import random
import undetected_chromedriver as uc


def passwdgen() -> str:
    available_chars = '!@#$%^&*()_+-=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return "".join(random.sample(available_chars, random.randint(8, 12)))


def usrnamegen(gen_name: str) -> str:
    available_chars = "_01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rand_chars = "".join(random.sample(available_chars, random.randint(3, 5)))
    temp_modif = gen_name.replace(" ", "_")
    # I do not want to explain this shit.
    usrname = temp_modif[0:random.randint(int(len(temp_modif) / 2), len(temp_modif))] + rand_chars
    return usrname


# Just to not make a mess in the code.
def find_insert(driver, find_by: str, in_value: str, by_value: str) -> None:
    element = driver.find_element(by=find_by, value=by_value)
    if not in_value == '':
        print(f"Inserting value '{in_value}' into the {by_value} placeholder.")
        element.send_keys(in_value)


def main() -> None:
    name = names.get_full_name()  # Get random name from names lib.
    username = usrnamegen(name)  # Generate a username using the same password gen function with tweaks
    password = passwdgen()  # Generate a password everytime using a function
    email = "example@example.com"  # Get an email from a pre-made txt file.

    print(
        "-" * 35,
        "\nUsername: ", username,
        "\nPassword: ", password,
        "\nFull Name: ", name,
        "\nEmail: ", email,
        '\n' + "-" * 35,
        "\n"
    )
    driver = uc.Chrome(headless=False, use_subprocess=False)  # Init the driver.
    driver.get("https://www.instagram.com/accounts/emailsignup/")  # Go to the sign-up page.
    time.sleep(5)
    # Inserting an email.
    find_insert(
        driver=driver,
        find_by='name',
        in_value=email,
        by_value='emailOrPhone',
    )
    # Inserting a password.
    find_insert(
        driver=driver,
        find_by='name',
        in_value=password,
        by_value='password',
    )
    # Inserting a Full Name.
    find_insert(
        driver=driver,
        find_by='name',
        in_value=name,
        by_value='fullName',
    )
    # Inserting a username.
    find_insert(
        driver=driver,
        find_by='name',
        in_value=username,
        by_value='username',
    )

    time.sleep(1)
    driver.close()


if __name__ == "__main__":
    main()
