import os
import yaml
from subprocess import ( check_output )

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class GAM:

    def __init__(self):
        self.domain = None
        self.domain_config = None
        self.current_user_config = {}

    def go(self, domain, **kwargs):
        self.domain = domain
        self.get_domain_config()

        for user in self.domain_config['users']:
            self.process_user(user)

    def get_domain_config(self):
        domain_config_path = os.path.join(
            __location__,
            'mapping',
            f'{self.domain}.yml'
        )
        print(f"INFO: loading domain config {self.domain}")
        with open(domain_config_path) as stream:
            self.domain_config = yaml.safe_load(stream)

    def process_user(self, user):
        duration = '43200' # int cast as string for inclusion in string commands, treated as INT64 @ google
        h = os.environ.get('HOME')

        print(f"INFO: processing user - {user}")
        print(f" applying duration: {duration}")

        cmd = [
            f'{h}/bin/gam/gam',
            'update',
            'user',
            user,
            'SSO.duration',
            duration
        ]
        check_output(cmd)

        cmd = [
            f'{h}/bin/gam/gam',
            'update',
            'user',
            user
        ]

        if not self.domain_config['users'].get(user, []):
            print(f" removing all roles")
            cmd.extend(["SSO.role", "multivalued", ""])
        else:
            for role_dict in self.domain_config['users'][user]:
                role_string = f"{role_dict['role']},{role_dict['provider']}"
                print(f" applying role: {role_string}")
                cmd.extend(["SSO.role", "multivalued", role_string])
        check_output(cmd)

        print(f"INFO: DONE - {user}")
