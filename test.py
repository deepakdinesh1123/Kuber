import io

import yaml

# Read YAML file
with open("data.yaml", "r") as stream:
    data_loaded = yaml.safe_load(stream)

print(data_loaded)
