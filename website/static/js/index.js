function deleteNote(noteId){ /* This function sends a request to the backend */
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }), /* delete the note */
    }).then((_res) => {
        window.location.href = "/"; /* refresh the page */
    });
}
