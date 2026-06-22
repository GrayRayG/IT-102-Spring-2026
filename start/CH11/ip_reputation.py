#!/usr/bin/env python3
# Script that checks the reputation of an IP address using the AbuseIPDB API
# By Ray G Peckham

"""
This script checks IP reputation using the AbuseIPDB API
It takes an IP address as input and returns abuse data about that IP
"""

#libraries utilized
import os
import re
import requests
from dotenv import load_dotenv

#load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")


def validate_ip(ip: str) -> bool:
    """
    Validate that the input looks like a real IP address
    Using regex to check the format
    """
    #pattern checks for four groups of 1-3 digits separated by dots
    pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    return bool(pattern.match(ip))


def check_ip_reputation(ip_address: str) -> dict:
    """
    Send a GET request to the AbuseIPDB API and return the response
    1.) Set the headers with the API key for authentication
    2.) Make the request to the API endpoint with the IP
    3.) Return the JSON response data
    """
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    #maxAgeInDays=90 pulls reports from the last 90 days
    response = requests.get(
        f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}&maxAgeInDays=90",
        headers=headers
    )
    return response.json()


def display_results(data: dict):
    """
    Take the raw API response and display it in a readable format
    instead of dumping raw JSON to the screen
    """
    #pull the data section out of the response
    info = data.get("data", {})

    print("\n--- IP Reputation Report ---")
    print(f"IP Address     : {info.get('ipAddress')}")
    print(f"Country        : {info.get('countryCode')}")
    print(f"Usage Type     : {info.get('usageType')}")
    print(f"ISP            : {info.get('isp')}")
    print(f"Abuse Score    : {info.get('abuseConfidenceScore')}%")
    print(f"Total Reports  : {info.get('totalReports')}")
    print(f"Last Reported  : {info.get('lastReportedAt')}")

    #check the score and flag the IP based on risk level
    score = info.get("abuseConfidenceScore", 0)
    if score >= 75:
        print("\n [HIGH RISK] This IP has a high abuse confidence score")
    elif score >= 25:
        print("\n [MODERATE RISK] This IP has been reported for abuse")
    else:
        print("\n [LOW RISK] This IP looks clean")


def main():
    print("AbuseIPDB IP Reputation Checker")

    #make sure the API key loaded correctly before doing anything
    if not API_KEY:
        print("Error: API key not found. Please check your .env file")
        return

    #get an IP address from the user and validate it with regex
    while True:
        ip_address = input("Enter an IP address to check: ").strip()
        if validate_ip(ip_address):
            break
        print("That does not look like a valid IP address, please try again")

    print(f"\nChecking {ip_address} against AbuseIPDB...")

    #make the API call
    result = check_ip_reputation(ip_address)

    #display the results in a clean format
    display_results(result)


if __name__ == "__main__":
    main()