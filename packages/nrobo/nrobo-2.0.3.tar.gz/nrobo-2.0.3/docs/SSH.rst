SSH
===

Generating a new SSH key
------------------------

1. Open terminal
2. Paste the text below, substituting in your GitHub email address
   - `ssh-keygen -t ed25519 -C "your_email@example.com"`

Adding your SSH key to the ssh-agent
------------------------------------

1. Ensure the ssh-agent is running. You can use the "Auto-launching the ssh-agent" instructions in "Working with SSH key passphrases", or start it manually:
    - `start the ssh-agent in the background`
      - `eval "$(ssh-agent -s)"`
      - `> Agent pid 59566`
2. Add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_ed25519 in the command with the name of your private key file.
   - `ssh-add ~/.ssh/id_ed25519`

    