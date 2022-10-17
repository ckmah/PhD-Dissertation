# Import necessary packages
from fpdf import FPDF
import datetime

# Input the parameters for the paper
title = "Diverse logics and grammar encode notochord enhancers"
authors = "Benjamin P Song*, Michelle F Ragsac*, Krissie Tellez, Granton A Jindal, Jessica L Grudzien, Sophia H Le, Emma K Farley"
disclaimer = "*These authors contributed equally to this work"

# Generate PDF to gather signatures 
pdf = FPDF(orientation='P', unit='in', format='Letter')

header_text = "Michelle Franc Ragsac has my permission to include the "
header_text += "following paper which was submitted for publication of which "
header_text += "I was a co-author, in her doctoral dissertation."

def format_paper(title, authors, disclaimer): 
    return(f'{authors}. "{title}". {disclaimer}')

for author in authors.split(","): 
    author_cleaned = (author.strip().replace('*',''))
    
    pdf.add_page()
    pdf.set_font(family='Times', style='', size=11) 
    pdf.multi_cell(0,.25, header_text, 0, 1) 
    pdf.multi_cell(0,.25, "", 0, 1) 
    pdf.multi_cell(0,.25, format_paper(title, authors, disclaimer), 0, 1) 
    pdf.multi_cell(0,.25, "", 0, 1) 
    pdf.multi_cell(0,.25, f"{author_cleaned}\t________________________________________\t\tDate _____________________", 0, 1)
    
pdf.output("Diverse-logics-notochord-enhancer_coauthor-permission-letter.pdf")
print(f"Done with request for permission documents for '{title}'!")
