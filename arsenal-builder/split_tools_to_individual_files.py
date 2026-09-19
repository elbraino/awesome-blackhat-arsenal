import os
import json
import re

# ------------------------------------------------------------
# 🧼 Sanitize filenames: remove invalid characters and truncate
# ------------------------------------------------------------
def sanitize_filename(name, fallback="tool", max_length=50):
    name = re.sub(r'[\\/*?:"<>|]', "_", name)  # Replace invalid filename characters
    return name.strip()[:max_length] or fallback

# ------------------------------------------------------------
# 📦 Split all tool objects from each JSON file into separate files
# ------------------------------------------------------------
def split_folder_to_individual_json_objects(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    counter = 0  # For creating unique filenames

    for filename in os.listdir(input_folder):
        if not filename.endswith(".json"):
            continue

        filepath = os.path.join(input_folder, filename)

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                tools = data if isinstance(data, list) else [data]

                for tool in tools:
                    # 🧾 Extract only the desired fields
                    filtered = {
                        "Tool Name": tool.get("tool_name"),
                        "Speakers": tool.get("speakers"),
                        "Tracks": tool.get("tracks"),
                        "Event": tool.get("event"),
                        "Github URL": tool.get("github_url"),
                        "Description": tool.get("description"),
                        "Year": tool.get("Year"),
                        "Location": tool.get("Country")
                    }

                    # 🏷️ Generate a safe filename from actual tool_name
                    raw_name = tool.get("tool_name") or f"tool_{counter}"
                    safe_name = sanitize_filename(raw_name)
                    filename_out = f"{counter:04d}_{safe_name}.json"
                    output_path = os.path.join(output_folder, filename_out)

                    # 💾 Save individual tool JSON
                    with open(output_path, "w", encoding="utf-8") as out_f:
                        json.dump(filtered, out_f, indent=2, ensure_ascii=False)

                    print(f"✅ Saved: {filename_out}")
                    counter += 1

        except Exception as e:
            print(f"⚠️ Skipped {filename} due to error: {e}")

# ------------------------------------------------------------
# 🚀 Entry point — customize input/output folders below
# ------------------------------------------------------------
if __name__ == "__main__":
    input_folder = "Data/Asia"        # Folder with multi-tool JSON files
    output_folder = "Asia/2023"            # Output folder for individual tool JSONs

    split_folder_to_individual_json_objects(input_folder, output_folder)
