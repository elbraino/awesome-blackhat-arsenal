import os
import sys
import json
import re

def remove_numbers_prefix(name):
    # Removes leading number prefixes like 123_ or 123_456_
    return re.sub(r'^\d+(?:_\d+)*_', '', name)

def process_country_folder(input_root: str, output_root: str, country: str):
    country_input_path = os.path.join(input_root, country)
    
    if not os.path.exists(country_input_path):
        print(f"❌ Folder not found: {country_input_path}")
        return

    for year in os.listdir(country_input_path):
        year_path = os.path.join(country_input_path, year)
        if not os.path.isdir(year_path):
            continue

        for tool_file in os.listdir(year_path):
            if not tool_file.endswith(".json"):
                continue
            
            input_file_path = os.path.join(year_path, tool_file)
            
            # Load JSON content
            try:
                with open(input_file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Invalid JSON in: {input_file_path}")
                continue
            
            # Clean tool file name
            cleaned_file_name = remove_numbers_prefix(tool_file)

            # Prepare output path
            output_dir = os.path.join(output_root, country, year)
            os.makedirs(output_dir, exist_ok=True)
            
            output_file_path = os.path.join(output_dir, cleaned_file_name)
            with open(output_file_path, "w", encoding="utf-8") as out_f:
                json.dump(data, out_f, indent=2, ensure_ascii=False)
            
            print(f"✅ Processed: {output_file_path}")

if __name__ == "__main__":
    # Usage: python3 flatten_tool_files.py <Country>   (e.g. Asia)
    input_root = "arsenal-builder"
    output_root = "tools"
    country = sys.argv[1].strip() if len(sys.argv) > 1 else input("Enter country folder name: ").strip()
    
    process_country_folder(input_root, output_root, country)
