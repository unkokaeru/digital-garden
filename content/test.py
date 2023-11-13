"""A script to check if I can fetch the environment variables"""

import os

print(os.environ['TEST_ENV_VAR'])

print(os.getenv('TEST_ENV_VAR'))