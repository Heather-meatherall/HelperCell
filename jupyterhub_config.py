import os, nativeauthenticator
# c = get_config()  # Initialize configuration object

c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.NativeAuthenticator.open_signup = True

user_file = '/srv/jupyterhub/jupyterhub/users.txt'

# Initialize sets to avoid errors if file is missing
allowed = {'admin'}

if os.path.exists(user_file):
    with open(user_file, 'r') as f:
        # Read lines, strip whitespace, and ignore empty lines
        file_users = {line.strip() for line in f if line.strip()}
        allowed.update(file_users)

c.Authenticator.allowed_users = allowed
c.Authenticator.admin_users = {'admin'}

def auto_authorize(authentication):
    if authentication['name'] in allowed:
        return True
    return False

c.NativeAuthenticator.import_from_config = True 


