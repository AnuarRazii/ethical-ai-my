from app.audit.hash_chain import compute_chain_hash


def test_chain_hash_changes_with_previous_hash() -> None:
    payload = {"action": "test"}
    a = compute_chain_hash(payload, "0" * 64)
    b = compute_chain_hash(payload, "1" * 64)
    assert a != b
