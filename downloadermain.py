from pytube import YouTube
import os

url = input(str("Enter URL: "))
video = YouTube(url)
print("Downloading... ")

