import yaml

with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)
    print(config)  # Should print the dictionary
