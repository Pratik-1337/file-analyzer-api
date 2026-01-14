from app.services import analyze_file
import os

os.system('cls' if os.name == 'nt' else 'clear')

name = input("Enter Filename: ")
output = analyze_file(name)

report = open("report.txt", "w")

if output == "FILE_NOT_FOUND":
    print("\nEnter a Valid File Name.")
elif output == None:
    report.write("\nNo Numbers found in the given file.")
else:
    report.write("=========================\n")
    report.write("   FILE ANALYSIS REPORT\n")
    report.write("=========================\n\n")

    report.write(f"Count  : {output["count"]}\n")
    report.write(f"Average: {output["average"]:.2f}\n")
    report.write(f"Minimum: {output["min"]}\n")
    report.write(f"Maximum: {output["max"]}\n")
    report.write(f"Product: {output["product"]}")

    print("\nSaved the Analysis in report.txt")
report.close()

input("\nPress any key to exit.")