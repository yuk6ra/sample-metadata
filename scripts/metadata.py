import random
import json
import string

# ENV Settings
while True:
    METADATA_TYPE = int(input("Metadata Type: (Unrevealed:0, Revealed:1): "))
    if METADATA_TYPE == 0:
        print("Set Unrevealed...")
        DATA_FOLDER_NAME = "unrevealed"
        break
    elif METADATA_TYPE == 1:
        print("Set Revealed...")
        DATA_FOLDER_NAME = "revealed"
        break

MAIN_PATH = f'../metadata'
SAVE_DATA_PATH = f'{MAIN_PATH}/{DATA_FOLDER_NAME}'

# Metadata Settings
SUPPLY = 10
DOMAIN = "metadata.prtcl.xyz"
IMAGE_URI = f"https://{DOMAIN}/images"
DESCRIPTION = "test"


def main():
    image = IMAGE_URI
    description = DESCRIPTION

    for token_id in range(0, SUPPLY):
        metadata = create_metadata(token_id)
        output(metadata, token_id)


def output(data, token_id):

    template = open(f'../templates/{DATA_FOLDER_NAME}.json', 'r')

    reader = string.Template(template.read())
    json = reader.safe_substitute(data)

    with open(f'{SAVE_DATA_PATH}/{token_id}.json', mode='w') as file:
        file.write(json)

    with open(f'{SAVE_DATA_PATH}/{token_id}', mode='w') as file:
        file.write(json)


def create_metadata(token_id):

    if METADATA_TYPE == 0:
        name = f"Unrevealed #{token_id}"
        image = f"{IMAGE_URI}/{DATA_FOLDER_NAME}/0.png"  # Only 0.png

        data = {
            "name": name,
            "image": image,
            "description": DESCRIPTION,
        }
        return data

    elif METADATA_TYPE == 1:
        name = f"Revealed #{token_id}"
        image = f"{IMAGE_URI}/{DATA_FOLDER_NAME}/{token_id}.png"

        data = {
            "name": name,
            "image": image,
            "description": DESCRIPTION,

            "trait_type_1": "Trait",
            "trait_type_2": "Trait",
            "trait_type_3": "Trait",
            "trait_type_4": "Trait 4",
            "trait_type_5": "Trait 5",

            "value_1": f"{token_id + 1}",
            "value_2": f"{token_id + 2}",
            "value_3": f"{token_id + 3}",
            "value_4": f"value 4_{token_id % 4}",
            "value_5": f"value 5_{token_id % 5}",

        }
        return data


if __name__ == '__main__':
    main()

