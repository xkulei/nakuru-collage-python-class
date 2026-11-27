# Git and GitHub: your first project history

**Level:** beginner · **Class time:** about 80–90 minutes · **You need:** Git, a text editor, Python, and a GitHub account for the online part.

## What you will learn

By the end, you should be able to explain Git versus GitHub, make two commits, publish a project to GitHub, create a branch, and open a pull request.

## 1. Git and GitHub are different

| Term | Plain meaning | Where it works |
| --- | --- | --- |
| **Git** | A tool that records versions of your project | On your computer, even without internet |
| **GitHub** | A website that hosts Git repositories and helps people collaborate | Online |
| **Repository (repo)** | A project folder whose changes Git tracks | Local or on GitHub |
| **Commit** | A named snapshot of staged changes | First stored locally |
| **Branch** | A separate line of work in the same repo | Local and/or on GitHub |
| **Remote** | A saved connection to another copy of the repo | Usually a GitHub URL |
| **Pull request (PR)** | A proposal to review and merge changes from one branch into another | On GitHub |

Think of **Git** as the history tool and **GitHub** as a place to share and discuss that history. A commit is not automatically uploaded to GitHub; `git push` sends it there.

```text
Your files → git add → staging area → git commit → local history
                                                   │
                                                   └─ git push → GitHub
```

The **staging area** is the set of changes you choose for the next commit. `git status` tells you what is untracked, changed, or staged.

## 2. Check Git and set your identity

Open a terminal. On Windows you can use PowerShell, Git Bash, or the VS Code terminal.

```bash
git --version
```

