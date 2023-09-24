#!/usr/bin/env python3

import time
import shutil
import psutil
import socket
import smtplib
from email.message import EmailMessage


def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 80


def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_ram_usage():
    """Verifies that there's enough unused RAM"""
    available_ram = psutil.virtual_memory().available
    threshold = 500 * 1024 * 1024  # 500MB
    return available_ram > threshold


def check_localhost():
    """Verifies that the hostname "localhost" can be resolved to 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def check_computer_ok():
    """Checks that the CPU usage, disk usage, available memory and name resolution are OK"""
    checks = [
        (check_cpu_usage(), "Error - CPU usage is over 80%"),
        (check_disk_usage("/"), "Error - Available disk space is less than 20%"),
        (check_ram_usage(), "Error - Available memory is less than 500MB"),
        (check_localhost(), "Error - localhost cannot be resolved to 127.0.0.1")]
    for check in checks:
        if not check[0]:
            return check[1]
        else:
            return True


def send_mail(subject):
    """Sends an email with the given subject"""
    message = EmailMessage()
    message["To"] = "student-03-3c29cac2b57f@example.com"
    message["From"] = "automation@example.com"
    message["Subject"] = subject
    message.set_content("Please check your system and resolve the issue as soon as possible.")
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()


if __name__ == '__main__':
    everything_ok = check_computer_ok()
    if not everything_ok:
        send_mail(everything_ok)
