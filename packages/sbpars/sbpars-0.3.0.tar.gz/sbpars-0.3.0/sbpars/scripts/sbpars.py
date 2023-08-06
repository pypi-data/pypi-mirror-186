#!/usr/bin/env python3
from sbpars.app import parser, export_to_csv, export_to_excel


def main():
    print("Hi! I parse sberbank transactions file.\nTrying to parse...")
    data = parser()
    print("Successfully parsed index.html file")
    export_to_csv(data)
    print("Successfully exported to .csv table")
    export_to_excel(data)
    print("Successfully exported to .xslx table\nWell done!")


if __name__ == '__main__':
    main()
