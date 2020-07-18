# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_choice(email, censor_phrase):
    text_censored = email.replace(censor_phrase, " ")
    return text_censored

#print(censor_choice(email_one, "learning algorithms"))
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
def censorlist(email, lst):
    for word in lst:
        text_censored = email.replace(word, " ")
        return text_censored

#print(censorlist(email_two,proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censorneg(email, lst):
  censorlist(email, proprietary_terms)
  for word in negative_words:
    counter = 0
    if word in email:
      counter += 1
      if counter >=2:
        email = email.replace(word, " ")
  return email

#print(censorneg(email_three, negative_words))  


def extremecensor(email, lst, negatives):
    text = censorneg(email, lst)
    text_split = text.split()
    for word in text_split:
        if word.count(" ") >= 1:
            index = text_split.index(word)
            word_before = text_split[index - 1]
            word_after = text_split[index + 1]
            text_split[index - 1] = " " * len(word_before)
            text_split[index + 1] = " " * len(word_after)
    return " ".join(text_split)

print(extremecensor(email_three, proprietary_terms, negative_words))
