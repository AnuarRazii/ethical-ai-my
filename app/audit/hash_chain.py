import hashlib
import json


GENESIS_HASH = "0" * 64


def compute_chain_hash(event_payload: dict, previous_hash: str) -> str:
    encoded_payload = json.dumps(event_payload, sort_keys=True, separators=(",", ":"))
    material = f"{previous_hash}:{encoded_payload}".encode("utf-8")
    return hashlib.sha256(material).hexdigest()
