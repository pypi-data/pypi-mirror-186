import re


class SQLMinifier:
    def minify(self, sql):
        """
        Minifies an SQL string into a single line.
        """
        # Break by newline to make it easier to remove single line comments.
        lines = re.split(r'\n', sql)
        # Remove single line comments and join all lines by a space to make it easier to remove multiline comments.
        match = ' '.join([re.sub(r'\s*--.*', '', s) for s in lines])
        # Remove multi-line comments.
        match = re.sub(r'/\*.*?\*/', "", match)
        # Replace more than 2 consecutive spaces into 1 space.
        match = re.sub(r'\s\s+', " ", match)
        # Remove the spaces between the following characters: , ; ( )
        match = re.sub(r'(\s*)(;|,|\)|\()(\s*)', r"\2", match)
        # Remove trailing whitespaces.
        return match.strip()
