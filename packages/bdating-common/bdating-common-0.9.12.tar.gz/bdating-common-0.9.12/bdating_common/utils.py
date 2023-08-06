import os
def is_env_true(env_key:str):
    env_value=os.environ.get(env_key)
    if env_value is None:
        return False
    env_value=env_value.strip().lower()
    if env_value.startswith('t') or env_value.startswith('y'):
        return True
    if env_value.isdigit():
        return False if env_value.replace('0', '')=='' else True # all constructed with 0
    return False