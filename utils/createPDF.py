import os

import roman as roman

from Models.PdfModel import PDF
from utils.dataManager import getDatas


def createPDF():
    title = 'RadiationCAM Report'
    name = getDatas('user')['PERSONAL']['name1'] + "   " + getDatas('user')['PERSONAL']['name2'] + "   " + getDatas('user')['PERSONAL']['name3']
    print(name)

    pdf = PDF(title, name)
    pdf.set_title(title)
    pdf.set_author(name)

    i = 0

    permanent_report = getDatas('permanent')['REPORT']
    user_report = getDatas('user')['REPORT']

    for chapter in permanent_report:
        i = i + 1
        j = 0
        pdf.chapter_title(roman.toRoman(i), chapter)

        if not isinstance(permanent_report[chapter], str):
            for key_question, value_question in permanent_report[chapter].items():
                j = j + 1
                pdf.question_title(j, value_question)

                if user_report[chapter][key_question] == '':
                    pdf.chapter_body("No response")
                else:
                    pdf.chapter_body(user_report[chapter][key_question])
        else:
            if user_report[chapter] == '':
                pdf.chapter_body("No response")
            else:
                pdf.chapter_body(user_report[chapter])

    pdf.output(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\report.pdf')
    os.startfile(r'C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\report.pdf')
