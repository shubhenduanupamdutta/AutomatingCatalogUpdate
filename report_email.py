#!/usr/bin/env python3

import glob
import datetime
import reports
import emails

today = datetime.datetime.now().today().strftime("%B %d, %Y")
DIRECTORY_PATH = "./supplier-data/descriptions"
pdf_file = "/tmp/processed.pdf"


def get_additional_info(files: list) -> str:
    """Returns a string with additional information from the files."""
    additional_info = ""
    for file in files:
        with open(file) as f:
            additional_info += f"name: {f.readline().strip()}<br/>"
            additional_info += f"weight: {f.readline().strip()}<br/><br/>"
    return additional_info


def get_filepaths(directory: str) -> list:
    """Returns a list of text files in the directory"""
    return glob.glob(f"{directory}/*.txt")


if __name__ == '__main__':
    filepaths = get_filepaths(DIRECTORY_PATH)
    fruit_info = get_additional_info(filepaths)
    reports.generate_report(pdf_file, "Processed Update on {}".format(today), fruit_info)
    sender = "automation@example.com"
    receiver = "student-03-3c29cac2b57f@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = pdf_file
    message = emails.generate_email("automation@example.com", receiver, subject, body, attachment)
    emails.send_email(message)
