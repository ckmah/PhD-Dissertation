# Import necessary packages
from fpdf import FPDF
import datetime

# Input the parameters for the paper
title = "Diverse logics and grammar encode notochord enhancers"
authors = "Benjamin P Song*, Michelle F Ragsac*, Krissie Tellez, Granton A Jindal, Jessica L Grudzien, Sophia H Le, Emma K Farley"
disclaimer = "*These authors contributed equally to this work"

requestor_name = "Michelle Franc Ragsac"

class PDF(FPDF):
    def header(self):
        self.image('uc-letterhead.png', w=7.75, h=1.2, type='PNG')
        self.set_font(family='Times', style='', size=11)

def format_paper(title, authors, disclaimer): 
    return(f'{authors}. "{title}". {disclaimer}')
		
pdf = PDF(orientation='P', unit='in', format='Letter')

pdf.add_page()
pdf.set_font(family='Times', style='', size=11) 

# Input the parameters for the "from" address
address = "Department of Medicine\n"
address += "University of California, San Diego\n"
address += "9500 Gilman Drive\n"
address += "La Jolla, California 92093\n"
address += "Phone: 858-246-2552\n"
address += "Email: efarley@ucsd.edu\n"

# Input the parameters for the "to" address
addressee = "James Antony, Dean\n"
addressee += "Division of Graduate Education and Postdoctoral Affairs\n"
addressee += "University of California, San Diego"

todays_date = datetime.datetime.now().strftime("%B %d, %Y")

# Compose the letter

pdf.multi_cell(0,.25, address, 0, 1) 
pdf.multi_cell(0,.25, "", 0, 1)
pdf.multi_cell(0,.25, todays_date, 0, 1) 
pdf.multi_cell(0,.25, "", 0, 1)
pdf.multi_cell(0,.25, addressee, 0, 1) 
pdf.multi_cell(0,.25, "", 0, 1)

pdf.multi_cell(0,.25, "Dear Dean Antony:", 0, 1)
pdf.multi_cell(0,.25, "", 0, 1)
pdf.multi_cell(0,.25, f"We request permission for {requestor_name} to use material that has been submitted for publication. Ms. Ragsac was one of the authors on this paper.", 0, 1)
pdf.multi_cell(0,.25, "", 0, 1)
pdf.multi_cell(0,.25, format_paper(title, authors, disclaimer), 0, 1) 
pdf.ln(1)
pdf.multi_cell(0,.25, "Chair of Committee\t________________________________________\t\tDate ___________", 0, 1)
pdf.multi_cell(0,.25, "", 0, 1)
pdf.multi_cell(0,.25, "Michelle Franc Ragsac\t________________________________________\t\tDate ___________", 0, 1)

pdf.output('Diverse-logics-notochord-enhancer_gepa-permission-letter.pdf', 'F')
print(f"Done with request for permission documents for '{title}'!")
			   