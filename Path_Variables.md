# Mac PATH Variables
- Add terminal commands by exporting PATH variables
- Update Python to new versions using alias
- Review how to find pathname variables

## Export PATH to Add Commands
1. Open your `.bash_profile`. The easiest way to do this is by revealing hidden files in your home directory using `Cmd + Shift + .`, and graphically double-clicking the .`bash_profile` to open it. <br>
If that doesn't work for you, try the command `sudo nano .bash_profile` and enter your password to open `.bash_profile` as an administrator.

2. Once `.bash_profile` is open, make sure your PATH is set up properly. It should look like this before you change anything:
```
PATH=/bin:/usr/bin:/usr/local/bin:${PATH}
export PATH
```

If your path doesn't already look like this, just copy and paste the above into your `.bash_profile`.

3. To export a new PATH variable and create a new command, use this format and fill in the directory containing the application or information you want to create a command for:
```
export PATH=$PATH:<insert your new directory here>
```

Example: I want to export my PATH for the Luau langague, which is stored here: `/Users/shifraisaacs/.luau/luau`. I take that directory (`/Users/shifraisaacs/.luau`), and export the PATH variable:
```
export PATH=$PATH:/Users/shifraisaacs/.luau
```

Now, I can use `luau` as a terminal command. <br><br>

4. Open your terminal and type `source .bash_profile` to activate the new PATH variable.

5. To make sure everything is working, type your new command to. Also try a basic command like `ls` or `clear` to make sure this process didn't eliminate old commands. If the `ls` command is not found, go back to Step 1 to reset your PATH

### Update Python with Alias
1. Copy the pathname for your desired version of Python.

2. Create an alias for the command `python` with this command: `alias python=<pathname>`.

Example:
```
alias python=/usr/local/bin/python3.10
```

3. Check with `python --version` terminal command.

### Tip: Finding Your Directory
Click the object you want to export a PATH for with 2 fingers. Then, hold down the `option` key until you see `Copy Object as pathname`. <br>
Click on that and paste it into a PATH in `.bash_profile`. Everything before the final slash is the directory you should use for your PATH.