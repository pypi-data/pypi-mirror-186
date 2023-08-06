import os
import platform

def convert(docx_file: str, output_pdf: str, debug: bool=False)->None:
    if platform.system().lower() == 'windows':
        import win32com.client

        word = win32com.client.Dispatch("Word.application")

        try:
            if "/" in docx_file or "\\" in docx_file:
                wordDoc = word.Documents.Open(docx_file, False, False, False)
            else:
                wordDoc = word.Documents.Open(os.getcwd()+'\\'+docx_file, False, False, False)
            if "/" in output_pdf or "\\" in output_pdf:
                wordDoc.SaveAs2(output_pdf, FileFormat = 17)
            else:
                wordDoc.SaveAs2(os.getcwd()+'\\'+output_pdf, FileFormat = 17)
            wordDoc.Close()
        except Exception as err:
            if debug:
                print(str(err))
            print('Falha ao converter: {}'.format(output_pdf))

        word.Quit()

    elif platform.system().lower() == 'linux':
        try:
            os.system(f'soffice --headless --convert-to pdf {docx_file}')
            os.rename(docx_file.split('/')[-1].replace(docx_file.split('.')[-1], 'pdf'), output_pdf)
        except Exception as err:
            if debug:
                print(str(err))
            print('Falha ao converter: {}'.format(output_pdf))

    else:
        print('Sistema desconhecido.')