#!/usr/bin/env python
# https://github.com/ElDeveloper/phd-thesis/blob/master/permission-letters/build.py

import pathlib
import os
import json
from jinja2 import Template
import numpy as np
import pandas as pd
from subprocess import call
from tempfile import TemporaryDirectory
import shutil


def process_paper(citation):
    date_index = citation.index("(")
    citation_authors = citation[:date_index]
    citation_authors = citation_authors.replace(".", "").strip()
    citation_rest = citation[date_index:]
    authors = citation_authors.split(", ")

    updated_authors = []
    for author in authors:
        parts = author.split(" ")
        first_initial = parts[0][0]
        if len(parts) == 3:
            middle_initial = parts[1][0]
            to_add = f"{parts[2]} {first_initial}{middle_initial}"
        elif len(parts) == 2:
            to_add = f"{parts[1]} {first_initial}"
        else:
            raise ValueError(f"Malformed name: {author}!")
        updated_authors.append(to_add)

    return f"{', '.join(updated_authors)} {citation_rest}"


def main():

    # Load the template
    with open("template.tex") as f:
        template = f.read()
    env = Template(template)

    # Load the paper title strings
    with open("./papers.json", "r") as f:
        papers = json.load(f)
    paper_strings = {k: process_paper(v) for k, v in papers.items()}

    # Load the author data
    author_df = pd.read_excel("authors.xlsx")

    # Create a folder "forms" if it doesn't exist
    if not os.path.exists("forms"):
        os.makedirs("forms")

    # Loop through the authors and generate the forms
    for _, row in author_df.iterrows():
        co_authored = []

        # Loop through the papers and check if the author is on them
        for paper, paper_string in paper_strings.items():
            if not pd.isnull(row[paper]):
                co_authored.append(paper_string)

        # If the author is not on any papers, raise an error
        if len(co_authored) == 0:
            raise ValueError('Could not find a paper for %s %s. There may be a'
                             ' typo or you might not have any publications '
                             ' with this author.'%
                             (row.first_name, row.last_name))

        # Generate the form as a PDF
        filename = row.email.replace('@', 'AT')

        # Skip if the file already exists
        if pathlib.Path(f"forms/{filename}.pdf").exists():
            continue

        # Make new PDF
        with TemporaryDirectory() as tmp:
            filename = f"{tmp}/{filename}"
            with open(filename + '.tex', 'w') as f:
                data = env.render(first_name=row.first_name,
                                  last_name=row.last_name, papers=co_authored)
                f.write(data)
            args = [
                "pdflatex",
                f"-output-directory={tmp}",
                filename
            ]
            call(args)
            tmp_path = pathlib.Path(tmp)
            pdf = next(tmp_path.glob("*.pdf"))

            # Move the PDF to the forms directory
            shutil.move(pdf, "forms")


if __name__ == '__main__':
    main()
