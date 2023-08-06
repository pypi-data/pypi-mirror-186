import os
IS_PRODUCTION = os.environ.get("ENV") == "production"
IS_DEVELOPMENT = not IS_PRODUCTION
IS_DIGITAL_OCEAN = os.environ.get("IS_DIGITAL_OCEAN") == 'True'


def is_docker():
    path = '/proc/self/cgroup'

    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
        or os.environ.get('KUBERNETES_SERVICE_HOST') is not None
    )


IS_DOCKER = is_docker()

TARGET_DIR = "production" if IS_PRODUCTION else "test"

TARGET_DIR_PARENT = 'digital-ocean-app-data' if IS_DIGITAL_OCEAN else 'app-data'
BASE_PATH = f'{TARGET_DIR_PARENT}/{TARGET_DIR}'
PROFILES_PATH = f'{BASE_PATH}/profiles'
SCREENSHOTS_PATH = f'{BASE_PATH}'

LOGS_PATH = f'../{BASE_PATH}/debug'

DB_PATH = f'{BASE_PATH}/app-data.db'

DOCKER_COMPOSE_YAML = f'docker-compose.yaml'
DOCKER_COMPOSE_YAML_FOR_VIDEOS = f'composes'
WAIT_DURATION = 20
WAIT_DURATION_SHORT = 10
WAIT_DURATION_VERY_SHORT = 5
WAIT_DURATION_VERY_VERY_SHORT = 2


RETRY_ATTEMPTS_LOW = 3
RETRY_ATTEMPTS_HIGH = 5

SECONDS_IN_MINUTES = 60

MASTER_API_URL = "http://master-srv:4000" if IS_DOCKER else "http://localhost:4000"
