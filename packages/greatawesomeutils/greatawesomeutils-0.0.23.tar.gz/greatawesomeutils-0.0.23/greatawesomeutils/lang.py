# import datetime
from datetime import datetime
from datetime import timedelta
import pytz
import errno
import json
import sys
import random
import pandas as pd
from time import sleep
import requests
from requests.exceptions import ReadTimeout
import traceback

import os
from .config import IS_DOCKER


def retry(func, retry_wait=None, retries=5):
    tries = 0
    while tries < retries:
        tries += 1
        try:
            created_result = func()
            return created_result
        except Exception as e:

            traceback.print_exc()

            if tries == retries:
                raise e

            print('Retrying')

            if retry_wait is not None:
                sleep(retry_wait)


def is_errors_instance(instances, error):
    for i in range(len(instances)):
        ins = instances[i]
        if isinstance(error, ins):
            return True, i
    return False, -1


def istuple(el):

    return type(el) is tuple


def ignore_errors(func, instances=None):
    try:
        created_result = func()
        return created_result
    except Exception as e:
        is_valid_error, index = is_errors_instance(
            instances, e)
        if not is_valid_error:
            raise e
        print('Ignoring')
        traceback.print_exc()


def retry_if_is_error(func, instances=None, retries=2, wait_time=None):
    tries = 0
    errors_only_instances = list(
        map(lambda el: el[0] if istuple(el) else el, instances))

    while tries < retries:
        tries += 1
        try:
            created_result = func()
            return created_result
        except Exception as e:
            is_valid_error, index = is_errors_instance(
                errors_only_instances, e)

            if not is_valid_error:
                raise e

            traceback.print_exc()

            if istuple(instances[index]):
                instances[index][1]()

            if tries == retries:
                raise e

            print('Retrying')

            if wait_time is not None:
                sleep(wait_time)


def keep_doing(func, wait=1):
    while True:
        func()
        sleep(wait)


def silentremove(filename):
    try:
        os.remove(filename)
        return True
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
        else:
            return False


def sleep_if_docker(n):
    if IS_DOCKER:
        sleep(n)
    return


def is_windows():
    return os.name == 'nt'


def get_range(_from, _to):
    return ",".join(map(str, list(range(_from, _to))))


def find_ip():
    url = 'https://checkip.amazonaws.com/'
    try:
        response = requests.get(url, timeout=10)
        return (response.text).strip()

        # requests.exceptions.ReadTimeout
    except ReadTimeout:
        return None
    except Exception:
        traceback.print_exc()
        return None


def get_valid_ip():
    ip = find_ip()
    while ip is None:
        ip = find_ip()
    return ip


def find_by_key(ls,  key, value):
    for index in range(len(ls)):
        user = ls[index]
        if user[key] == value:
            return user


def find_by_id(ls, id):
    return find_by_key(ls, 'id', id)


def remove_nones(list):
    return [element for element in list if element is not None]


def write_json(path, data, indent=4):
    with open(path, 'w') as fp:
        json.dump(data, fp, indent=indent)


def write_temp_json(data, indent=4):
    path = './temp.json'
    print('Writing ./temp.json')
    with open(path, 'w') as fp:
        json.dump(data, fp, indent=indent)


def read_json(path):
    with open(path, 'r') as fp:
        users = json.load(fp)
        return users


def read_file(path):
    with open(path, 'r') as fp:
        data = fp.read()
        return data


def write_file(path, data):
    with open(path, 'w', encoding="utf-8") as fp:
        fp.write(data)


def write_html(path, data):
    with open(path, 'w', encoding="utf-8") as fp:
        fp.write(data)


def read_html(path):
    with open(path, 'r', encoding="utf-8") as fp:
        data = fp.read()
        return data


def append_file(path, data):
    with open(path, 'a') as fp:
        fp.write(data)


def exit_with_failed_status():
    print('Exiting with status 1')
    sys.exit(1)


def crash():
    sleep(5)
    return 5/0


def wait_for_enter(message="Press Enter To Continue..."):
    input(message)


HOUR_SECONDS = 3600


def sleep_for_n_seconds(n):
    print(f"Sleeping for {n} seconds...")
    sleep(n)


