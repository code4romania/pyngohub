from ngohub.models.public import Version


def normalize_version(version_data: dict[str, str]) -> Version:
    normal_data = Version(**version_data)

    return normal_data
