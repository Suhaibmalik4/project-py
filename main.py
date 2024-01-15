import tkinter as tk
from tkinter import messagebox

class Note:
    def __init__(self, title="", content=""):
        self.title = title
        self.content = content

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note")

        # List to store notes
        self.notes = []

        # Set up the user interface
        self.setup_gui()

    def setup_gui(self):
        # Widgets
        self.title_entry = tk.Entry(self.root, width=40)
        self.content_text = tk.Text(self.root, wrap=tk.WORD, width=40, height=10)
        self.notes_listbox = tk.Listbox(self.root, width=40, height=10, selectmode=tk.SINGLE)

        # Buttons
        add_button = tk.Button(self.root, text="add", command=self.add_note)
        delete_button = tk.Button(self.root, text="delete", command=self.delete_note)

        # Grid layout
        self.title_entry.grid(row=0, column=0, padx=10, pady=5, columnspan=2)
        self.content_text.grid(row=1, column=0, padx=10, pady=5, columnspan=2)
        self.notes_listbox.grid(row=2, column=0, padx=10, pady=5, columnspan=2)
        add_button.grid(row=3, column=0, padx=10, pady=5)
        delete_button.grid(row=3, column=1, padx=10, pady=5)




    # Bind the event to the appropriate function
        self.notes_listbox.bind("<ButtonRelease-1>", self.load_selected_note)

    def save_notes(self):
        with open("notes.txt", 'w', encoding='utf-8') as file:
            for note in self.notes:
                file.write(f"{note.title}:{note.content}\n")

    def load_notes(self):
        try:
            with open("notes.txt", 'r', encoding='utf-8') as file:
                self.notes = [Note(*line.strip().split(":")) for line in file.readlines()]
                self.update_notes_listbox()
        except FileNotFoundError:
            self.notes = []

    def add_note(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END)

        if title and content.strip():
            self.notes.append(Note(title, content))
            self.update_notes_listbox()
            self.clear_note_entry()
            self.save_notes()
        else:
            messagebox.showwarning("warning", "pleas enter somthing")

    def delete_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            self.notes.pop(selected_index[0])
            self.update_notes_listbox()
            self.clear_note_entry()
            self.save_notes()

    def update_notes_listbox(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            self.notes_listbox.insert(tk.END, note.title)

    def load_selected_note(self, event):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            selected_note = self.notes[selected_index[0]]
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, selected_note.title)
            self.content_text.delete("1.0", tk.END)
            self.content_text.insert(tk.END, selected_note.content)

    def clear_note_entry(self):
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = NoteApp(root)
    app.load_notes()  # Load notes when the application starts
    root.mainloop()

if __name__ == "__main__":
    main()
