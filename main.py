from sna.SentimentScoreGenerator import SentimentScoreGenerator
from sna.YTExtractor import YTExtractor
from googleapiclient.discovery import build
import googleapiclient.discovery
import pandas as pd
import seaborn as sb
import openai


def main():
    YTData = YTExtractor()
    YTData.