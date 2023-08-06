import requests

class MyClickUp:
    def __init__(self, token: str):
        self._token = token
        self._baseUrl = "https://api.clickup.com/api/v2/"
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": self._token
        }

    def getTeam(self) -> dict:
        """
        Returns a dict with the data of users registered in ClickUp. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}team"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getSpace(self, spaceId: str) -> dict:
        """
        Returns a dict with data from a Space. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}space/{spaceId}"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getSpaceFolders(self, spaceId: str) -> dict:
        """
        Returns a list with the Folders of a Space. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}space/{spaceId}/folder"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getFolder(self, folderId: str) -> dict:
        """
        Returns a dict with data from a Folder. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}folder/{folderId}"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getFolderByName(self, folderName: str, spaceId) -> list:
        """
        Returns a list with the Folders of a Space. See ClickUp API documentation for details of the structure of this data.
        """
        folderName = folderName.lower()
        folderList = []
        mySpace = self.getSpaceFolders(spaceId)
        for myFolder in mySpace['folders']:
            if myFolder['name'].lower() == folderName:
                folderList.append(myFolder)
            # endif --
        # endfor --
        return folderList

    def getFolderLists(self, folderId: str) -> dict:
        """
        Returns a list with the Lists of a Folder. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}folder/{folderId}/list"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getList(self, listId: str) -> dict:
        """
        Returns a dict with data from a List. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}list/{listId}"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getListsByName(self, listName: str, folderId) -> list:
        """
        Returns a dict with data from a List. See ClickUp API documentation for details of the structure of this data.
        """
        listName = listName.lower()
        listList = []
        myFolder = self.getFolderLists(folderId)
        for myList in myFolder['lists']:
            if myList['name'].lower() == listName:
                listList.append(myList)
            # endif --
        # endfor --
        return listList

    def getListTasks(self, listId: str) -> dict:
        """
        Returns a list with the Tasks of a List. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}list/{listId}/task"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getTask(self, taskId: str, flagSubtasks: bool = False) -> dict:
        """
        Returns a dict with data from a Task. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}task/{taskId}"
        params = {"subtasks": flagSubtasks}
        auth_response = requests.get(urlClickUp, headers=self._headers, params=params)
        return auth_response.json()

    def getTasksByName(self, taskName: str, listId) -> list:
        """
        Returns a dict with data from a Task. See ClickUp API documentation for details of the structure of this data.
        """
        taskName = taskName.lower()
        taskList = []
        myList = self.getListTasks(listId)
        for myTask in myList['tasks']:
            if myTask['name'].lower() == taskName:
                taskList.append(myTask)
            # endif --
        # endfor --
        return taskList

    def getListCustomFields(self, listId: str) -> dict:
        """
        Returns a list with the Custom Fields of a List. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}list/{listId}/field"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def getListCustomFieldByName(self, listId: str, fieldName: str) -> dict | None:
        """
        Returns a dict with the details of a Custom Fields of a List. See ClickUp API documentation for details of the structure of this data.
        """
        fieldName = fieldName.lower()
        customFields = self.getListCustomFields(listId)
        for field in customFields['fields']:
            if field['name'].lower() == fieldName:
                return field
            # endif --
        # endfor --
        return None

    def getCustomFieldOption(self, listId: str, fieldName: str, optionName: str) -> dict | None:
        """
        Returns a list with the options of a Custom Fields of a List. See ClickUp API documentation for details of the structure of this data.
        """
        field = self.getListCustomFieldByName(listId=listId, fieldName=fieldName)
        if not field or 'type_config' not in field or 'options' not in field['type_config']:
            return None
        # endif --
        optionName = optionName.lower()
        for option in field['type_config']['options']:
            if option['name'].lower() == optionName:
                return option
            # endif --
        # endfor --
        return None

    def getUser(self, userId: str) -> dict:
        """
        Returns a dict with a Users's data. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}team/team_id/user/{userId}"
        auth_response = requests.get(urlClickUp, headers=self._headers)
        return auth_response.json()

    def createFolder(self, folderJson: dict, spaceId: str) -> dict:
        """
        Creates a Folder in a given Space, the Folder details are specified in the dict "folderJson", according to the ClickUp API . See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}space/{spaceId}/folder"
        auth_response = requests.post(urlClickUp, headers=self._headers, json=folderJson)
        return auth_response.json()

    def createList(self, listJson: dict, folderId: str) -> dict:
        """
        Creates a List in a given Folder, the List details are specified in the dict "listJson", according to the ClickUp API. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}folder/{folderId}/list"
        auth_response = requests.post(urlClickUp, headers=self._headers, json=listJson)
        return auth_response.json()

    def createTask(self, taskJson: dict, listId: str, parentTaskId: str = None) -> dict:
        """
        Creates a Task in a given Folder, the Task details are specified in the dict "taskJson", according to the ClickUp API. See ClickUp API documentation for details of the structure of this data.
        """
        if parentTaskId is not None:
            taskJson["parent"] = parentTaskId
        urlClickUp = f"{self._baseUrl}list/{listId}/task"
        auth_response = requests.post(urlClickUp, headers=self._headers, json=taskJson)
        print(urlClickUp)
        return auth_response.json()

    def updateFolder(self, folderJson: dict, folderId: str) -> dict:
        """
        Updates the Folder properties, the Folder details are specified in the dict "folderJson", according to the ClickUp API. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}folder/{folderId}"
        auth_response = requests.put(urlClickUp, headers=self._headers, json=folderJson)
        return auth_response.json()

    def updateList(self, listJson: dict, listId: str) -> dict:
        """
        Updates the List properties, the List details are specified in the dict "listJson", according to the ClickUp API. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}list/{listId}"
        auth_response = requests.put(urlClickUp, headers=self._headers, json=listJson)
        return auth_response.json()

    def updateTask(self, taskJson: dict, taskId: str) -> dict:
        """
        Updates the Task properties, the Task details are specified in the dict "taskJson", according to the ClickUp API. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}task/{taskId}"
        auth_response = requests.put(urlClickUp, headers=self._headers, json=taskJson)
        return auth_response.json()

    def deleteFolder(self, folderId: str):
        """
        Delete a Folder. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}folder/{folderId}"
        requests.delete(urlClickUp, headers=self._headers)

    def deleteList(self, listId: str):
        """
        Delete a List. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}list/{listId}"
        requests.delete(urlClickUp, headers=self._headers)

    def deleteTask(self, taskId: str):
        """
        Delete a Task. See ClickUp API documentation for details of the structure of this data.
        """
        urlClickUp = f"{self._baseUrl}task/{taskId}"
        requests.delete(urlClickUp, headers=self._headers)
# endclass --
