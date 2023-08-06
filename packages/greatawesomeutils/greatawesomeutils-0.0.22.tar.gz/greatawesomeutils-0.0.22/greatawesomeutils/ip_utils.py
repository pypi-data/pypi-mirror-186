from greatawesomeutils.lang import get_valid_ip

def has_ip_changed(initial_ip):
    curr_ip = get_valid_ip()
    print("Current IP is: ", curr_ip)
    return initial_ip != curr_ip


def wait_till_ip_change():
    initial_ip = get_valid_ip()

    while True:
        if has_ip_changed(initial_ip):
            ip = get_valid_ip()
            print(f"IP changed from {initial_ip} to {ip}.")
            return ip


if __name__ == "__main__":
    print(has_ip_changed("192.0.0.1"))
