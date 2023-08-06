import requests
import os
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def __post_body(value: int, env: str):
    env = '*' if env is None else env
    return {
        "key": "BUILD_NUMBER",
        "value": str(value),
        "protected": False,
        "variable_type": "env_var",
        "masked": False,
        "environment_scope": env
    }


def bump_build_no():
    gitlab_token = os.getenv('GITLAB_TOKEN')
    instance = os.getenv('CI_API_V4_URL')
    if gitlab_token is None:
        eprint('Missing GITLAB_TOKEN environment variable')
        exit(127)

    environment = os.getenv('CI_ENVIRONMENT_NAME', '*')
    headers = {'PRIVATE-TOKEN': gitlab_token}
    project_no = os.getenv('CI_PROJECT_ID')

    x = requests.get(f'{instance}/projects/{project_no}/variables', headers=headers)
    if x.status_code == 403:
        eprint(f'Unauthorized! Make sure GITLAB_TOKEN has rights to access api')
        exit(403)
    latest_version = next(filter(lambda i: i['key'] == 'BUILD_NUMBER' and i['environment_scope'] == environment, x.json()), None)
    if latest_version is None:
        requests.post(f"{instance}/projects/{project_no}/variables", headers=headers,
                      json=__post_body(1, environment))
        return 1

    else:
        new_value = int(latest_version['value']) + 1
        requests.put(f"{instance}/projects/{project_no}/variables/BUILD_NUMBER?filter[environment_scope]={environment}", headers=headers,
                     json=__post_body(new_value, environment))
        return new_value


if __name__ == '__main__':
    bump_build_no()
