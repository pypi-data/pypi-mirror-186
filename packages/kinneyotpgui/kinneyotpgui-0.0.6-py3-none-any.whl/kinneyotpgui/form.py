"""Form for one time pad"""

import random

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialog, QLabel, QFormLayout
from PySide6.QtWidgets import QLineEdit, QGridLayout, QTabWidget, QWidget, QPlainTextEdit

from kinneyotp import OTP

class Form(QDialog):
    """Main form"""

    def __init__(self, parent=None):
        """constructor"""
        super(Form, self).__init__(parent)
        self.parent = None
        self.main = self

        self.otp = OTP()

        width = 500
        height = 200

        length = 400

        self.setMinimumSize(width, height)
        self.setWindowTitle("One Time Pad")

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)

        # encode page
        encode_page = QWidget(self)
        layout = QFormLayout()
        encode_page.setLayout(layout)
        self.encode_text = QLineEdit()
        self.encode_text.setFixedWidth(length)
        self.encode_key = QLineEdit()
        self.encode_key.setFixedWidth(length)
        self.encoded = QLabel()
        self.encoded.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.encode_message = QLabel()
        layout.addRow('Text:', self.encode_text)
        layout.addRow('Key:', self.encode_key)
        layout.addRow('Encoded:', self.encoded)
        layout.addRow('', self.encode_message)
        self.encode_text.textChanged.connect(self.do_encode)
        self.encode_key.textChanged.connect(self.do_encode)

        # decode page
        decode_page = QWidget(self)
        layout = QFormLayout()
        decode_page.setLayout(layout)
        self.decode_text = QLineEdit()
        self.decode_text.setFixedWidth(length)
        self.decode_key = QLineEdit()
        self.decode_key.setFixedWidth(length)
        self.decoded = QLabel()
        self.decoded.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.decode_message = QLabel()
        layout.addRow('Text to decode:', self.decode_text)
        layout.addRow('Key:', self.decode_key)
        layout.addRow('Decoded:', self.decoded)
        layout.addRow('', self.decode_message)
        self.decode_text.textChanged.connect(self.do_decode)
        self.decode_key.textChanged.connect(self.do_decode)

        # generate page
        generate_page = QWidget(self)
        layout = QFormLayout()
        generate_page.setLayout(layout)
        self.seed = QLineEdit()
        self.random_text = QPlainTextEdit()
        # monospace font
        mono_font = self.font()
        if hasattr(QFont, "Monospace"):
            mono_font.setStyleHint(QFont.Monospace)
        else:
            mono_font.setStyleHint(QFont.Courier)
        mono_font.setFamily("Monaco")
        mono_font.setPointSize(12)
        self.random_text.setFont(mono_font)
        # TODO: add qt validator for valid seed input
        # TODO: re-size the random_text box
        self.seed.setFixedWidth(length)
        layout.addRow('Seed:', self.seed)
        layout.addRow('Random:', self.random_text)
        self.seed.textChanged.connect(self.do_generate)

        # settings page
        settings_page = QWidget(self)
        layout = QFormLayout()
        settings_page.setLayout(layout)
        self.alphabet = QLabel()
        self.alphabet.setText(self.otp.alphabet)
        self.alphabet.setFixedWidth(length)
        layout.addRow('Alphabet:', self.alphabet)

        # about page
        about_page = QWidget(self)
        layout = QFormLayout()
        about_page.setLayout(layout)
        self.about = QLabel()
        self.about.setWordWrap(True)
        about_text = "This code is similar to a 'one time pad' (aka Vernam Cipher) which can be used to encode/decode messages.\n"
        about_text += "\n"
        about_text += "Tips:\n"
        about_text += " - The key must be at least the same length as the uncoded text.\n"
        about_text += " - The key must be truly random.\n"
        about_text += " - The key must never be reused, in whole or in part.\n"
        about_text += " - The key must be kept completely secret by the communicating parties.\n"
        about_text += " - Consider adding (or using) a character (or phrase) that indicates that the message was sent under duress.\n"

        self.about.setText(about_text)
        layout.addRow('', self.about)

        # add pane to the tab widget
        tab.addTab(encode_page, 'Encode')
        tab.addTab(decode_page, 'Decode')
        tab.addTab(generate_page, 'Generate')
        tab.addTab(settings_page, 'Settings')
        tab.addTab(about_page, 'About')

        main_layout.addWidget(tab, 0, 0, 2, 1)

    def do_encode(self):
        """Try to encode using text using the key."""
        text = self.encode_text.text()
        key = self.encode_key.text()

        # ensure the values are all uppercase
        tmp_text = text.upper()
        if text != tmp_text:
            self.encode_text.setText(tmp_text)
            text = tmp_text
        tmp_key = key.upper()
        if key != tmp_key:
            self.encode_key.setText(tmp_key)
            key = tmp_key

        encoded = ""
        msg = ""
        if len(text) <= len(key):
            self.otp.key = key
            msg, encoded = self.otp.encode(text)
        else:
            msg = "The length of the text must be shorter or the same length as the key."
        self.encoded.setText(encoded)
        self.encode_message.setText(msg)

    def do_generate(self):
        """Generate 'random' text using a seed. Note: This is not truly random."""
        seed_text = self.seed.text()
        random_text = ''
        if seed_text != '':
            random.seed(seed_text)
            for i in range(1000):
                x = random.randrange(len(self.alphabet.text()))
                random_text += self.alphabet.text()[x]
                if i > 1:
                    if (i+1) % 5 == 0:
                        random_text += " "
                    if (i+1) % 25 == 0:
                        random_text += "\n"
            self.random_text.setPlainText(random_text)

    def do_decode(self):
        """Try to decode using the text and the key."""
        text = self.decode_text.text()
        key = self.decode_key.text()

        # ensure the values are all uppercase
        tmp_text = text.upper()
        if text != tmp_text:
            self.decode_text.setText(tmp_text)
            text = tmp_text
        tmp_key = key.upper()
        if key != tmp_key:
            self.decode_key.setText(tmp_key)
            key = tmp_key

        decoded = ""
        msg = ""
        if len(text) <= len(key):
            self.otp.key = key
            msg, decoded = self.otp.decode(text)
        else:
            msg = "The length of the text must be shorter or the same length as the key."
        self.decoded.setText(decoded)
        self.decode_message.setText(msg)

    # pylint: disable=unused-argument
    def closeEvent(self, event):
        """Override the close event so the user can just click the close window in corner."""
        self.accept()
