from mtp import mtp

mtp_ = mtp()

mtp_.read_document("F:\\Проект 4курса\\вкр-ки\\1.docx")

print(mtp_.raw_text)