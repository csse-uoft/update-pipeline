import csv
import re


def escape_str(string: str, lower=True):
    """Generate an individual/class name that complies the ontology format."""
    if lower:
        string = string.lower()
    # string.replace('+', '_plus_')
    string.replace('<', '_lt_')
    string.replace('>', '_gt_')
    string = re.sub(r'[^-_0-9a-zA-Z]', '_', string)
    return re.sub(r'_-_|-_-|_+', '_', string)


def clean_description(description: str):
    description = re.sub(r'<.*?>|[^\u0009\u000A\u000D\u0020-\uD7FF\uE000-\uFFFD\u10000-\u10FFF]+', ' ', description)
    description = re.sub('&amp;', '&', description)
    description = re.sub('&nbsp;', ' ', description)
    description = re.sub('&lt;', '<', description)
    description = re.sub('&gt;', '>', description)
    description = re.sub(' +', ' ', description)

    return description.strip()


def is_bom(file_path):
    f = open(file_path, mode='r', encoding='utf-8')
    chars = f.read(4)[0]
    f.close()
    return chars[0] == '\ufeff'


def read_csv(csv_path: str, encoding=None):
    data = []
    if not encoding:
        encoding = 'utf-8-sig' if is_bom(csv_path) else 'utf-8'
    print(f'Loaded CSV "{csv_path}"; Encoding: {encoding}')
    with open(csv_path, encoding=encoding, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv(csv_path, data: list):
    with open(csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
