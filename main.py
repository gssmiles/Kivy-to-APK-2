from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def my_python_function(user_input):
    # For demo: reverse the input string
    return f"Processed: {user_input[::-1]}"

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Input Text Box (multiline, Indic-friendly)
        self.input_box = TextInput(
            hint_text="Enter text here...",
            multiline=True,
            font_name="Ramaraja.ttf",  # Example: use an Indic font installed on system
            size_hint=(0.2, 0.2)
        )
        layout.add_widget(self.input_box)

        # Button to process input
        btn = Button(text="Process", size_hint=(0.1, 0.1))
        #btn.bind(on_press=self.process_text)
        btn.bind(on_press=self.run_code)
        layout.add_widget(btn)

        # Output Text Box (multiline, Indic-friendly, read-only)
        self.output_box = TextInput(
            hint_text="Output will appear here...",
            multiline=True,
            readonly=True,
            font_name="Ramaraja.ttf",  # Use same font to show Indic text
            size_hint=(1, 0.5)
        )
        layout.add_widget(self.output_box)

        return layout

    def process_text(self, instance):
        # Example: reverse the input text (you can put your own logic here)
        input_text = self.input_box.text
        output_text = input_text[::-1]

        # Display in output box
        self.output_box.text = output_text
        
    def run_code(self, instance):
        user_input = self.input_box.text
        result = my_python_function(user_input)   # Call your function
        self.output_box.text = result             # Insert result into output textbox


if __name__ == "__main__":
    MyApp().run()
