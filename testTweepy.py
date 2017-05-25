import tweepy

auth = tweepy.OAuthHandler("7wQKiEEoanM2WaWfVihYmkSlR","6Ubv7nlcqWmyrhYOeQeSAI7TI2K9lXJKxUhQce403STeicyNuP")
auth.set_access_token("92749485-LwiTa0wFLAaUkEbqvYnq91skuYTfAGrmGcNTOhBNp","gr9IurnBfS5OKuGJdA4k4mvGpeSO4xdZvFkjgELJezdeA")
api = tweepy.API(auth)

for page in tweepy.Cursor(api.followers, screen_name="swathyGoru").items():
    print page.screen_name

