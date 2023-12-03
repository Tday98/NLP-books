import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import re


def analyze():
    """
    grabs the paths of the diary txt files from diary folder
    use regex to grab the dates
    run the NLTK SentimentIntensityAnalyzer on the individual
    text files and save it to the scores dictionary in {date: values} format
    :return scores:
    """
    scores = {}
    diary_list = glob.glob("./diary/**")
    diary_list = sorted(diary_list)
    regex = re.compile('[^./diary/][0-9]+-[0-9]+-[0-9]+[^.txt]')
    for diary in diary_list:
        findings = re.findall(regex, diary)
        with open(diary, "r") as diary_text:
            analyzer = SentimentIntensityAnalyzer()
            diary_individual = diary_text.read()
            scores[findings[0]] = analyzer.polarity_scores(diary_individual)
    return scores


if __name__ == "__main__":
    analyze()
