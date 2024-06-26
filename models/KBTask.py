class KBTask:

    """
    Task for a Kanban table.
    """

    def __init__(self, id: str | None = None, text: str = "Text for task not found", headerColor: str = "#3B6EFF"):
        self.id = id
        self.text = text
        self.headerColor = headerColor


    def __eq__(self, other) -> bool:
        return self.id == other.id
    
    def compareTo(self, other):

        """
        Return True if self and other are completely the same.
        """

        result = True

        if (self.id != other.id) or (self.text != other.text) or (self.headerColor != other.headerColor):
            result = False

        return result
    

    def findByText(self, text: str) -> int:

        """
        Return lowest index of given text in the text of this task.\n
        Return -1 if not found.
        """

        return self.text.lower().find(text.lower())