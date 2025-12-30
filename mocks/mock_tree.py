from core.element import AccessibleElement

def ok_button(): 
    return AccessibleElement(
        name="OK", 
        role="button",
        enabled=True
    )