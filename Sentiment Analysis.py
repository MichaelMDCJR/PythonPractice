from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *

# Clear all fields
def clear_all():
    negField.delete(0, END)
    posField.delete(0, END)
    neutField.delete(0, END)
    overField.delete(0, END)

    text_box.delete(1.0, END)


def detect_sentiment():
    # Get sentence
    sentence = text_box.get("1.0", "end")

    # Create a sentiment analyzer
    sent_analyzer = SentimentIntensityAnalyzer()

    sentiment_dict = sent_analyzer.polarity_scores(sentence)

    # Determine the intensity of string and put in in fields
    neg_string = str(sentiment_dict['neg']*100) + "% Negative"
    negField.insert(10, neg_string)

    pos_string = str(sentiment_dict['pos']*100) + "% Positive"
    posField.insert(10, pos_string)

    neut_string = str(sentiment_dict['neu']*100) + "% Neutral"
    neutField.insert(10, neut_string)

    # Decide if statement is positive, negative, or neutral
    if sentiment_dict['compound'] >= 0.05:
        string = "Positive"
    elif sentiment_dict['compound'] <= -0.05:
        string = "Negative"
    else:
        string = "Neutral"

    overField.insert(10, string)


if __name__ == "__main__":
    # Create GUI
    root = Tk()
    root.title("Sentiment Detector")
    root.geometry("250x400")

    # Prompt
    sentence_label = Label(root, text="Enter your sentence")

    # Text box for sentence
    text_box = Text(root, height=5, width=25)

    # Button for submitting
    submit = Button(root, text = "Check Sentiment", command=detect_sentiment)

    # Create labels for positive, negative, neutral, and overall sentiment
    negative = Label(root, text="Sentence was rated as: ")
    positive = Label(root, text="Sentence was rated as: ")
    neutral = Label(root, text="Sentence was rated as: ")
    overall = Label(root, text="Sentence was overall rated as: ")

    # Text boxes for sentiment ratings
    negField = Entry(root)
    posField = Entry(root)
    neutField = Entry(root)
    overField = Entry(root)

    # Button to clear text fields
    clear = Button(root, text="Clear", command=clear_all)

    sentence_label.grid(row=0, column=2)
    text_box.grid(row=1, column=2, padx=10, sticky=W)
    submit.grid(row=2, column=2)
    negative.grid(row=3, column=2)
    neutral.grid(row=5, column=2)
    positive.grid(row=7,column=2)
    overall.grid(row=9, column=2)
    negField.grid(row=4,column=2)
    neutField.grid(row=6, column=2)
    posField.grid(row=8, column=2)
    overField.grid(row=10, column=2)
    clear.grid(row=11, column=2)



    root.mainloop()