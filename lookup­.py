import pgeocode
import csv
import json

def lookup_postal_code(zip_code, country="US"):
    nomi = pgeocode.Nominatim(country)
    info = nomi.query_postal_code(zip_code)
    if info.empty or info.place_name is None:
        return None
    
    details = {
        "postal_code": zip_code,
        "country_code": info.country_code,
        "place_name": info.place_name,
        "state_name": info.state_name,
        "latitude": info.latitude,
        "longitude": info.longitude,
        "accuracy": info.accuracy
    }
    return details

def save_to_csv(details, filename="postal_lookup.csv"):
    keys = details.keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerow(details)
    print(f"Saved results to {filename}")

def save_to_json(details, filename="postal_lookup.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(details, f, ensure_ascii=False, indent=4)
    print(f"Saved results to {filename}")

if __name__ == "__main__":
    zip_code = input("Enter ZIP/Postal Code: ").strip()
    country = input("Enter ISO country code (default US): ").strip().upper() or "US"

    details = lookup_postal_code(zip_code, country)
    if not details:
        print(f"No information found for {zip_code} in {country}")
    else:
        print("Details found:")
        for k, v in details.items():
            print(f"{k}: {v}")

        save_csv = input("Save results to CSV? (y/n): ").strip().lower() == "y"
        if save_csv:
            save_to_csv(details)

        save_json = input("Save results to JSON? (y/n): ").strip().lower() == "y"
        if save_json:
            save_to_json(details)