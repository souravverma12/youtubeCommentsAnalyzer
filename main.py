from flask import Flask, render_template, request
import pyfile_web_scraping, sentiment_analysis_youtube_comments
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/scrap', methods=['POST'])
def scrap_comments():
    url = request.form.get('youtube url')

    file_and_detail = pyfile_web_scraping.scrapfyt(url)
    sentiment = sentiment_analysis_youtube_comments.sepposnegcom("Full Comments.csv")

    video_title, video_owner, video_comment_with_replies, video_comment_without_replies, *extra_data = file_and_detail
    pos_comments_csv = pd.read_csv('Positive Comments.csv')
    neg_comments_csv = pd.read_csv('Negative Comments.csv')
    
    video_posive_comments = sentiment[2]
    video_negative_comments = sentiment[3]

    return render_template(
    'index.html', 
    after_complete_message="Scraping Complete!", 
    title=video_title, 
    owner=video_owner, 
    comment_w_replies=video_comment_with_replies, 
    comment_wo_replies=video_comment_with_replies, 

    pos_comments_csv=pos_comments_csv.to_html(classes='dataframe', index=False), neg_comments_csv=neg_comments_csv.to_html(classes='dataframe', index=False)
)


    #return render_template("index.html", title=video_title,
     #                      owner=video_owner, comment_w_replies=video_comment_with_replies,
      #                     comment_wo_replies=video_comment_without_replies,
       #                    pos_comments_csv=pos_comments_csv.to_html(), neg_comments_csv=neg_comments_csv.to_html())

if __name__ == "__main__":
    app.run(debug=True)

#positive_comment=video_posive_comments, negative_comment=video_negative_comments,