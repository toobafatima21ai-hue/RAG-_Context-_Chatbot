from reportlab.pdfgen import canvas


def export_txt(messages):

    with open(
        "exports/chat_history.txt",
        "w",
        encoding="utf-8"
    ) as f:

        for msg in messages:

            f.write(
                f"{msg['role']}: {msg['content']}\n\n"
            )

    return "exports/chat_history.txt"


def export_pdf(messages):

    pdf_path = "exports/chat_history.pdf"

    c = canvas.Canvas(pdf_path)

    y = 800

    for msg in messages:

        c.drawString(
            50,
            y,
            f"{msg['role']}: {msg['content'][:100]}"
        )

        y -= 25

        if y < 50:

            c.showPage()

            y = 800

    c.save()

    return pdf_path