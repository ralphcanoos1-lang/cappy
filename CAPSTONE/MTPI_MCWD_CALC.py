""" Program File Name: MTPI_MCWD_CALC.py
Description: A Python program that will simulate MCWD calculation on water consumption.
Author: Jan Wharey Restauro
Date Started: October 04, 2025
Date Finished: October 25, 2025
Submitted to: Rey Cal """

# ============================================================================
# Problem 1 Pseudo code
# ============================================================================
# START
# 1. Import necessary modules (os for clearing screen)
# 2. Define program header with file information
# 3. Define constants for water rates and charges
# 4. Create function to clear screen
# 5. Create function to display centered title
# 6. Create function to get consumer information
# 7. Create function to get meter information
# 8. Create function to calculate water consumption
# 9. Create function to calculate charges (WATER FEE, FRANCHISE, PCA, PWA)
# 10. Create function to display billing details
# 11. Main program execution flow
# END
# ============================================================================

# ============================================================================
# Problem 1
# ============================================================================

import os
from datetime import datetime

# Constants for billing calculation
WATER_RATE_PER_CUBIC_METER = 25.00  # Example rate, adjust as needed
FRANCHISE_TAX_RATE = 0.05  # 5%
PCA_RATE = 0.02  # 2%
PWA_RATE = 0.01  # 1%

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================================================================
# Problem 2 Pseudo code
# ============================================================================
# START
# 1. Calculate terminal width
# 2. Get title text
# 3. Calculate padding needed for centering
# 4. Print empty lines for vertical centering
# 5. Print centered title with proper spacing
# 6. Print separator line
# END
# ============================================================================

# ============================================================================
# Problem 2
# ============================================================================

def display_title():
    """Display the program title centered on screen"""
    terminal_width = 80  # Standard terminal width
    title = "MCWD Billing Calculator"
    
    # Center the title
    padding = (terminal_width - len(title)) // 2
    print("\n" * 2)  # Add some vertical spacing
    print(" " * padding + title)
    print("=" * terminal_width)
    print()

# ============================================================================
# Problem 3 Pseudo code
# ============================================================================
# START
# 1. Display "CONSUMER INFORMATION" section header
# 2. Prompt for Name (left-aligned at column position)
# 3. Prompt for Address (left-aligned at column position)
# 4. Display empty line for spacing
# 5. Prompt for Consumer Type (left-aligned)
# 6. Prompt for Account Code (left-aligned)
# 7. Display empty line for spacing
# 8. Display "METER INFORMATION" section header
# 9. Prompt for Brand (left-aligned)
# 10. Prompt for Serial Number (left-aligned)
# 11. Prompt for Size (left-aligned)
# 12. Prompt for Period From date (left-aligned)
# 13. Prompt for Period To date (left-aligned)
# 14. Prompt for Due Date (left-aligned)
# 15. Prompt for Previous Reading (left-aligned)
# 16. Prompt for Current Reading (left-aligned)
# 17. Prompt for verification question
# 18. Return all collected data
# END
# ============================================================================

# ============================================================================
# Problem 3
# ============================================================================

def get_consumer_information():
    """Get consumer information with proper prompt positioning"""
    print("CONSUMER INFORMATION")
    print()
    
    # Consumer Information - Left side
    name = input("Name      : ").strip()
    address = input("Address   : ").strip()
    print()
    
    consumer_type = input("Consumer Type : ").strip() or "Regular"
    account_code = input("Account Code  : ").strip()
    
    return {
        'name': name,
        'address': address,
        'consumer_type': consumer_type,
        'account_code': account_code
    }

