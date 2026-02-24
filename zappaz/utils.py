def get_participants(groups, groupId: str):
    group = next((g for g in groups if g.get("id") == groupId), None)
    if group is None:
        return []
    return group.get("participants", [])