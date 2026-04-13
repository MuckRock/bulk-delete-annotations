"""
This is an Add-On derived from the Hello World Template,
it allows you to mass delete all annotations in a set of documents.
"""

import time
from documentcloud.addon import SoftTimeOutAddOn


class BulkDeleteAnnotations(SoftTimeOutAddOn):
    """Add-On deletes all notes on documents selected"""

    def main(self):
        """The main add-on functionality goes here."""
        self.client.session.headers.update({'User-Agent': 'Bulk Delete Annotations Add-On'})
        if self.get_document_count() is None:
            self.set_message("Please select at least one document.")
            return
        for document in self.get_documents():
            for note in document.annotations:
                note.delete()
            time.sleep(5)


if __name__ == "__main__":
    BulkDeleteAnnotations().main()
