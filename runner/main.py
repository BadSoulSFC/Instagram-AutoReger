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

class runner:
    def __init__(self, driver, name, password, username, email):
        self.name = name
        self.password = password
        self.username = username
        self.email = email
        
        self.driver = driver

class main_functions: 
    def passwdgen() -> str:
        available_chars = "!@#$%^&*()_+-=01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        return "".join(random.sample(available_chars, random.randint(8, 12)))
    
    def usrnamegen(pre_genname: str) -> str:
        available_chars = "_01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        temp2 = "".join(random.sample(available_chars, random.randint(3, 5))) 
        return pre_genname.replace(" ", "_") + temp2

def run_proc() -> None:
    runner.name = names.get_full_name() # Get random name from names lib.
    runner.username = main_functions.usrnamegen(runner.name) # Generate a userame everytime using the same password gen function with tweaks
    runner.password = main_functions.passwdgen() # Generate a password everytime using a function
    runner.email = "example@example.com" # Get an email from a premade txt file.

    print(
        "\nUsername: ", runner.username,
        "\nPassword: ", runner.password,
        "\nFull Name: ", runner.name,
        "\nEmail: ", runner.email
          )
        
    runner.driver = uc.Chrome(headless=True, use_subprocess=False) # Init the driver.
    runner.driver.get('https://www.instagram.com/accounts/emailsignup/') # Go to the sign up page.
    time.sleep(1)
    runner.driver.close()
    runner.driver.quit()
        

if __name__ == "__main__":
    run_proc()
