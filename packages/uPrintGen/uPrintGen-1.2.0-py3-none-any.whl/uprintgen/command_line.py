"""
        Command line functions
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from .svg_microprint_generator import SVGMicroprintGenerator


def main():
    """
     Command line main function
    """
    parser = argparse.ArgumentParser(prog='μPrintGen',
                                     description='Microprint generator')

    parser.add_argument('-i', '--file_input',
                        required=True,
                        dest='file_input',
                        help="File path for the input text to generate the microprint.")
    parser.add_argument('-c', '--config_file_path',
                        dest='config_file_path',
                        help="Config file path for the .json file containing the configurations "
                             "of the generated microprint.",
                        default="config.json"
                        )
    parser.add_argument('-o', '--output_filename', dest='output_filename',
                        help='Output filename for the generated microprint',
                        default="Microprint.svg"
                        )

    args = parser.parse_args()

    SVGMicroprintGenerator.from_text_file(output_filename=args.output_filename,
                                          config_file_path=args.config_file_path,
                                          file_path=args.file_input).render_microprint()
