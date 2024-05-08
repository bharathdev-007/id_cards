from fpdf import FPDF
import csv
import os

class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

def create_id_card(pdf, template_path, name, title, photo_path):
    pdf.add_page()
    pdf.image(template_path, 0, 0, 86, 54)
    pdf.set_font("Arial", size=10)
    pdf.set_xy(6, 25)
    pdf.cell(0, 0, name, ln=True)
    pdf.set_xy(6, 30)
    pdf.cell(0, 0, title, ln=True)
    pdf.image(photo_path, 60, 10, 20, 25)

def generate_id_cards(template_path, csv_file, photo_dir, output_pdf):
    pdf = PDF()
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            title = row['position']
            name = row['ï»¿name']
            
            photo_name = row['photo']
            photo_path = os.path.join(photo_dir, photo_name)
            create_id_card(pdf, template_path, name, title, photo_path)
    
    pdf.output(output_pdf)

if __name__ == "__main__":
    template_path = "ute_id_template.png"
    csv_file = "Data.csv"
    photo_dir = "photos"
    output_pdf = "employee_ids.pdf"
    
    generate_id_cards(template_path, csv_file, photo_dir, output_pdf)
