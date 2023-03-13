import getpass
import os
import subprocess

# 1)Elevate your user access to root;

root_password = getpass.getpass("Enter the root password: ")

# Switch to the root user with the password
p = subprocess.Popen(['su', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(input=root_password.encode())

# Check if the root user was switched to successfully
if p.returncode != 0:
    print("Failed to login as root. Exiting.")
    exit()


# 2)add a new user to your Linux OS and set a password for it;

new_user = input("Enter a username for the new user: ")
password = input("Enter a password for the new user: ")
subprocess.run(['sudo', 'useradd', '-m', '-s', '/bin/bash', new_user])

subprocess.run(['sudo', 'chpasswd'], input=f"{new_user}:{password}".encode())

# Check if the user was created successfully
result = subprocess.run(['id', '-u', new_user], capture_output=True)
if result.returncode != 0:
    print(f"Failed to create user '{new_user}'.")
    exit()

print(f"User '{new_user}' was created successfully.")

# 3) Test if the user is able to log in
result = subprocess.run(f'sudo -u {new_user} whoami', shell=True, capture_output=True)
if result.returncode == 0:
    print(f"User '{new_user}' is able to log in.")
    print(f"Output: {result.stdout.decode()}")
else:
    print(f"Failed to log in as user '{new_user}'.")
    print(f"Error message: {result.stderr.decode()}")

# Using grep command check if the user is created
os.system(f'sudo grep {new_user} /etc/passwd')

# grep the UID of each user
os.system('sudo cat /etc/passwd | cut -d: -f1,3')

# Find out the GID of the created user
os.system(f'sudo grep {new_user} /etc/group')

# Change the password of the user and force it to change the pass on his next login
os.system(f'sudo passwd -e {new_user}')

# Add a new user and set an expiration date for it, with a five-day warning period
new_user2 = input("Enter a username for the new user with an expiration date: ")
os.system(f'sudo useradd {new_user2} -e 2023-03-17 -f 5')

# Create a new group
new_group = input("Enter a name for the new group: ")
os.system(f'sudo groupadd {new_group}')

# Assign the two new users to that group
os.system(f'sudo usermod -a -G {new_group} {new_user} {new_user2}')

# Lock one of the user accounts
os.system(f'sudo usermod -L {new_user}')

# Change the shell of one user to tcsh and ask to install it if it's not installed
shell_choice = input("Would you like to install tcsh? [y/n]: ")
if shell_choice.lower() == 'y':
    os.system('sudo apt install tcsh')
os.system(f'sudo chsh -s /bin/tcsh {new_user}')

# Make sure your home directory has “execute” access enabled for group and other
os.system(f'sudo chmod go+x /home/{new_user}')

# Change to your home directory, and create a directory called labs
os.system(f'cd /home/{new_user}; mkdir labs')

# Create an empty file in labs directory
os.system(f'cd /home/{new_user}/labs; touch file')

# Change permissions of file to rwx-rwx-rwx
os.system(f'sudo chmod 777 /home/{new_user}/labs/file')

# List the file. What color is the file?
os.system(f'ls -l /home/{new_user}/labs/file')

# Change the permissions back to rx-rw-rw
os.system(f'sudo chmod 644 /home/{new_user}/labs/file')

# Check what owners does the file have
os.system(f'ls -l /home/{new_user}/labs/file')

# Change the user ownership of the file to another user
new_owner = input("Enter the username of the new owner for the file: ")
os.system(f'sudo chown {new_owner} /home/{new_user}/labs/file')

# Create a group called group1 and assign two users to the group
os.system('sudo groupadd group1')
os.system(f'sudo usermod -a -G group1 {new_user} {new_user2}')

# Create a file called group1.txt and redirect below input into the file
os.system('sudo touch /home')

