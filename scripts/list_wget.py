from pathlib import Path

from lancefennell.data import data

download_path = Path('./asset_urls.txt')
assets_path = Path('./assets/img')

def main():
    assets_path.mkdir(exist_ok=True, parents=True)

    with download_path.open(mode='w') as f:
        for item in data:
            f.write(f"{item['index_img_href']}\n")
            f.write(f"{item['detail_img_href']}\n")

if __name__ == '__main__':
    main()
