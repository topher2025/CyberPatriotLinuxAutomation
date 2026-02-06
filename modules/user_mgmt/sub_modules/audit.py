from utils.scripts import run_script



def audit_users(expected_users):
    result = run_script("modules/user_mgmt/shell/list_users.sh")



def audit_groups(expected_groups):
    pass

