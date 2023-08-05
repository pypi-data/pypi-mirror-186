import toml


def get_toml(toml_path=r'./poos-config.toml'):
    return toml.load(toml_path)