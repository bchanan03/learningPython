class Document:
    def __init__(self,
                 doc_filename,
                 doc_description,
                 doc_type):
        self._doc_filename = doc_filename
        self._doc_description = doc_description
        self._doc_type = doc_type
        self._doc_is_save = False
        print(f"New document created with {doc_filename} name")

    def open(self):
        if self._doc_is_save:
            print(f"Open new document: {self._doc_filename}")
            self._doc_is_save = False

    def close(self, enforce=False):
        if self.is_saved() or enforce:
            print(f"Close {self._doc_filename} document")
            return

        print(f"Please save {self._doc_filename} document before closing")

    def save(self):
        self._doc_is_save = True
        print(f"Saving {self._doc_filename} document")

    def revert(self):
        self._doc_is_save = False
        print(f"Reverting changes on {self._doc_filename} document")

    def write(self):
        self._doc_is_save = False
        print(f"Writing something onto {self._doc_filename} document")

    def is_saved(self):
        return self._doc_is_save

    def __str__(self):
        return f"Doc filename: {self._doc_filename}, Description: {self._doc_description}, Type: {self._doc_type}"


class Application():
    def __init__(self):
        self._doc = None
        self._history = []

    def close_document(self):
        if self._doc:
            self._doc.save()
            self._doc.close()

        self._doc = None

    def new_document(self, doc_filename, doc_description, doc_type):
        if self._doc:
            self._doc.save()
            self._doc.close()

        self._doc = Document(
            doc_filename=doc_filename,
            doc_description=doc_description,
            doc_type=doc_type
        )
        self._history.append([doc_filename, doc_description, doc_type])

    def open_document(self, doc_filename):
        for doc in self._history:
            if doc[0] == doc_filename:
                self._doc = Document(
                    doc_filename=doc[0],
                    doc_description=doc[1],
                    doc_type=doc[2]
                )
                print(f"Found document {doc_filename} in history")
                return

        print(f"Could not find any document with {doc_filename} name")

    def get_history(self):
        for doc in self._history:
            print(f"Found: {doc[0]}")

    def __str__(self):
        if not self._doc:
            return ""
        return f"Current open document: {self._doc}"


if __name__ == "__main__":
    myApp = Application()

    myApp.close_document()
    myApp.new_document("apollo", "apollo description", "docx")
    myApp.close_document()
    myApp.new_document("apollo II", "apollo II description", "docx")
    myApp.close_document()
    myApp.new_document("apollo III", "apollo III description", "docx")
    myApp.open_document("apollo II")
    myApp.get_history()
    print(myApp)



