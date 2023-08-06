import json

def _build_slot_sequence_dict(slotSequenceJSON):
    """
    Utility method to construct a dictionary of the slot sequence.
    """
    slot_sequence = {}

    for definition in slotSequenceJSON:
        param = definition['slotParameter']
        key = param['key']
        value = param['value']
        slot_sequence[key] = value

    return slot_sequence