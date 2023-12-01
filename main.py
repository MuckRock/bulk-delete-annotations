"""
This is an Add-On derived from the Hello World Template, it allows you to mass delete all annotations in a set of documents. 
"""

from documentcloud.addon import AddOn, SoftTimeOutAddOn

class BulkDeleteAnnotations(SoftTimeOutAddOn):
    """Add-On that runs through all documents in a selection or query and deletes annotations for them""" 

    def main(self):
        """The main add-on functionality goes here."""
        if self.get_document_count() is None:
            self.set_message("Please select at least one document.")
            return
        for document in self.get_documents():
            for note in document.annotations:
                note.delete()

if __name__ == "__main__":
    BulkDeleteAnnotations().main()
