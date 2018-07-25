import csv
import os
import fire

from os.path import isdir, join


def get_rows(path, start_id=0):

    for label in sorted(os.listdir(path)):
        label_path = join(path, label)
        if isdir(label_path):
            for file_name in sorted(os.listdir(label_path)):
                text_path = join(label_path, file_name)
                text = read_text(text_path)
                row = [start_id, text, label]
                start_id += 1
                yield row


def read_text(path):
    with open(path, "r", newline='') as input_file:
        text = input_file.read()
        return text


def convert_txt_to_csv(input_path, output_path):
    with open(output_path, "w", newline='') as output_file:
        writer = csv.writer(output_file)
        for row in get_rows(input_path):
            writer.writerow(row)


def main(dataset_dir, output_path="data/bbc_news.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    convert_txt_to_csv(dataset_dir, output_path)


if __name__ == '__main__':
  fire.Fire(main)
