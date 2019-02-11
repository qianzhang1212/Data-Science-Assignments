Check cs639 repo for tweets.json

#Convert more than 2 letter repetitions to 2 letter. Example: funnnnny --> funny

#TODO: The next line should implement the functionality in the above comment.

word = re.sub(r'(a-zA-Z)\1{2,}', r'\1\1', word, flags = re.DOTALL)

#Remove RT (retweet)

#TODO: The next line should implement the functionality in the above comment

#\b word border

tweet = re.sub(r'\brt\b', '', tweet)
