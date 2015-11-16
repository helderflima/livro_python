__author__ = 'helder'
# coding: utf-8
import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def main():
    response = request.urlopen(sys.argv[1])
    print(response)
    output = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader('Content-Length')
    print(response.getheader(content_length))
    if content_length:
        length = int(content_length)
        download_length(response, output, length)
    else:
        download(response, output)
    response.close();
    output.close();
    print("Finished")

def download_length(response, output, length):

    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d " % (((time * BUFF_SIZE)/length)*100))

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes} '.format(bytes=total_downloaded))

if __name__ == '__main__':
   main()
