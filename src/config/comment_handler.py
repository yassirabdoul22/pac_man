from typing import List


class CommentsHandler:
    def __init__(self,brut_text:str = ""):
        self.brut_text = brut_text
        self.cleaned_text = []

    def handle_comments(self)->str:
        self._handle_one_line_comments()
        return self._get_cleaned_text()

    def _handle_one_line_comments(self)->None:
        for line in self.brut_text.split('\n'):
            if not line:
                continue
            if "#" in line or "//" in line:
                sep = ""
                if line.startswith("#") or line.startswith("//"):
                    continue
                if "#" in line and "//" not in line:
                    sep = "#"
                if "//" in line and "#" not in line:
                    sep = "//"
                if "//" in line and "#" in line:
                    sep = "#" if list(line).index("#") < list(line).index("//") else "//"
                if sep:
                    self.cleaned_text.append(line.split(sep)[0] if len(line.split(sep)) > 1 else "")
                    continue
            self.cleaned_text.append(line)

    def _get_cleaned_text(self)->str:
        return "\n".join(self.cleaned_text)
