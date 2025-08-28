# zip-postal-code-lookup

A worldwide Python tool to lookup postal codes and return detailed information including city, state, latitude, longitude, and accuracy. Supports saving results to CSV or JSON.

---

## Features

- Lookup any postal code worldwide using ISO country codes.
- Returns full details: place name, state/province, country code, latitude, longitude, accuracy.
- Optional export to CSV and JSON.
- Handles invalid or unknown postal codes gracefully.

---

## Prerequisites

- Python 3.x  
- `pgeocode` library

Install the required library:

```bash
pip install pgeocode
```

---

## Usage

1. Clone the repository or download the script.
2. Run the script:

```bash
python lookup.py
```

3. Enter the postal code when prompted.
4. Enter the ISO country code (e.g., US, CA, FR). Leave blank for default US.
5. The script will display detailed information.
6. Optionally, save results to CSV or JSON.

### Example

```bash
Enter ZIP/Postal Code: 94103
Enter ISO country code (default US): 
Details found:
postal_code: 94103
country_code: US
place_name: San Francisco
state_name: California
latitude: 37.7725
longitude: -122.4147
accuracy: 4.0
Save results to CSV? (y/n): y
Saved results to postal_lookup.csv
Save results to JSON? (y/n): y
Saved results to postal_lookup.json
```

---

## Notes

- ISO country codes are standard 2-letter codes (e.g., US, GB, FR, JP).
- Accuracy field indicates how precise the data is (1=low, 4=high).
- Works worldwide with supported countries from `pgeocode`.

---

## License

Open-source and free to use for learning and experimentation purposes.