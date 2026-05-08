import csv
from datetime import datetime

# Pharmacy Workload Risk Analyzer
# This program helps determine whether a pharmacy shift workload
# is manageable based on staffing levels, total orders,
# urgent STAT orders, and shift length.

# This function calculates a workload score based on:
# - total pharmacy orders
# - number of urgent STAT orders
# - number of staff members
# - hours worked during the shift
# STAT orders are weighted heavier because they require immediate attention.
def calculate_workload_score(orders, staff, hours, stat_orders):

    # Add extra weight to STAT orders to reflect urgency
    weighted_orders = orders + (stat_orders * 1.5)

    # Divide workload by total staff hours available
    score = weighted_orders / (staff * hours)

    # Return the calculated workload score
    return score


# This function determines the workload risk category
# based on the workload score calculated above.
def determine_risk(score):

    # Low workload means staffing is likely sufficient
    if score < 8:
        return "Low"

    # Moderate workload may require monitoring
    elif score < 15:
        return "Moderate"

    # High workload may strain pharmacy operations
    elif score < 22:
        return "High"

    # Critical workload indicates immediate intervention is needed
    else:
        return "Critical"


# This function generates recommendations for pharmacy leadership
# depending on the current workload risk level.
def generate_recommendation(risk):

    # Recommendation for manageable workloads
    if risk == "Low":
        return "Workload appears manageable. Continue normal operations."

    # Recommendation for moderate workload concerns
    elif risk == "Moderate":
        return "Monitor staff closely and consider redistributing tasks."

    # Recommendation for high-risk workload conditions
    elif risk == "High":
        return "Consider adding support staff, adjusting breaks, or reducing non-urgent workload."

    # Recommendation for critical workload situations
    else:
        return "Immediate action recommended: add staff, notify leadership, and prioritize urgent orders."


# This function saves workload analysis results into a CSV file
# so previous shift data can be tracked and reviewed later.
def save_to_csv(data):

    # Name of the CSV file used to store results
    filename = "pharmacy_workload_results.csv"

    # Variable used to determine if the file already exists
    file_exists = False

    # Attempt to open the file in read mode
    # If successful, the file already exists
    try:
        with open(filename, "r"):
            file_exists = True

    # If the file does not exist, continue without crashing
    except FileNotFoundError:
        pass

    # Open the CSV file in append mode to add new results
    with open(filename, "a", newline="") as file:

        # Create a CSV writer object
        writer = csv.writer(file)

        # If the file is brand new, create column headers first
        if not file_exists:
            writer.writerow([
                "Date/Time",
                "Shift",
                "Total Orders",
                "STAT Orders",
                "Staff",
                "Hours",
                "Workload Score",
                "Risk Level",
                "Recommendation"
            ])

        # Write the current analysis data into the CSV file
        writer.writerow(data)

    # Inform the user that the results were saved successfully
    print(f"\nResults saved to {filename}")


# This function gathers user input and runs the workload analysis.
def run_analyzer():

    print("\n--- Pharmacy Workload Risk Analyzer ---")

    # Ask the user for shift information
    shift = input("Enter shift name (Day, Evening, Night): ")

    # Gather workload and staffing information from the user
    orders = int(input("Enter total number of pharmacy orders: "))
    stat_orders = int(input("Enter number of STAT/urgent orders: "))
    staff = int(input("Enter number of pharmacy staff working: "))
    hours = float(input("Enter shift length in hours: "))

    # Prevent division-by-zero errors and invalid staffing values
    if staff <= 0 or hours <= 0:
        print("Error: Staff and hours must be greater than zero.")
        return

    # Calculate workload score using entered data
    score = calculate_workload_score(orders, staff, hours, stat_orders)

    # Determine workload risk category
    risk = determine_risk(score)

    # Generate staffing recommendations
    recommendation = generate_recommendation(risk)

    # Display all workload analysis results to the user
    print("\n--- Analysis Results ---")
    print(f"Shift: {shift}")
    print(f"Total Orders: {orders}")
    print(f"STAT Orders: {stat_orders}")
    print(f"Staff Working: {staff}")
    print(f"Shift Length: {hours} hours")
    print(f"Workload Score: {score:.2f}")
    print(f"Risk Level: {risk}")
    print(f"Recommendation: {recommendation}")

    # Ask the user whether they want to save the results
    save_choice = input(
        "\nWould you like to save these results to a CSV file? (yes/no): "
    ).lower()

    # Save results if the user chooses "yes"
    if save_choice == "yes":

        # Record the current date and time
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a row of data for the CSV file
        row = [
            now,
            shift,
            orders,
            stat_orders,
            staff,
            hours,
            round(score, 2),
            risk,
            recommendation
        ]

        # Save the row into the CSV file
        save_to_csv(row)


# This function demonstrates the analyzer using preset sample data.
# It allows users or instructors to quickly test the program.
def sample_demo():

    print("\n--- Sample Demo Scenario ---")

    # Example shift information
    shift = "Evening"

    # Example workload data
    orders = 320
    stat_orders = 45
    staff = 4
    hours = 8

    # Run calculations using the sample values
    score = calculate_workload_score(orders, staff, hours, stat_orders)
    risk = determine_risk(score)
    recommendation = generate_recommendation(risk)

    # Display the sample analysis results
    print(f"Shift: {shift}")
    print(f"Total Orders: {orders}")
    print(f"STAT Orders: {stat_orders}")
    print(f"Staff Working: {staff}")
    print(f"Shift Length: {hours} hours")
    print(f"Workload Score: {score:.2f}")
    print(f"Risk Level: {risk}")
    print(f"Recommendation: {recommendation}")


# Main program loop that displays the menu
# and allows the user to continue using the program
# until they choose to exit.
def main():

    # Infinite loop keeps program running until exit is selected
    while True:

        # Display main menu
        print("\n==============================")
        print("Pharmacy Workload Risk Analyzer")
        print("==============================")
        print("1. Run Workload Analyzer")
        print("2. View Sample Demo")
        print("3. Exit")

        # Get menu selection from the user
        choice = input("Choose an option: ")

        # Run analyzer option
        if choice == "1":
            run_analyzer()

        # Run sample demo option
        elif choice == "2":
            sample_demo()

        # Exit the program safely
        elif choice == "3":
            print("Thank you for using the Pharmacy Workload Risk Analyzer.")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# Start the program
main()