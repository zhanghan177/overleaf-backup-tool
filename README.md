# Overleaf backup tool
Tool for backing up projects from Overleaf.

## Modify made to base repo

The original repo is at: https://github.com/tbmihailov/overleaf-backup-tool.git
I have made the following modifications to enable a better support for:

- Support for protected projects
- Backups are listed by their name
- Modified storage file structure

## Installation
Works with Python 3.+

```bash
git clone https://github.com/zhanghan177/overleaf-backup-tool
cd overleaf-backup-tool
pip install -r requirements.txt
```

## Usage
```bash
python overleaf_backup.py backup_dir overleafuser@domain.com overleafpass
```

If you want to store your Overleaf credentials in environment variables, you could
```bash
cp app-env.example app-env
# Update credentails in app-env
source app-env

python overleaf_backup.py
```

## How it works
The tool logins with your Overleaf username and password and downloads all projects under "active" and "archived" via git.

You will find the cloned projects folders in backup_dir/git_backup/:

```text
your_backup_dir/
 ├── projects.json      # List of all projects
 ├── your-project-1-id
 │   ├── acl2018.bib
 │   ├── acl2018.sty
 │   ├── acl_natbib.bst
 │   ├── main.tex
 ├── your-project-2-id
 │   ├── acl2018.bib
 │   ├── acl2018.sty
 │   ├── acl_natbib.bst
 │   ├── main.tex
```

projects.json contains the metadata about the projects in Overleaf.
Successfully backed up projects will not be downloaded again if they are not changed in Overleaf.
