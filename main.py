import urllib.request
import re
import os
from tqdm import tqdm
import argparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

CVF_URL = "https://openaccess.thecvf.com"


def get_url(conference: str, year: int):
    return f"{CVF_URL}/{conference}{year}?day=all"


def download_papers(conference: str, year: int, enumerate_papers=False):
    # Download the html file where papers are posted
    html_name = f"{conference}_papers_{year}.html"
    if not os.path.exists(html_name):
        print("Downloading HTML file...")
        cvf_webpage = get_url(conference, year)
        urllib.request.urlretrieve(cvf_webpage, html_name)
    else:
        print("HTML file exists!")

    html_file = open(html_name, "r", encoding="utf8")
    html_content = html_file.read()
    html_file.close()

    # Parse the html file and get the corresponding paper links
    papers_links = re.findall(r"\[<a href=\"(.*)\">pdf</a>\]", html_content)
    print(f"Number of papers in {conference} {year}: {len(papers_links)}")

    # Download papers
    output_dir = f"{conference}_papers_{year}"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    print("Downloading...")
    for i in tqdm(range(len(papers_links))):
        paper_link = papers_links[i]
        full_paper_link = CVF_URL + paper_link
        paper_name = full_paper_link.split('/')[-1]
        if enumerate_papers:
            paper_name = f"{i}_{paper_name}"
        output_path = os.path.join(output_dir, paper_name)
        urllib.request.urlretrieve(full_paper_link, output_path)
    print("Download finished!")


if __name__ == "__main__":
    parser = ArgumentParser(description="Script for downloading the papers of the CVFs conferences",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("--conference",
                        default="CVPR",
                        type=str,
                        choices=["CVPR", "ICCV", "WACV"],
                        help="Name of the conference")
    parser.add_argument("--year",
                        default=2022,
                        type=int,
                        choices=range(2021, 2023),
                        help="Year of the conference")
    parser.add_argument("--enumerate",
                        action=argparse.BooleanOptionalAction,
                        help="Add and ID at the beginning of the paper")

    args = parser.parse_args()

    download_papers(args.conference, args.year, enumerate_papers=args.enumerate)
