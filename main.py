import read_csv
import json_converter
import search
import json

def main():
    csv_file_path = 'files/google_review_ratings.csv'
    json_file_path = 'data.json'
    
    # Step 1: Read CSV
    csv_data = read_csv.read_csv(csv_file_path)
    
    # Step 2: Convert to JSON
    json_data = json_converter.convert_to_json(csv_data)
    
    # Step 3: Save JSON to file
    json_converter.save_json_to_file(json_data, json_file_path)
    
    # Print JSON data
    print("JSON Data:\n", json_data)
    
    # Step 4: Search in JSON
    search_string = input("Enter a string to search in the JSON data: ")
    
    # Load JSON from the file
    with open(json_file_path, 'r') as file:
        json_data_from_file = json.load(file)
    
    # Call the search function
    search_results = search.search_json(json_data_from_file, search_string)
    
    # Print search results
    print("Search Results:\n", json.dumps(search_results, indent=4))

if __name__ == "__main__":
    main()
