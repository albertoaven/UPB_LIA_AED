def build_index_by_id(events):
    index = {}

    for event in events:
        index[event.id] = event

    return index