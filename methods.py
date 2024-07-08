from googletrans import Translator, LANGUAGES

class MyTranslator:
    def __init__(self):
        self.langs = list(LANGUAGES.values())

    def run(self, txt='Type text here', src='english', dest='hindi'):
        self.translator = Translator()
        self.txt = txt
        self.src = src
        self.dest = dest

        try:
            self.translated = self.translator.translate(self.txt, src=self.src, dest=self.dest)
        except Exception as e:
            print(f"Error: {e}")
            self.translated = self.translator.translate(self.txt)

        self.ttext = self.translated.text
        return self.ttext
