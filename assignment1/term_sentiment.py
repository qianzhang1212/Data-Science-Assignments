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

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}

    tweets = open(tweets_file, 'r')
    for tweet in tweets:
        score = get_tweet_sentiment(tweet, sent_scores)
        words = tweet.strip().split(" ")
        for word in words:
            if not word:
                continue
            if(word not in sent_scores.keys()):
                if(word not in new_term_sent.keys()):
                    new_term_sent[word] = []
                new_term_sent[word].append(score)

    for key in new_term_sent.keys():
        new_term_sent[key] = sum(new_term_sent[key])/float(len(new_term_sent[key]))

    return new_term_sent

def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    save_to_file = open("new_term.txt", 'w')

    for term in new_term_sent.keys():
        print(term + " {0:.2f}".format(new_term_sent[term]))
        #save_to_file.write('%s\n' % (term + " {0:.2f}".format(new_term_sent[term])))
    #save_to_file.close()

    #print(len(new_term_sent))

if __name__ == '__main__':
    main()