import os

from easy_tasks import help_with_json
from var_print import varp


def write_config_json():
    data = {
        "CHROME_PROFILE_USER_DATA": r"C:\Users\Creed\AppData\Local\Google\Chrome\User Data",
        "CHROMEDRIVER_PATH": None,
    }
    help_with_json.dump_as_json(
        data,
        r"C:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\GitHub\selenium_simplification\selenium_simplification\Chrome\config.json",
    )


def read_config_json():
    data = help_with_json.get_from_json(
        r"C:\Users\Creed\OneDrive\Schul-Dokumente\Programmieren\Python\GitHub\selenium_simplification\selenium_simplification\Chrome\config.json"
    )

    varp(data)
    # print(data)


if __name__ == "__main__":
    write_config_json()
    read_config_json()
