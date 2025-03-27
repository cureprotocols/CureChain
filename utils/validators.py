# validators.py
import json

REQUIRED_FIELDS = [
    "meta",
    "introduction",
    "methods",
    "results",
    "discussion",
    "conclusion",
    "references"
]

REQUIRED_META_FIELDS = ["title", "abstract"]

def validate_protocol_structure(data):
    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if "meta" in data:
        missing_meta = [field for field in REQUIRED_META_FIELDS if field not in data["meta"]]
    else:
        missing_meta = REQUIRED_META_FIELDS

    if missing_fields or missing_meta:
        return False, {
            "missing_protocol_fields": missing_fields,
            "missing_meta_fields": missing_meta
        }

    return True, {}