If the command is not found, install Git from [git-scm.com/downloads](https://git-scm.com/downloads/) and reopen the terminal.

On your **own computer**, tell Git what name and email to record in your commits. Replace the examples with your own details:

```bash
git config --global user.name "Amina Student"
git config --global user.email "amina@example.com"
```

On a **shared lab computer**, wait until you have created your practice repo in step 3, then set your identity **inside that repo** without `--global`:

```bash
git config user.name "Amina Student"
git config user.email "amina@example.com"
```

Check the values with `git config user.name` and `git config user.email`. The email can be a GitHub account email or your GitHub no-reply email if you use one. Do not type a password or access token into a file you plan to commit.

## 3. Make a new local repository

Use a **new, empty folder** for this exercise. The commands below create a folder called `git-practice`; do not run `git init` in a folder containing unrelated class files.

```bash
mkdir git-practice
cd git-practice
git init -b main
git status
```

`git init -b main` starts a repository and names its first branch `main`. Git creates a hidden `.git` folder to hold the history. `git status` tells you that there are no commits yet.

Now create a file named `hello.py` in this folder using your editor:

```python
print("Hello, Git!")
```

Run it with `py hello.py` on Windows or `python3 hello.py` on macOS/Linux. Then run:

```bash
git status
```

**Notice:** Git calls `hello.py` **untracked**. The file exists, but it is not in any commit yet.

## 4. Stage and commit your first version

```bash
git add hello.py
git status
git commit -m "Add first Python program"
git log --oneline
```

What each command does:

1. `git add hello.py` places the current contents of that file in the staging area.
2. `git status` now shows it under **Changes to be committed**.
3. `git commit -m "..."` records the staged version with a short message.
4. `git log --oneline` shows the recent history. Your commit has a short ID and your message.

**Important:** `git add` does not make a commit, and `git commit` does not upload to GitHub. Also, if you change a file *after* `git add`, run `git add` again to stage the newer contents.

## 5. Make a second version

Replace the contents of `hello.py` with:

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

Save the file. Then inspect and record the change:

```bash
git status
git diff
git add hello.py
git diff --staged
git commit -m "Greet the user by name"
git log --oneline
```

`git diff` shows changes in your working file that are **not yet staged**. After `git add`, `git diff --staged` shows what the next commit will contain. The history now has two commits.

**Quick check:** Can you tell a partner which line was removed and which lines were added?

## 6. Keep generated files out of Git

Create a file named `.gitignore` in `git-practice` with:

```text
__pycache__/
*.pyc
.venv/
.env
```

These patterns tell Git to ignore Python cache files, a common virtual environment folder, and a common local environment file. They do not erase files already tracked by Git. Commit your ignore rules:

```bash
git add .gitignore
git commit -m "Ignore local Python files"
```

## 7. Publish the repository to GitHub

1. Sign in at [github.com](https://github.com/).
2. Choose **New repository** (the **+** menu may also offer it).
3. Name it `git-practice`. Choose **Private** for a class exercise unless your teacher asks you to share it publicly.
4. **Do not** add a README, `.gitignore`, or license on GitHub for this exercise: your local repo already has its own history.
5. Create the repository and copy its HTTPS URL. It will look like `https://github.com/YOUR-USERNAME/git-practice.git`.

Back in the terminal, replace `YOUR-USERNAME` with your GitHub username:

```bash
git remote add origin https://github.com/YOUR-USERNAME/git-practice.git
git remote -v
git push -u origin main
```

`origin` is a conventional short name for the GitHub URL. `git remote -v` lets you check the address. `git push -u origin main` sends your local `main` branch to GitHub and sets it as the branch to push to by default in future. Refresh the GitHub page to see `hello.py`, `.gitignore`, and your commits.

GitHub may open a browser sign-in window when you push. Follow that flow. A normal GitHub account password is not used as a Git password in the terminal; GitHub documents credential managers, tokens, and SSH as command-line authentication options. **Never share a token or paste it into a project file.**

## 8. Make a branch and open a pull request

A branch lets you work on a change without immediately changing `main`.

```bash
git switch -c add-goodbye
```

Add this line to the end of `hello.py`:

```python
print("Thanks for trying my program!")
```

Then save, run the Python file, and commit the change:

```bash
git status
git add hello.py
git commit -m "Add goodbye message"
git push -u origin add-goodbye
```

On GitHub, open your repo. Look for **Compare & pull request**, or use **Pull requests → New pull request**. Set **base: `main`** and **compare: `add-goodbye`**. Give the PR a title such as `Add goodbye message` and describe what changed. Open the PR and review the **Files changed** tab.

Your instructor may ask you to merge it. If the PR is merged on GitHub, update your local `main` branch:

```bash
git switch main
git pull origin main
```

`git pull` brings the remote changes into your current local branch. Run `git log --oneline` to see the updated history. A PR is a place for review and discussion; opening it does not merge it automatically.

## 9. Command cheat sheet

| Command | Meaning |
| --- | --- |
| `git status` | What changed? What is staged? |
| `git add hello.py` | Stage this file's current contents |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git commit -m "message"` | Save staged changes in local history |
| `git log --oneline` | Show a short commit history |
| `git remote -v` | Show saved remote URLs |
| `git push` | Send local commits to a remote |
| `git pull` | Bring remote changes into the current branch |
| `git switch -c name` | Create and switch to a branch |
| `git switch main` | Switch to the `main` branch |
| `git clone URL` | Make a new local copy of an existing remote repo |

**Clone is different from pull:** `clone` creates a new local repo from a remote URL. `pull` updates a repo you already have. Do not clone your repo *inside* your existing `git-practice` folder.

## 10. Common problems

| Message or symptom | Likely cause | What to check |
| --- | --- | --- |
| `git` is not recognized | Git is not installed or terminal was open before installation | Install Git, reopen terminal, run `git --version` |
| `not a git repository` | Terminal is in the wrong folder | Run `pwd` (or `Get-Location` in PowerShell), then `cd` into `git-practice` |
| `Please tell me who you are` | Name/email not configured | Set `git config user.name` and `user.email` |
| `nothing to commit, working tree clean` | No new staged changes | Check the file was saved, then run `git status` |
| `remote origin already exists` | A remote named `origin` was added already | Run `git remote -v`; do not add it again |
| Push asks for a password or is denied | GitHub authentication is incomplete, or the URL/account is wrong | Check `git remote -v` and follow GitHub's sign-in guidance |
| Push rejected because remote has work you lack | GitHub and local histories differ | Ask your instructor to inspect the histories; avoid force pushing |

## 11. Exit ticket

Answer without looking at the cheat sheet:

1. What is the difference between Git and GitHub?
2. What is the difference between `git add`, `git commit`, and `git push`?
3. Why do we use a branch before a pull request?
4. Show your instructor your GitHub repo with at least two commits and a PR (or explain where you got stuck).

## Official references

- [Git: first-time setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
- [Git: recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [Git: switching branches](https://git-scm.com/docs/git-switch)
- [GitHub: creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
- [GitHub: remotes and pushing](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories)
- [GitHub: authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
