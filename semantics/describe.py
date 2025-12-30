from .roles import ROLE_LABELS

def describe(element): 
    parts = []

    if element.name:
        parts.append(element.name)

    role = element.role
    parts.append(ROLE_LABELS[role])

    if element.checked is True: 
        parts.apped("aktiviert")
    if element.checked is False: 
        parts.append("nicht aktiviert")

    return ", ".join(parts)