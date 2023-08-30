# thesis permission forms

This project is a script to generate permission forms for my thesis. It is based on https://github.com/ElDeveloper/phd-thesis/.

## Usage

1. Recreate the conda environment to run the script:

    ```
    conda env create -f environment.yml
    conda activate thesis-forms
    ```

2. Update `authors.xlsx` with the authors' names, emails and projects they were a part of.
3. Update `papers.json` with the paper titles.
4. Update `template.tex` with your name.
5. Run `python build.py` to generate the permission forms. Check the `forms` folder for the generated PDFs and make sure there are no errors.