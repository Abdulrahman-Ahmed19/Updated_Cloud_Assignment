import re
from collections import Counter

# Read the contents of the file (replace with your actual file path)
file_path = '/appllication/Random_Paragraphs.txt'
with open(file_path, "r") as file:
    text = file.read()

# Define a list of common stop words
stop_words = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
    "themselves", "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after", "above",
    "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
    "again", "further", "then", "once", "here", "there", "when", "where", "why", "how",
    "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can",
    "will", "just", "don", "should", "now","also"
])

# Use regular expression to find words and filter out stop words
filtered_words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in stop_words]

# Count the frequency of each word
word_counts = Counter(filtered_words)

# Order words by frequency (descending)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Display word frequency count
for word, count in sorted_word_counts:
    print(f"{word}: {count}")