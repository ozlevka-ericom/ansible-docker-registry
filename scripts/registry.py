#!/usr/bin/env python3

import json, argparse, os


CONFIG_FILE_NAME = "/etc/docker/daemon.json"
JSON_TEMPLATE = {
    "insecure-registries": []
}

def prepare_no_file(args):
    JSON_TEMPLATE["insecure-registries"].append(args.registry)
    with open(CONFIG_FILE_NAME, mode='w', encoding='UTF-8') as file:
        json.dump(JSON_TEMPLATE, file)


def make_json_file(args):
    if os.path.exists(CONFIG_FILE_NAME):
        with open(CONFIG_FILE_NAME, mode='r') as file:
            json_file = json.load(file)
        if "insecure-registries" not in json_file:
            json_file["insecure-registries"] = ["{}".format(args.registry)]
        elif args.registry not in json_file["insecure-registries"]:
            json_file["insecure-registries"].append(args.registry)

        with open(CONFIG_FILE_NAME, mode='w') as file:
            json.dump(json_file, file)
    else:
        prepare_no_file(args)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", required=True)

    args = parser.parse_args()
    make_json_file(args)


if __name__ == '__main__':
    main()