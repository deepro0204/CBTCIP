from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(receipt_data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Receipt Title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - 50, "Payment Receipt")

    # Receipt Date
    c.setFont("Helvetica", 12)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawRightString(width - 50, height - 100, f"Date: {current_date}")

    # Add Receipt Data
    c.setFont("Helvetica", 12)
    y = height - 150
    for key, value in receipt_data.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width / 2.0, 30, "Thank you for your business!")

    c.save()

def main():
    # Sample receipt data
    receipt_data = {
        "Receipt No": "123456",
        "Customer Name": "John Doe",
        "Amount Paid": "$100.00",
        "Payment Method": "Credit Card",
        "Transaction ID": "7890ABCDEF",
    }

    # Filename of the receipt
    filename = "payment_receipt.pdf"

    # Create the receipt
    create_receipt(receipt_data, filename)
    print(f"Receipt has been created and saved as {filename}")

if __name__ == "__main__":
    main()
