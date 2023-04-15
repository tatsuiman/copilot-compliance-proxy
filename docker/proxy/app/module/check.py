import re
import yaml

def load_settings(filename):
    with open(filename, 'r') as f:
        settings = yaml.safe_load(f)
    return settings


def check_payload(payload, settings):
    # Check for ignored keywords
    for ignore_keyword in settings.get('ignore_keywords', []):
        if ignore_keyword in payload:
            raise ValueError(f"Ignored keyword found: {ignore_keyword}")

    # Replace matching keywords
    for replace_keyword in settings.get('replace_keywords', []):
        pattern = re.compile(replace_keyword['keyword'])
        payload = pattern.sub(replace_keyword['replace'], payload)

    return payload
