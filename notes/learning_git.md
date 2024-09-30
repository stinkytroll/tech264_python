## Git vs GitHub
Git is a version control tool that is installed locally on your system. GitHub is a platform that offers a graphical 
interface that can let you can work together and share code by hosting your repos on there. 
It also had CI/CD pipeline tools such as project management software. 

## Types of Version Control
A VCS tracks changes to files over time, allowing multiple people to collaborate and revert to previous versions if necessary.

## When to Use One
- When collaborating on projects.
- To maintain a history of changes and revert to previous states.

## Benefits
- Tracks all changes and who made them.
- Helps with collaboration with multiple users.

# Types of Version Control
- Local Version Control – Stores on the local machine.
- Centralized Version Control (CVCS) – A central server that stores all version for users to check.
- Distributed Version Control (DVCS) – Peer to peer approach as opposed to client-side. 

## What is Manual Version Control?
- Saving different versions of a file manually in separate directories or with different names.
- Lacks sufficient tracking. 

# Centralised VCS vs Distributed VCS (like Git)
## Centralised 
- Users pull files from a central repo and all changes are stored on a central server.

## Distributed
- Users have a complete copy of repository to allow users to work online and mess around with stuff.

## Local Version Control with Git
- Only differences between version are stored as opposed to the entire file.
- Git can be used locally without pushing changes to a server.

## What Does Git Store in a 'Commit'?
- "Saves" and uploads the entire project with references and changes to the repo.

## The Three States in Git
### Modified
File has changes but not yet staged for a commit.
### Staged
Changes are ready to be committed.
### Committed
Changes are saved in the repository.

## Common Workflow of Git Commands
- git init – Initialise a new Git repository.
- git add – Stage changes for the next commit.
- git commit – Save changes in the repository.
- git push – Send local commits to a remote repository.
- git pull – Fetch and merge changes from a remote repository.

## Danger: If Sensitive Data is Accessible in a Previous Commit

**Problem**: Sensitive data can still be accessed from previous commits, even if removed in the latest commit.

### Solutions:

1. **Remove Previous Commits** (Risky):
   - Use `git reset` to remove the commits containing sensitive data. ⚠️ Be careful, this could result in losing work.
   
2. **Alternative Approach**:
   1. Delete the GitHub repository (makes the data safe).
   2. Remove the sensitive file from your local directory.
   3. Delete the `.git` folder from your local repository to remove all history.

---

## How to Remove Files You Don't Want to Commit

- **Folders starting with a dot** (`.`) are automatically ignored (e.g., `.git`).
- **.gitignore File**:
  - Use it to prevent files or folders from being committed.
  - Useful for ignoring:
    - Sensitive data like personal files, credentials, passwords.
    - Large files or unnecessary folders.
    - System files or IDE settings (e.g., `.idea`, `bin`, `out`).
  - **Note**: Files already committed will still appear in history.

---

## How to Remove Committed Files from Git History

1. Add files to `.gitignore` to prevent future commits.
2. Use the command:
   ```bash
   git rm --cached -r .idea
