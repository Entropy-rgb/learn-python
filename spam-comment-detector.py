def is_spam(comment, keywords):
  """
  Checks if a comment is spam based on a list of keywords.

  Args:
    comment: The comment string to check.
    keywords: A list of keywords that indicate spam.

  Returns:
    True if the comment is spam, False otherwise.
  """
  comment = comment.lower()  # Convert comment to lowercase for case-insensitive matching
  for keyword in keywords:
    if keyword.lower() in comment:
      return True
  return False


user_comment = ""
print('================================')
print("Type 'exit' to exit this program")
print('================================')
# Define the spam keywords
spam_keywords = ["Make a lot of money", "buy now", "subscribe this", "click this"]
while user_comment != 'exit':
    # Get input from the user
    user_comment = input("Please enter a comment to check for spam: ")

    # Check the user's comment and print the result
    if is_spam(user_comment, spam_keywords):
        print(f"The comment '{user_comment}' is SPAM")
    else:
        print(f"The comment '{user_comment}' is NOT SPAM")