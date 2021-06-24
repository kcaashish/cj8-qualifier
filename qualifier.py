from typing import Any, List, Optional


def make_table(
    rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False
) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    lens = []

    # converts the rows into tuples of column element
    # and gets the max length of each column
    for col in zip(*rows):
        lens.append(max([len(str(i)) for i in col]))
        # lens.append(max([len(str(i)) for i in col]))

    # calculates length of each column label
    # uses the maximun of the two for formatting
    if labels:
        label_lens = [len(str(i)) for i in labels]
        use_lens = [l if l > y else y for l, y in zip(lens, label_lens)]
    else:
        use_lens = lens

    # sets up formatted string with allocated space
    # based on the length required for each column
    if centered:
        fmt = " │ ".join(["{:^" + str(l) + "}" for l in use_lens])
    else:
        fmt = " │ ".join(["{:<" + str(l) + "}" for l in use_lens])

    # place labels in alloted space
    label = ""
    if labels:
        label = "│ " + fmt.format(*[str(i) for i in labels]) + " │" + "\n"

    # place row elements in alloted space
    rows_str = ""
    for row in rows:
        rows_str = (
            rows_str + "".join("│ " + fmt.format(*[str(i) for i in row]) + " │") + "\n"
        )

    # printing the table borders
    top = "┌"
    for i, le in enumerate(use_lens):
        top = top + "─" * (le + 2)
        if len(use_lens) > 1 and len(use_lens) - 1 != i:
            top = top + "┬"

    top = top + "┐" + "\n"

    mid = ""
    if labels:
        mid = "├"
        for i, le in enumerate(use_lens):
            mid = mid + "─" * (le + 2)
            if len(use_lens) > 1 and len(use_lens) - 1 != i:
                mid = mid + "┼"

        mid = mid + "┤" + "\n"

    bot = "└"
    for i, le in enumerate(use_lens):
        bot = bot + "─" * (le + 2)
        if len(use_lens) > 1 and len(use_lens) - 1 != i:
            bot = bot + "┴"

    bot = bot + "┘" + "\n"

    string_to_return = top + label + mid + rows_str + bot
    return string_to_return
