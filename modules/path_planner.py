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


# ---------------- RANGE CHECK ----------------
def in_warning_range(name, d):
    # Case-1
    if name in CASE1:
        return (0.31 <= d <= 0.50) or (0.10 <= d <= 0.30)

    # Case-2
    if name in CASE2:
        return (1.0 <= d <= 1.50) or (0.60 <= d <= 1.0)

    # Case-3
    if name in CASE3:
        return (2.5 <= d <= 3.0) or (1.5 <= d <= 2.4)

    return False


# ---------------- PATH PLANNER ----------------
def plan_path(objects, frame_width):
    left = []
    center = []
    right = []

    for obj in objects:
        name = obj["name"].lower()
        d = obj["distance_m"]
        side = obj["side"]

        # Ignore Case-4 objects
        if name in CASE4:
            continue

        # Ignore objects outside warning range
        if not in_warning_range(name, d):
            continue

        # Add object to its zone
        if side == "left":
            left.append(name)
        elif side == "right":
            right.append(name)
        else:
            center.append(name)

    # ---------------- NO RELEVANT OBJECTS ----------------
    if not left and not center and not right:
        return {"recommendation": None}

    # ---------------- CENTER CLEAR ----------------
    if not center:
        if left and right:
            return {
                "recommendation": (
                    f"Center path is clear. "
                    f"{left[0]} on the left. "
                    f"{right[0]} on the right."
                )
            }
        if left:
            return {
                "recommendation": (
                    f"{left[0].capitalize()} on the left. "
                    f"Center and right paths are clear."
                )
            }
        if right:
            return {
                "recommendation": (
                    f"{right[0].capitalize()} on the right. "
                    f"Center and left paths are clear."
                )
            }

    # ---------------- CENTER BLOCKED ONLY ----------------
    if center and not left and not right:
        return {
            "recommendation": (
                f"{center[0].capitalize()} in the center. "
                f"Move left or right."
            )
        }

    # ---------------- LEFT CLEAR ----------------
    if not left:
        return {
            "recommendation": (
                "Left path is clear. "
                "Obstacles ahead or on the right."
            )
        }

    # ---------------- RIGHT CLEAR ----------------
    if not right:
        return {
            "recommendation": (
                "Right path is clear. "
                "Obstacles ahead or on the left."
            )
        }

    # ---------------- ONLY LEFT BLOCKED ----------------
    if left and not center and not right:
        return {
            "recommendation": (
                f"{left[0].capitalize()} on the left. "
                "Move through the center or right."
            )
        }

    # ---------------- ONLY RIGHT BLOCKED ----------------
    if right and not center and not left:
        return {
            "recommendation": (
                f"{right[0].capitalize()} on the right. "
                "Move through the center or left."
            )
        }

    # ---------------- ALL SIDES BLOCKED ----------------
    return {
        "recommendation": (
            "Move carefully. Obstacles detected around you."
        )
    }


