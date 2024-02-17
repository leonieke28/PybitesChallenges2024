import textwrap

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
    newlines (\n\n) in text determines the amount of columns.
    Return a string with the column output like:
    line1\nline2\nline3\n ... etc ...
    See also the tests for more info."""
    paragraphs = text.split("\n\n")
    lines = [textwrap.wrap(paragraph, COL_WIDTH) for paragraph in paragraphs]

    max_lines = max(len(paragraph) for paragraph in lines)
    columns = []
    for i in range(max_lines):
        row = []
        for paragraph in lines:
            try:
                row.append(paragraph[i])
            except IndexError:
                row.append("")
        columns.append("\t".join(row))

    return "\n".join(columns)
