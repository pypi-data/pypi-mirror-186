GIT
===s

1. Configure your Git username/email
   - To set your global username/email configuration:
        - `git config --global user.name "FIRST_NAME LAST_NAME"`
        - `git config --global user.email "MY_NAME@example.com"`
2. To set repository-specific username/email configuration:
   - `git config user.name "FIRST_NAME LAST_NAME"`
   - `git config user.email "MY_NAME@example.com"`
   - `cat .git/config`
3. Set remote url
    - `git remote add origin https://github.com/USER/REPO.git`
    - `git remote -v`