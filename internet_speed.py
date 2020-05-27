""" Internet Speed """
import speedtest
import argparse

test = speedtest.Speedtest()

def download_speed():
    speed = round(test.download() / 1_000_000, 2)
    return str(speed) + " Mbps"

def upload_speed():
    speed = round(test.upload() / 1_000_000, 2)
    return str(speed) + " Mbps"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--download", action="store_true", help="Test Download Speed")
    group.add_argument("-u", "--upload", action="store_true", help="Test Upload Speed")
    args = parser.parse_args()

    if args.download:
        print(f"\nDownload Speed: {download_speed()}\n")
    elif args.upload:
        print(f"\nUpload Speed: {upload_speed()}\n")
    else:
        print("""\nPlease specify a method:
  -d:  Download speed
  -u:  Upload speed
""")

