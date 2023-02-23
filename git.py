'''
git config --global user.name "Bhargavi Poyekar" - Sets the username

git config --global user.email bhargavi1poyekar@gmail.com - Sets email

git config --global init.default branch main- Sets default branch

$ git config -h -shows all options for that command (here config)

git help config - shows the manual for the command (here config)

$ cd c:/Users/bharg/OneDrive/Desktop/git - changed directory

$ git init - initialized git repository in the folder

git status- shows the status of the repository, tells which branch we are in, what files are not committed etc.

$ git add index.htm - tracks a file(here index.htm). After tracking git can detect changes in the file
After adding, it sits in staging

$ git rm --cached index.htm - untracks a file

.gitignore file to tell git which files to ignore and not track 

git add .
git add --all
git add -A
(all these above 3 commands track all the files present in the respository)

Committing a file:

creates a checkpoint, which makes it possible for us to go back to this point in future.

After committing, if there is any change in any of the file, it shows in the status, that the file has been modified

Now if you want to check what has been modified,use:
git diff - tells what changed, original text in red, updated text in green


3 environments:

working files(where you edit the file) --> staging (waiting to get committed) -> commit(log or history into the books)

if you are not ready to commit and bring a staged file back to working files,:
git restore --staged <filename>

git commit -a -m "message" - Skips the staging stage and directly commits

git rm "<filename>" -removes/deletes the file from repository, even from your pc.

can restore the deleted file- git restore "<filename"

$ git mv "KCC Logo.png" "Primary Logo.png" -> rename file

git log  (to see the commit history)

git log --oneline (shows abbreviated version of commit history)

git commit -m "Message" --amend (Updates the message of previous commit without having to commit again)


git log -p shows exactly what changed in all the commits 

We can go back to previous commits:

git reset <commit id num>


Create new branches- copy of main branch, where we can make changes without changiing the main branch
if we are satisfied with all the changes, we can then merge them back to original branch.

git branch <branchname>

git branch - shows all the branches and * tells which is the current branch

git switch <branchname> - switches to the other branch

once you switch to other branch, all the changes will happen in that specific branch, 
and the original master/main branch remained unchanged
if you switch back to master, you can see there is no change in the file.

to merge the branch with master -> 
git merge -m "message" <branchname>

git branch -d <branchname> (deletes the branch)

git switch -c <branchname> - creates new branch and switch to it

if you try to merge a branch, when main is also changed, you might face merge conflict, 
where you are in main/merge branch, you see head, and current in the file, where you can remove the conflict
by keeping what you want and save it, then commit it and then merge the file.
 

'''
