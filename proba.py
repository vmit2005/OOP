import requests

img_url = "https://vodomotorika.ru/userfiles/shop_items/7929/1.jpg"
# video_url='https://zavod-spb.ru/wp-content/uploads/2021/03/translation.mp4'
video_url='https://video.aliexpress-media.com/play/u/ae_sg_item/2211031663284/p/1/e/6/t/10301/306731706753.mp4%60'


def download_img(url=''):
    try:
        # response = requests.get(url=url)

        with open('reg_img1.jpg', 'wb') as file:
            file.write(response.content)
        response = requests.get(url=url,stream=True)
        return "img downloaded"
        with open('reg_img1.jpg', 'wb') as file:
            for chunk in response.

    except Exception as _ex:
        return "Upps..."

def download_video(url=''):
    try:
        response = requests.get(url=url)

        with open('reg_video.mp4', 'wb') as file:
            file.write(response.content)
        return "img downloaded"

    except Exception as _ex:
        return "Upps..."


def main():
    # print(download_img(url=img_url))
    print(download_video(url=video_url))


if __name__ == '__main__':
    main()