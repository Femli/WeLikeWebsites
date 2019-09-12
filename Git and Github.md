

### Step 0: Using git and GitHub
1. Download git [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Install it by running the program.
2. Create a GitHub account [here](https://github.com).

### Step 1: Creating a repo on your computer
1. Create a folder and name it.
2. Open the Terminal / Console and find the folder you created.
3. Create a repo in that folder using `git init` command.


### Step 2: Add a new file to the repo
1. Add a file to the repo you created.
2. git should have tracked the change in the repo (new file added). You can check changes made using `git status`.

### Step 3: Staging your repo
1. Commits in git make an official record of the change made in repos. That way you can always go back and restore your files.
2. Before you make a commit, first you must stage any changes made to a file using the `git add <file>` or stage all files using `git add .`
3. You can check the files added to the stage using `git status`.

### Step 4: Commit your repo
1. All files that are staged can now be committed using the `git commit` command.
2. Whenever we commit files, it's good practice to write about what is being committed. We can do this by `git commit -m “enter description here"`.

### Step 5: Sync local repos to GitHub
All repos stored in your computer are *local* repos. Repos that are stored on GitHub are *online* repos.
1. Create an online repo in your GitHub account; give it a proper name.
2. Open the Terminal / Console and find the local repo you created in your computer.
3. Sync your local repo to the GitHub repo using `git remote add origin https://github.com/User/Repo.git"`
    - Note that `User` should be your GitHub username, and `Repo` should be the name of your GitHub repo.
4. To complete the sync of repos, we must push the files in the local repo to the GitHub repo with the `git push -u origin` command.
5. Note that a “master branch” will be created. Don’t worry about that for now.
