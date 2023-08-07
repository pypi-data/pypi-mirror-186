import io
import urllib3 #$ python -m pip install urllib3
import zipfile
class InternetDownloader:
    def __init__(self):
        pass
    @staticmethod
    def download_image(i_url_link=None,i_image_name='image.jpg'):
        assert isinstance(i_url_link,str)
        assert isinstance(i_image_name,str)
        http = urllib3.PoolManager()
        image_data = http.request('GET',i_url_link).data
        with open(i_image_name,'wb') as image:
            image.write(image_data)
    @staticmethod
    def download_zip(i_url_link=None,i_dest_path='Save'):
        print('Downloading zip file...')
        http = urllib3.PoolManager()
        data = http.request('GET', i_url_link).data
        data = zipfile.ZipFile(io.BytesIO(data))
        data.extractall(i_dest_path)
        return True

if __name__ == '__main__':
    print('This module is to download somethings from internets and save to disk')
    InternetDownloader.download_zip(i_url_link=r'https://learnopencv.s3.us-west-2.amazonaws.com/pothole_dataset.zip')
"""=================================================================================================================="""