import json
import re

from itertools import groupby
from pprint import pprint, pformat

def condense_dicts(dicts):
    for d in dicts:
        del d["version"]
        yield d

def get_condensed_dicts(dicts):
    return list(condense_dicts(dicts))

with open("bruckner-3rd-versions.md") as fp:
    lines = [line[:-1] for line in fp]

lines = [line[3:] for line in lines[2:]]

VERSION_RE = \
    re.compile("(?P<conductor>\w+)\/(?P<orchestra>\w+):\s(?P<version>.+)")

performances = []

for line in lines:
    m = VERSION_RE.match(line)
    performances.append( {"version": m['version'], 
                          "conductor": m['conductor'], 
                          "orchestra": m['orchestra']} )

performances.sort(key=lambda d:d["version"])

grouped_performances = [(key, get_condensed_dicts(values)) for key, values 
                                        in groupby(performances, 
                                                   key=lambda d:d['version'])]

d = {"Symphony No. 3": grouped_performances}

print(d)
# formatted_json_string = pformat(d, indent=2, width=60, sort_dicts=True)
# print(formatted_json_string)

with open("my_bruckner_recordings.json", mode="w") as fp:
    json.dump(d, fp, indent=1)
