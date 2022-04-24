from _datetime import date
from fpdf import FPDF


class PDF(FPDF):

    def __init__(self, title, name):
        super().__init__()
        self.title = title
        self.name = name
        self.add_page()

    def header(self):
        self.set_draw_color(255, 255, 255)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)

        # name of the student
        self.set_font('Arial', '', 11)
        w = self.get_string_width(self.name) + 6
        self.cell(w, 9, self.name, 1, 0, 'C', 1)
        w = self.get_string_width(str(date.today())) + 275
        self.cell(w, 9, str(date.today()), 1, 1, 'C', 1)

        # title of the report
        self.set_font('Arial', 'B', 18)
        w = self.get_string_width(self.title) + 6
        self.set_x((210 - w) / 2)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        self.cell(w, 9, self.title, 1, 1, 'C', 1)

        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 14)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, '%s) %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def question_title(self, num, label):
        # Arial 12
        self.set_font('Arial', 'B', 12)
        # Background color
        self.set_fill_color(255, 255, 255)
        # Title
        self.cell(0, 6, '%s) %s' % (num, label), 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, name):
        # Read text file
        # with open(name, 'rb') as fh:
        #     txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, name)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        # self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        # self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)
        self.ln()
