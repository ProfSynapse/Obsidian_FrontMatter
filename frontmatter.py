import os
import yaml

def load_config(config_file):
    """Loads configuration from a YAML file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        dict: Configuration data.
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def add_yaml_front_matter_to_file(file_path, yaml_front_matter):
    """Adds the specified YAML front matter to a markdown file.

    Args:
        file_path (str): The path to the markdown file.
        yaml_front_matter (str): The YAML front matter to add.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Check if the file already has front matter
    if content.startswith('---'):
        print(f"File {file_path} already contains YAML front matter. Skipping.")
        return

    # Create the new content with YAML front matter
    new_content = f"---\n{yaml_front_matter}\n---\n\n{content}"

    with open(file_path, 'w') as file:
        file.write(new_content)

    print(f"Added YAML front matter to {file_path}")

def process_folder(folder_path, yaml_front_matter):
    """Processes all markdown files in a folder, adding the specified YAML front matter.

    Args:
        folder_path (str): The path to the folder containing markdown files.
        yaml_front_matter (str): The YAML front matter to add to each file.
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                add_yaml_front_matter_to_file(file_path, yaml_front_matter)

if __name__ == "__main__":
    config_file = "config.yaml"
    config = load_config(config_file)

    folder_path = config['folder_path']
    yaml_front_matter = config['yaml_front_matter']

    process_folder(folder_path, yaml_front_matter)
