# NOTE: This program assumes the EC2 standard for concrete strength calculation.

import datetime
import csv
import os

def calculate_strength(load_kn, area_mm2=22500):
    """Calculate the concrete strength in MPa."""
    
    # Convert load from kN to N
    load_n = load_kn * 1000

    # Calculate strength in MPa
    strength_mpa = round(load_n / area_mm2, 2)

    return strength_mpa

def evaluate_test(actual, target):
    """Evaluate the test result based on actual and target strengths."""

    return "PASS" if actual >= target else "FAIL"

def save_result(actual, target, load, filename="crushing_results.csv"):
    """Save the test result to a CSV file."""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    result = evaluate_test(actual, target)
    data = [timestamp, f"{target:.2f}", f"{load:.2f}", f"{actual:.2f}", result]
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Target Strength (MPa)", "Applied Load (kN)", "Actual Strength (MPa)", "Result"])
        writer.writerow(data)


def main():
    try:
        load = float(input("Enter the applied load in kN: "))
        target_strength = float(input("Enter the target concrete strength in MPa: "))
        actual_strength = calculate_strength(load)
        result = evaluate_test(actual_strength, target_strength)
        save_result(actual_strength, target_strength, load)
        print(f"Actual Strength: {actual_strength:.2f} MPa")
        print(f"Target Strength: {target_strength:.2f} MPa")
        print(f"Test Result: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()