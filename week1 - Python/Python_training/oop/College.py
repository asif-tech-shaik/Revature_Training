class College:
    def __init__(self, ccode, cname, **kwargs):
        self._ccode = ccode
        self._cname = cname

    def display_college(self):
        return f"College Code: {self._ccode}, College Name: {self._cname}"