def get_meter_information():
    """Get meter information with proper prompt positioning"""
    print("\nMETER INFORMATION")
    print()
    
    brand = input("Brand          : ").strip()
    serial_number = input("Serial Number  : ").strip()
    size = input("Size           : ").strip()
    period_from = input("Period From    : ").strip()
    period_to = input("Period To      : ").strip()
    due_date = input("Due Date       : ").strip()
    
    print()
    date = input("Date           : ").strip()
    previous_reading = int(input("Reading        : ").strip())
    
    print()
    current_reading = int(input("Reading        : ").strip())
    consumption = current_reading - previous_reading
    
    print()
    verification = input("Are All Entries Correct? (Y/N): ").strip().upper()
    
    return {
        'brand': brand,
        'serial_number': serial_number,
        'size': size,
        'period_from': period_from,
        'period_to': period_to,
        'due_date': due_date,
        'date': date,
        'previous_reading': previous_reading,
        'current_reading': current_reading,
        'consumption': consumption,
        'verification': verification
    }

def calculate_charges(consumption):
    """Calculate all billing charges"""
    # Base water fee calculation
    water_fee = consumption * WATER_RATE_PER_CUBIC_METER
    
    # Calculate taxes and additional charges
    franchise = water_fee * FRANCHISE_TAX_RATE
    pca = water_fee * PCA_RATE
    pwa = water_fee * PWA_RATE
    
    # Total sales
    total_sales = water_fee + franchise + pca + pwa
    
    return {
        'water_fee': water_fee,
        'franchise': franchise,
        'pca': pca,
        'pwa': pwa,
        'total_sales': total_sales
    }

def display_billing_details(consumer_info, meter_info, charges, previous_balance=0.00, advance_payment=0.00):
    """Display the complete billing information"""
    clear_screen()
    display_title()
    
    # Display Consumer Information and Billing Details side by side
    print(f"CONSUMER INFORMATION")
    print()
    print(f"Name      : {consumer_info['name']:<30} BILLING DETAILS")
    print(f"Address   : {consumer_info['address']:<30} Charges          Period        Amount")
    print(f"                                               WATER FEE        {meter_info['period_to']:<12} {charges['water_fee']:>7.2f}")
    print(f"                                               FRANCHISE        {meter_info['period_to']:<12} {charges['franchise']:>7.2f}")
    print(f"Consumer Type : {consumer_info['consumer_type']:<20} PCA              {meter_info['period_to']:<12} {charges['pca']:>7.2f}")
    print(f"Account Code  : {consumer_info['account_code']:<20} PWA              {meter_info['period_to']:<12} {charges['pwa']:>7.2f}")
    print()
    print(f"              METER INFORMATION                Total Sales                        {charges['total_sales']:>7.2f}")
    print(f"Brand          : {meter_info['brand']:<15} Date      Reading  Consumption  Previous Balance :          {previous_balance:>7.2f}")
    print(f"Serial Number  : {meter_info['serial_number']:<15} {meter_info['date']:<10} {meter_info['previous_reading']:<8} {meter_info['consumption']:<12} Advance Payment  :         {advance_payment:>7.2f}")
    print(f"Size           : {meter_info['size']:<15} {meter_info['period_to']:<10} {meter_info['current_reading']:<8}")
    
    total_amount_due = charges['total_sales'] + previous_balance - advance_payment
    print(f"Period From    : {meter_info['period_from']:<15}")
    print(f"Period To      : {meter_info['period_to']:<15}                                   Total Amount Due :          {total_amount_due:>7.2f}")
    print(f"Due Date       : {meter_info['due_date']:<15} Are All Entries Correct? (Y/N): {meter_info['verification']}")
    print()
    print("=" * 80)

def main():
    """Main program execution"""
    clear_screen()
    display_title()
    
    # Get consumer information
    consumer_info = get_consumer_information()
    
    # Get meter information
    meter_info = get_meter_information()
    
    # Check if user confirmed entries
    if meter_info['verification'] == 'Y':
        # Calculate charges
        charges = calculate_charges(meter_info['consumption'])
        
        # Get additional billing information
        print()
        previous_balance = float(input("Previous Balance  : ").strip() or "0")
        advance_payment = float(input("Advance Payment   : ").strip() or "0")
        
        # Display final billing details
        display_billing_details(consumer_info, meter_info, charges, previous_balance, advance_payment)
    else:
        print("\nPlease re-enter the information correctly.")
        main()  # Restart the process

# Run the program
if __name__ == "__main__":
    main()
