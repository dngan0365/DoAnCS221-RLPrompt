import argparse
import gdown
import os

MODEL_URLS = {
    'yelp-train': 'https://drive.google.com/file/d/1AUBbpFcfBkKh5WUGwdXFhHxzZspPRn7W/view?usp=sharing',
    'yelp-test': 'https://drive.google.com/file/d/1VOhHZiYzZy8fzKpFDEqsbwvxO6iJ8dSr/view?usp=sharing',
    'shakespeare-train-100-0': 'https://drive.google.com/file/d/1A-yKYvXovOwumB99UygzC40NrjXgoNeZ/view?usp=sharing',
    'shakespeare-train-100-1': 'https://drive.google.com/file/d/1iW_SVoxHwORTX8aK5DWm3y_AZkEmg7Ny/view?usp=sharing',
    'shakespeare-train-100-2': 'https://drive.google.com/file/d/1PzJN3nXHeBT8-d3iR7vpDOJZPIiW0cfX/view?usp=sharing',
    'shakespeare-test-all': 'https://drive.google.com/file/d/17UMjwFjn2us7EIKr1Pnzx-LHGojlu-zB/view?usp=sharing'
}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', required=True, choices=list(MODEL_URLS.keys()))
    return parser.parse_args()


def download_file_from_google_drive(url, output_path):
    # Extract the file ID from the Google Drive URL
    file_id = url.split('/d/')[1].split('/')[0]
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output=output_path, quiet=False)


if __name__ == "__main__":
    args = parse_args()

    target_path = './style_classifiers'
    os.makedirs(target_path, exist_ok=True)

    # Define the output file path
    output_file_path = f"{target_path}/{args.model_name}.tar.gz"

    # Download the file using gdown
    download_file_from_google_drive(MODEL_URLS[args.model_name], output_file_path)

    # If extraction is needed, add extraction logic here
    # For example, you can use tarfile to extract `.tar.gz` files