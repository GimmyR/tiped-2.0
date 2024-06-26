import pickle
from models.KBTask import KBTask
from models.KBTableException import KBTableException

class KBTable :

    """
    This class defines a Kanban Table.
    """

    prefix = "T"
    columns = ["To do", "In progress", "Done"]

    def __init__(self, filename: str | None = None) :

        self.__seq__ = 1
        self.filename = filename
        self.content = {}
        for column in KBTable.columns :
            self.content[column] = []


    def saveToFile(self) :

        """
        This method saves the Kanban Table in the specified file.
        """

        with open(self.filename, "wb") as file :
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)


    def openFile(self) :

        """
        This method open the specified file and load the content into this Kanban Table.
        """

        with open(self.filename, "rb") as file :
            table = pickle.load(file)
            self.__seq__ = table.__seq__
            self.content = table.content


    def findTask(self, task: KBTask) -> tuple | None :

        """
        This method returns the position (key, index) of a task in the Kanban Table or None if not found.
        """

        result = None

        for column in KBTable.columns :
            if task in self.content[column] :
                result = (column, self.content[column].index(task))
                break

        return result
    

    def findTaskByText(self, text: str) -> tuple | None :

        """
        This method returns the position (key, index) of the given text of task in the Kanban Table or None if not found.
        """

        result = None

        for column in KBTable.columns :
            size = len(self.content[column])
            for i in range(size):
                index = self.content[column][i].findByText(text)
                if index >= 0:
                    result = (column, i)
                    break

        return result
    

    def removeTask(self, task: KBTask) :

        """
        This method removes the specified task in this Kanban Table.
        """

        position = self.findTask(task)

        if position == None :
            raise KBTableException("The specified task is not found.")
        
        else :
            column, index = position
            del self.content[column][index]
    

    def insertTask(self, task: KBTask, column: str, index: int) :

        """
        This method inserts the specified task in the specified position (column and index).

        If index is negative, it appends task in the specified column.
        """

        if index >= 0 :
            self.content[column].insert(index, task)
        else:
            self.content[column].append(task)


    def editTask(self, task: KBTask):

        """
        Find task with ID and update it.
        """

        position = self.findTask(task)

        if position != None :
            self.content[position[0]][position[1]] = task
        else:
            raise KBTableException("Task not found.")


    def next(self):

        """
        Return current sequence then increment current sequence.
        """

        result = KBTable.prefix + str(self.__seq__)
        self.__seq__ += 1

        return result
    

    def display(self):

        """
        Display kanban table in terminal.
        """

        for key in self.content.keys():
            print(f"{key} :")
            for task in self.content[key]:
                print(f"- {task.id}, {task.text}, {task.headerColor}")


    def hasChanged(self):

        """
        Return True if current KBTable is different from that contained in the file.
        """

        if self.filename == None:
            raise KBTableException("Filename not found.")
        else:
            tmp = KBTable(self.filename)
            tmp.openFile()
            return not (self == tmp)


    def __eq__(self, other) -> bool:
        
        """
        Return True if the two tables have the same tasks in the same columns.
        """

        result = True
        
        for column in KBTable.columns:
            size1 = len(self.content[column])
            size2 = len(other.content[column])

            if size1 != size2:
                result = False
                break
            else:
                for i in range(size1):
                    if not self.content[column][i].compareTo(other.content[column][i]):
                        result = False
                        break

        return result
    

    def size(self, column: str | None = None) -> int:

        """
        Return the number of tasks in the given column.
        If column is not given, return the number of tasks in the whole table.
        """

        if column != None:
            return len(self.content[column])
        
        else:
            result = 0
            for col in KBTable.columns:
                result += len(self.content[col])
            return result
        

    def percentageOfIncrease(self) -> float:

        """
        Return the percentage of Done Task compared to All Tasks.
        """

        totalSize = self.size()

        if totalSize == 0:
            return 0
        else:
            return "%.2f" % ((float(self.size(KBTable.columns[2])) / float(totalSize)) * 100)