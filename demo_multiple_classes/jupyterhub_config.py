c = get_config()

# Our user list
c.Authenticator.whitelist = [
    'fabien',
    'corine',
    'pierre',
    'grader-techprog',
    'grader-progsoir'
]

c.Authenticator.admin_users = {
    'fabien',
    'corine'
}

# fabien and corine have access to different shared servers:
c.JupyterHub.load_groups = {
    'formgrade-techprog': [
        'fabien',
        'grader-techprog',
    ],
    'formgrade-progsoir': [
        'corine',
        'grader-progsoir'
    ],
    'nbgrader-techprog': [],
    'nbgrader-progsoir': []
}

# Start the notebook server as a service. The port can be whatever you want
# and the group has to match the name of the group defined above.
c.JupyterHub.services = [
    {
        'name': 'techprog',
        'url': 'http://127.0.0.1:9999',
        'command': [
            'jupyterhub-singleuser',
            '--group=formgrade-techprog',
            '--debug',
        ],
        'user': 'grader-techprog',
        'cwd': '/home/grader-techprog',
        'api_token': '{{techprog_token}}'
    },
    {
        'name': 'progsoir',
        'url': 'http://127.0.0.1:9998',
        'command': [
            'jupyterhub-singleuser',
            '--group=formgrade-progsoir',
            '--debug',
        ],
        'user': 'grader-progsoir',
        'cwd': '/home/grader-progsoir',
        'api_token': '{{progsoir_token}}'
    },
]

