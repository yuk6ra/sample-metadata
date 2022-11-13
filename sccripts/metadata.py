import random
import json
import string

MAIN_PATH = f'..'
DATA_FOLDER_NAME = "metadata/"
SAVE_DATA_PATH = f'{MAIN_PATH}/{DATA_FOLDER_NAME}'

SUPPLY = 100
IMAGE_URI = ""
DESCRIPTION = "test"

def main():
    # supply = int(input("supply:"))
    # image = input("imageURI:")
    # animation_url = input("animationURI:")
    supply = SUPPLY
    image = IMAGE_URI
    description = DESCRIPTION

    for token_id in range(1, supply + 1):
        metadata = create_metadata(token_id, image, description)
        output(metadata, token_id)


def output(data, token_id):
    template = open('../templates/metadata.json', 'r')

    reader = string.Template(template.read())
    json = reader.safe_substitute(data)

    with open(f'{SAVE_DATA_PATH}/{token_id}', mode='w') as file:
        file.write(json)


def create_metadata(token_id, image, description):
    data = {
        "name": f"Sample {token_id}",
        "image": f"{image}/{token_id}",
        "description": description,
    }
    return data


if __name__ == '__main__':
    main()

