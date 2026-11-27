# Teacher notes: Git and GitHub first lesson

Use [STUDENT_HANDOUT.md](STUDENT_HANDOUT.md) as the file to share. These notes are for a live 80–90 minute lesson. Students already know basic Python, so the code is intentionally small; the focus is Git.

## Suggested timing and what to say

| Time | Activity | Teaching point |
| --- | --- | --- |
| 0–10 min | Git versus GitHub | “Git is the history tool on your machine; GitHub hosts a copy online.” Ask: can Git work without internet? Yes. |
| 10–20 min | Setup and `git init` | Have everyone confirm `git --version` and create a fresh `git-practice` folder. On shared PCs, configure name/email locally inside the repo. |
| 20–35 min | First commit | Pause after `git status`, then after `git add`, then after `git commit`. Ask what changed at each pause. |
| 35–45 min | Second commit | Demonstrate `git diff` before staging and `git diff --staged` after. Ask students to predict what the second commit includes. |
| 45–60 min | GitHub publish | Create an empty remote repo, connect `origin`, push. Allow extra time for sign-in. |
| 60–80 min | Branch and PR | Create `add-goodbye`, commit, push, open PR, inspect Files changed. Merge only if time permits. |
| 80–90 min | Exit ticket | Ask for the add/commit/push distinction and inspect one student's history. |

## Board diagram

```text
working files ──add──> staging area ──commit──> local Git history ──push──> GitHub
     ▲                                  ▲                            │
     └──────────── edit                └──────── pull ──────────────┘
```

Use this to emphasize that saving a file, staging, committing, and publishing are separate actions. `git status` is the safest command for students to run whenever they are unsure what state they are in.

## Live demo checkpoints

1. After creating `hello.py`, `git status` should show an untracked file.
2. After `git add hello.py`, status should show it under changes to be committed.
3. After the first commit, status should say the working tree is clean, and `git log --oneline` should show one commit.
4. After editing, `git diff` should show the old print line removed and the two new lines added.
5. After pushing, the GitHub repo page should show the files and recent commits.
6. After pushing the feature branch, GitHub should offer a comparison or PR creation path.

## Questions and short answers

- **Why stage?** It lets you choose the exact content of the next commit.
- **Why commit messages?** They explain what changed in a snapshot.
- **Is a commit on GitHub immediately?** No; push it.
- **Is GitHub required to use Git?** No.
- **What is `origin`?** A local nickname for a remote URL, not a special website.
- **What is `main`?** The name of the primary branch in this exercise.
- **What is a PR?** A request to review and merge changes between branches on GitHub.
- **Is a PR the same as `git pull`?** No. The names are similar, but a PR is a GitHub collaboration feature; `git pull` updates a local branch from a remote.

## Common classroom snags

- **Student runs `git init` in the wrong folder:** Have them stop and show `pwd`/`Get-Location` and `git status`. Do not give a blanket delete command; inspect the folder first.
- **Git asks for identity:** On lab PCs, use `git config user.name` and `git config user.email` in the practice repo, without `--global`.
- **Student created README on GitHub:** The remote now has an extra initial commit. The simplest classroom recovery is often to create a new empty GitHub repo with another name and use its URL; inspect before changing an existing remote.
- **Authentication interrupts the lesson:** Students can complete every local step and show `git log --oneline`; publish later. Do not ask students to share tokens or passwords.
- **No PR button:** Confirm the feature branch was pushed and compare `add-goodbye` against `main` in the repository's Pull requests area.
- **Unsaved editor tab:** If `git status` shows no change, check that the Python file was saved.

## Optional 10-minute pair activity

Partner A creates a branch named `add-course`, adds `print("I am learning Git")`, commits, and explains each command aloud. Partner B checks `git status` and `git log --oneline`, then explains what a PR would show. Swap roles with another small change.

## Assessment

A student meets the core objective if they can show two local commits, explain add/commit/push in their own words, and identify their current branch. Online completion adds a visible GitHub repository and a PR from the feature branch.

## Sources checked

The command flow follows [Git's setup guide](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup), [Git's recording-changes guide](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository), [Git's branch documentation](https://git-scm.com/docs/git-switch), and [GitHub's repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [remote](https://docs.github.com/en/get-started/git-basics/managing-remote-repositories), and [authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github) documentation.
