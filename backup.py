import subprocess

def git_add():
    result = subprocess.check_output(['git', 'add', '.'])
    print result

def git_register_removed():
    result = subprocess.check_output(['git', 'status'])
    not_staged_for_commit_deleted = []
    mode_not_staged_for_commit = False
    for e in result.splitlines():
        if '# Changes not staged for commit:' in e:
            mode_not_staged_for_commit = True
            continue
        elif '# Untracked files:' in e:
            mode_not_staged_for_commit = False
            continue
        if mode_not_staged_for_commit:
            if '#       deleted:' in e:
                not_staged_for_commit_deleted.append(e.split('# deleted:')[1].strip())
    for e in not_staged_for_commit_deleted:
        print subprocess.check_output(['git', 'rm', e])

def git_commit():
    print subprocess.check_output(['git', 'commit', '-m', 'backup'])

def git_push():
    print subprocess.check_output(['git', 'push'])

if __name__=="__main__":
    git_add()
    git_register_removed()
    git_commit()
    git_push()
