import os
import subprocess

def convert_pptx_to_pdf(input_path, output_path):
    """
    Convert a .pptx file to PDF using LibreOffice.
    """
    try:
        # Use LibreOffice to convert the file
        command = ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", os.path.dirname(output_path), input_path]
        subprocess.run(command, check=True)
        print(f"Converted: {input_path} -> {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {input_path}: {e}")

def find_and_convert_pptx_to_pdf(folder_path):
    """
    Find all .pptx files in the folder and convert them to PDF.
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pptx"):
                pptx_path = os.path.join(root, file)
                pdf_path = os.path.splitext(pptx_path)[0] + ".pdf"
                
                print(f"Processing: {pptx_path}")
                convert_pptx_to_pdf(pptx_path, pdf_path)

if __name__ == "__main__":
    folder_path = input("Enter the folder path to search for .pptx files: ").strip()
    if os.path.isdir(folder_path):
        find_and_convert_pptx_to_pdf(folder_path)
    else:
        print("Invalid folder path. Please provide a valid directory.")