def on_exception(f, on_exception):
    try:
        f()
    except Exception as e:
        print(e)
        on_exception()


def is_time_passed(end_watch_time):
    now = datetime.now()
    return now > end_watch_time


def is_time_passed_in_utc(utc_end_watch_time):
    now = get_time_in_utc()
    return now > utc_end_watch_time


def get_time_in_utc():
    return datetime.now(tz=pytz.utc)


def calc_end_watch_time(seconds):
    watch_time = timedelta(seconds=seconds)
    start_watch_time = datetime.now()
    end_watch_time = start_watch_time + watch_time
    return end_watch_time


datetime_format = '%Y-%m-%d %H:%M:%S'


def str_to_datetime(when):
    return datetime.strptime(
        when, datetime_format)


def datetime_to_str(when):
    return when.strftime(datetime_format)


def datetime_file_safe_format(when):
    fmt = '%Y-%m-%d_%H-%M-%S'
    return when.strftime(fmt)


def timezoned_datetime_to_utc(unawaretime, timezone):

    pythztimezone = pytz.timezone(timezone)

    localized_timestamp = pythztimezone.localize(unawaretime)
    new_timezone_timestamp = localized_timestamp.astimezone(pytz.utc)
    return new_timezone_timestamp


def utc_to_timezoned_datetime(utctime, timezone):
    pythztimezone = pytz.timezone(timezone)
    return utctime.astimezone(pythztimezone)


def country_code_to_time_zone(code):
    result = pytz.country_timezones[code]

    if code == 'US':
        # todo: choose prefferd  timezone for us
        pass

    assert (len(result) == 1)

    return result[0]


def merge_list_of_dicts(dicts):
    result = []
    for i in range(len(dicts[0])):
        el = {}
        for each_dict in dicts:
            el.update(each_dict[i])
        result.append(el)
    return result


def merge_dicts_in_one_dict(dicts):
    el = {}
    for each_dict in dicts:
        el.update(each_dict)
    return el


def wrap_with_dict(ls, key):
    def wrap(i):
        return {f'{key}': i}
    return list(map(wrap, ls))


def delete_from_dicts(ls, key):
    for x in ls:
        x.pop(key)
    return ls


def extract_from_dict(ls, key):
    return list(map(lambda i: i[key], ls))


def get_boolean_variable(name: str, default_value: bool = None):
    # Add more entries if you want, like: `y`, `yes`, ...
    true_ = ('True', 'true', '1', 't')
    false_ = ('False', 'false', '0', 'f')
    value = os.getenv(name, None)
    if value is None:
        if default_value is None:
            raise ValueError(f'Variable `{name}` not set!')
        else:
            value = str(default_value)
    if value.lower() not in true_ + false_:
        raise ValueError(f'Invalid value `{value}` for variable `{name}`')
    return value in true_


def pretty_print(result):
    print(json.dumps(result, indent=4))


def sleep_forever():
    print('Sleeping Forever')
    while True:
        sleep(100)


def flatten(l):
    return [item for sublist in l for item in sublist]


def partition(pred, iterable):
    trues = []
    falses = []
    for item in iterable:
        if pred(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses


def partition_by_percentage(percentage, iterable):
    N = len(iterable)
    split_point = round(N * percentage)
    return iterable[0:split_point], iterable[split_point:N]


def safe_pop(ls, index = 0):
        try:
          return ls.pop(index)
        except:
          return None

def safe_index(ls, index = 0):
        try:
          return ls[index]
        except:
          return None


def short_random_sleep():
    sleep_for_n_seconds(random.uniform(2, 4))

def long_random_sleep():
    sleep_for_n_seconds(random.uniform(7, 17))


def write_csv(data):
    df = pd.DataFrame(data)
    path = './result.csv'
    print(f'Writing {path}')
    df.to_csv(path, encoding='utf-8', index=False)

if __name__ == '__main__':
    # print(get_utc_time())
    # print(datetime.now())
    print(get_time_in_utc())
    # print(timezoned_datetime_to_utc(
    #     datetime(2001, 2, 3, 11, 59, 0), "Asia/Kolkata"))
    # FROM = 62
    # TO = 82
    # print(get_range(FROM, TO))
    # print('N: ', len(range(FROM, TO)))
