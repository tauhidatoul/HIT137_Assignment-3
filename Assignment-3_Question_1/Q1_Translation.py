import tkinter as tk
from translate import Translator  # Assuming a translation library is installed (e.g., `translate`)

class LanguageTranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Language Translator")
        self.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for user input
        self.input_entry = tk.Entry(self, width=30)
        self.input_entry.pack(pady=10)

        # Button to trigger translation
        self.translate_button = tk.Button(self, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        # Label to display translated text
        self.translation_label = tk.Label(self, text="")
        self.translation_label.pack(pady=10)

    # Method overriding - Explanation (# This method overrides the default destroy method)
    def destroy(self):
        print("Application is closing.")
        super().destroy()

    # Encapsulation - Explanation (# This method encapsulates the translation logic)
    def translate_text(self):
        user_input = self.input_entry.get()
        translated_text = self._perform_translation(user_input)
        self.translation_label.config(text=translated_text)

    # Multiple inheritance - Explanation (# This method combines two decorators)
    @staticmethod
    def _validate_input(func):
        def wrapper(self, *args, **kwargs):
            user_input = self.input_entry.get()
            if not user_input:
                self.translation_label.config(text="Please enter text to translate.")
            else:
                func(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def _perform_translation(user_input):
        # Simulate translation using a translation library
        translator = Translator(to_lang="fr")  # Translating to French for demonstration
        translation = translator.translate(user_input)
        return translation


if __name__ == "__main__":
    app = LanguageTranslatorApp()
    app.mainloop()
