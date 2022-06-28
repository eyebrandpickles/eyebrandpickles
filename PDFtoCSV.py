import tabula
filename = input("/Users/rajeshkumaranandan/Documents/Study/Rajeshkumar_Anandan_Resume.PDF")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')
df.to_csv('out.csv')