import os
import re

def update_css_links(directory):
    pattern = re.compile(r'(<link[^>]+href=["\'])/marvelrivals/assets/css/main\.css(["\'])')
    
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            updated_content = pattern.sub(r'\1/marvelrivals/assets/css/output.css\2', content)
            
            if content != updated_content:  # Only overwrite if there's a change
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(updated_content)
                print(f"Updated: {filename}")
            else:
                print(f"No change needed: {filename}")

if __name__ == "__main__":
    directory = "./docs/characters"  # Change this if needed
    update_css_links(directory)
