import argparse
import json
import logging
import random
from pathlib import Path
import webbrowser

CONFIG_FILE_PATH = Path(__file__).parent / "config.json"


def main():
    args = parse_args()
    logger = logging.getLogger(__name__)
    if args.config:
        if not CONFIG_FILE_PATH.exists():
            CONFIG_FILE_PATH.touch()
        webbrowser.open(str(CONFIG_FILE_PATH))
        return
    if args.show_config_path:
        print(CONFIG_FILE_PATH)
        return
    alternatives = []
    try:
        with open(CONFIG_FILE_PATH) as config_file:
            alternatives = json.load(config_file)["alternatives"]
    except FileNotFoundError:
        logger.error(f"The config file '{CONFIG_FILE_PATH}' does not exist!")
        return
    except json.JSONDecodeError:
        logger.error(f"Failed to parse {CONFIG_FILE_PATH}!", exc_info=True)
        return

    if len(alternatives) == 0:
        logger.error(
            f"The config file {CONFIG_FILE_PATH} has no alternatives"
            " to choose from!"
        )

    alternative = random.choices(
        alternatives, weights=[a["weight"] for a in alternatives]
    )[0]
    webbrowser.open(alternative["link"])


def parse_args():
    parser = argparse.ArgumentParser(
        "Decide what to watch using the power of randomness!"
    )
    parser.add_argument("--config", action="store_true")
    parser.add_argument("--show-config-path", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    main()
