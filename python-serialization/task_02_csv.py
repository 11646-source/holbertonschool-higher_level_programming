#!/usr/bin/python3
"""
Module: task_02_csv
Converts a CSV file into JSON format and saves it to data.json.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON format and save it to data.json.
    Returns True if successful, False otherwise.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False
