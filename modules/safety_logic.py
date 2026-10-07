# ---------------- OBJECT GROUPS ----------------
CASE1 = [
    "door", "wall", "person", "tv", "bed", "refrigerator", "table", "steps",
    "tree", "wood", "cylinder", "washing machine", "sofa", "microwave",
    "window", "board", "river", "leak", "knife", "water"
]

CASE2 = [
    "bike", "bicycle"
]

CASE3 = [
    "car", "bus", "truck", "auto", "train", "gate", "electrical post",
    "van", "jcb"
]

CASE4 = [
    "book", "cup", "clothes", "mat", "bag", "plate", "food", "pen",
    "pencil", "paper", "leaf", "box", "toy", "glasses"
]


# ---------------- MAIN FUNCTION ----------------
def generate_instruction(obj):
    name = obj["name"].lower()
    side = obj["side"]
    d = obj["distance_m"]

    # Ignore small objects
    if name in CASE4:
        return None

    # ---------------- CASE 1 ----------------
    # Person, wall, door, refrigerator, tree, etc.
    if name in CASE1:
        # 50 cm - 31 cm
        if 0.31 <= d <= 0.50:
            return f"{name.capitalize()} ahead on your {side}. Move carefully."
        # 30 cm - 10 cm
        if 0.10 <= d <= 0.30:
            return f"{name.capitalize()} is very close on your {side}. Stop and move safely."

    # ---------------- CASE 2 ----------------
    # Bike, bicycle
    if name in CASE2:
        # 1.5 m - 1.0 m
        if 1.0 <= d <= 1.5:
            return f"{name.capitalize()} ahead on your {side}. Move carefully."
        # 1.0 m - 0.60 m
        if 0.60 <= d < 1.0:
            return f"{name.capitalize()} is very close on your {side}. Keep a safe distance."

    # ---------------- CASE 3 ----------------
    # Car, bus, truck, van, train, etc.
    if name in CASE3:
        # 3.0 m - 2.5 m
        if 2.5 <= d <= 3.0:
            return f"{name.capitalize()} ahead on your {side}. Move carefully."
        # 2.4 m - 1.5 m
        if 1.5 <= d < 2.5:
            if side == "left":
                return f"{name.capitalize()} is approaching on your left. Move right safely."
            elif side == "right":
                return f"{name.capitalize()} is approaching on your right. Move left safely."
            else:
                return f"{name.capitalize()} is approaching in front. Move carefully and keep distance."

    return None
