import sys


def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
    """
    scores = {}

    afinnfile = open(sentiment_file, 'r')
    scores = {}
    for line in afinnfile:
        term, score = line.split('\t')
        scores[term] = int(score)

    afinnfile.close()

    return scores


def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0

    words = tweet.split()

    i = 0
    while(i<len(words)):
        if(i+2<len(words)):
            word1 = words[i]
            word2 = words[i] + words[i+1]
            word3 = words[i] + words[i+1] + words[i+2]

            if(word3 in sent_scores.keys()):
                score += sent_scores[word3]
                i += 3
            elif(word2 in sent_scores.keys()):
                score += sent_scores[word2]
                i += 2
            elif(word1 in sent_scores.keys()):
                score += sent_scores[word1]
                i += 1
            else:
                i += 1
        elif(i+1<len(words)):
            word1 = words[i]
            word2 = words[i] + words[i+1]
            if(word2 in sent_scores.keys()):
                score += sent_scores[word2]
                i += 2
            elif(word1 in sent_scores.keys()):
                score += sent_scores[word1]
                i += 1
            else:
                i += 1
        else:
            word1 = words[i]
            if(word1 in sent_scores.keys()):
                score += sent_scores[word1]
                i += 1
            else:
                i += 1

    return score


def get_sentiment(tweets_file, sent_scores, output_file):
    """A function that finds the sentiment of each tweet and outputs a sentiment score (one per line).

            Args:
                tweets_file (string): The name of the file containing the clean tweets
                sent_scores (dictionary): The dictionary output by the method create_sent_dict
                output_file (string): The name of the file where the output will be written

            Returns:
                None
    """
    tweets = open(tweets_file, 'r')
    output = open(output_file, 'w')
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)
        output.write('%d\n' % score)
    output.close()
    tweets.close()


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]
    output_file = "sentiment.txt"

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)
    # Read the tweet data and assign sentiment
    get_sentiment(tweets_file, sent_scores, output_file)


if __name__ == '__main__':
    main()