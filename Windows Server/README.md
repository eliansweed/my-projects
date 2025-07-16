# Purpose
This script is designed to automate the creation of user accounts in a Windows Server environment using a batch (.txt or .bat) script.

# How It Works
The script contains a list of commands that create local or domain user accounts using the `dsadd user` command. Each line in the script adds a user with a specified username and password.

# Usage Instructions
1. Copy the script into a `.bat` file, e.g., `create-users.bat`.
2. Run the script with administrative privileges on the Windows Server.
   - Right-click the file and choose **"Run as administrator"**.
3. The specified users will be created on the system.

# Notes
- Replace `usernameX` and `passwordX` with actual usernames and secure passwords.
- For domain users, use PowerShell or modify the script to use Active Directory cmdlets.
- This script is intended for local user creation on the server.

# Author
[Elian Sweed]
