#!/usr/bin/env python

import requests
import os

def download_bag_files(urls):

    # check if bag_files directory exists, else create a new one
    directory = os.path.join(os.getcwd(), "data", "bag_files")
    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in urls:

        # extract bag_ID from url
        bag_ID = url

        # extract link of the bag file
        link = urls[url]

        # check that a file exists on the defined url
        response = requests.head(link)
        if response.status_code != 200:
            raise RuntimeError("Cannot find the file {} at the link {}".format(bag_ID, link))

        # define bag_name but also prevent errors for bag_ID misunderstanding (bag_ID should be without .bag extension)
        if ".bag" in bag_ID:
            bag_name = os.path.join(directory, bag_ID)
        else:
            bag_name = os.path.join(directory, bag_ID + ".bag")

        if not os.path.isfile(bag_name):
            print("Downloading {}.".format(bag_ID))
            # download file and save it to a bag file
            r = requests.get(link, allow_redirects=True)
            open(bag_name, 'wb').write(r.content)

        # print which bag files have been downloaded so far
        if ".bag" in bag_ID:
            print("The {} file is downloaded.".format(bag_ID))
        else:
            print("The {}.bag file is downloaded.".format(bag_ID))


def main():

    # print('Trying to download')
    # insert the bag_IDs and urls of the bag files that you want to download
            # define bag_ID for better error message management
            # define full link to bag file to minimize potential link errors
    urls = {
        # "bag_ID" : "full link to bag file"
        # "20180108135529_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108135529_a313.bag",
        # "20180108141006_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141006_a313.bag",
        # "20180108141155_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141155_a313.bag",
        # "20180108141448_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141448_a313.bag",
        # "20180108141719_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141719_a313.bag",

        # # "20170925205642_bumblebe": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20170925205642_bumblebe.bag",
        # "20171113190125_sharkduc": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171113190125_sharkduc.bag",
        "20171115200334_raven": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171115200334_raven.bag",
        "20171128034730_shamrock": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171128034730_shamrock.bag",
        # "20171129194137_ducktape": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171129194137_ducktape.bag",
        # "20171129200600_ducktape": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171129200600_ducktape.bag",
        "20171208104308_flitzer": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171208104308_flitzer.bag",
        "20171208104942_flitzer": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171208104942_flitzer.bag",
        "20171222161318_yaf": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171222161318_yaf.bag",
        "20171222164854_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171222164854_a313.bag",
        "20171222170143_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171222170143_a313.bag",
        "20171226184622_yaf": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171226184622_yaf.bag",
        "20171226184929_yaf": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171226184929_yaf.bag",
        "20171226185149_yaf": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20171226185149_yaf.bag",
        "20180104160023_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104160023_a313.bag",
        "20180104160326_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104160326_a313.bag",
        "20180104160628_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104160628_a313.bag",
        "20180104161012_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104161012_a313.bag",
        "20180104161713_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104161713_a313.bag",
        "20180104184212_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104184212_a313.bag",
        "20180104184537_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104184537_a313.bag",
        "20180104184952_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104184952_a313.bag",
        "20180104185251_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104185251_a313.bag",
        "20180104185603_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104185603_a313.bag",
        "20180104190924_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104190924_a313.bag",
        "20180104191210_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104191210_a313.bag",
        "20180104191413_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104191413_a313.bag",
        "20180104191716_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104191716_a313.bag",
        "20180104193114_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104193114_a313.bag",
        "20180104194245_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180104194245_a313.bag",
        "20180108135251_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108135251_a313.bag",
        "20180108135529_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108135529_a313.bag",
        "20180108140736_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108140736_a313.bag",
        "20180108141006_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141006_a313.bag",
        "20180108141155_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141155_a313.bag",
        "20180108141448_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141448_a313.bag",
        "20180108141719_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108141719_a313.bag",
        "20180108195947_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108195947_a313.bag",
        "20180108200202_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108200202_a313.bag",
        "20180108200650_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108200650_a313.bag",
        "20180108201149_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180108201149_a313.bag",
        "20180111102628_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180111102628_a313.bag",
        "20180111103659_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180111103659_a313.bag",
        "20180111104301_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180111104301_a313.bag",
        "20180111105758_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180111105758_a313.bag",
        "20180111130129_a313": r"http://ipfs.duckietown.org:8080/ipfs/QmUbtwQ3QZKmmz5qTjKM3z8LJjsrKBWLUnnzoE5L4M7y7J/logs/20180111130129_a313.bag"

    }

    # download bag files
    download_bag_files(urls)

if __name__ == "__main__":
    main()

