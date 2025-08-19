"""
Replace DGHM with DEM within a zip folder.
"""
import os
import zipfile
import argparse


def patch_xml(input_xml, output_xml):
    """Replace DGHM occurrences in the .XML files with DEM and convert encoding to UTF-8."""
    with open(input_xml, 'r', encoding='shift_jis') as xml_file:
        data = xml_file.read()

        #replace DGHM for DEM
        data = data.replace('DGHM', 'DEM')

        # reencode to utf-8
        data = data.replace('encoding="Shift_JIS"', 'encoding="UTF-8"')

    with open(output_xml, 'w', encoding='utf-8') as f:
        f.write(data)
    


def patch_zip(input_zip, output_zip):
    """Process XML files within a zipped folder: Replace DGHM occurrences with DEM in each .XML."""
    
    patched_files = []
    with zipfile.ZipFile(input_zip, 'r') as zin:
        for file_name in zin.namelist():
            file = zin.read(file_name)
            data = file.decode("shift_jis")

            #replace DGHM for DEM
            data = data.replace('DGHM', 'DEM')

            # reencode to utf-8
            data = data.replace('encoding="Shift_JIS"', 'encoding="UTF-8"')
            patched_file = data.encode("utf-8")
            patched_files.append((file_name, patched_file))

    with zipfile.ZipFile(output_zip, 'w') as zout:
        for file_name, modified_file in patched_files:
            zout.writestr(file_name, modified_file)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Patch DGHM to DEM in XML or ZIP files.")
    parser.add_argument("input", help="Input XML file or ZIP folder")
    parser.add_argument("output", help="Output XML file or ZIP folder")
    parser.add_argument(
        "--zip",
        action="store_true",
        help="Set this flag if input/output are ZIP archives"
    )
    args = parser.parse_args()

    if args.zip:
        patch_zip(args.input, args.output)
    else:
        patch_xml(args.input, args.output)