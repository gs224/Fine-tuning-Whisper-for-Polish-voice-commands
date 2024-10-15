# exercise_2.py
# BPE and WordPiece Tokenization with Data Download and Preprocessing

from datasets import load_dataset
import string
from collections import Counter
from tqdm import tqdm


# Step 1: Pre-implemented Byte Pair Encoding (BPE)
class BPEncoder:
    def __init__(self, alphabet, merge_rules, bpe_cache=dict()):
        self.alphabet = alphabet
        self.merge_rules = merge_rules
        self.bpe_cache = bpe_cache

    def split_seq(self, s):
        """
        Split the input into alphabet units.
        """
        t = sorted([a for a in self.alphabet if s.startswith(a)], key=lambda x: -len(x))[0]
        if len(t) < len(s):
            return [t] + self.split_seq(s[len(t):])
        else:
            return [t]

    def apply_merge_rule(self, merge_rule, bpe_seq):
        ret = []
        i = 0
        while i < len(bpe_seq) - 1:
            if merge_rule == (bpe_seq[i], bpe_seq[i+1]):
                ret.append(bpe_seq[i] + bpe_seq[i+1])
                i += 2
            else:
                ret.append(bpe_seq[i])
                i += 1
        if i == len(bpe_seq) - 1:
            ret.append(bpe_seq[i])
        return ret, Counter()

    def encode(self, s):
        """
        Encode the input string using BPE.
        """
        if s in self.bpe_cache:
            return self.bpe_cache[s]
        else:
            ret = self.split_seq(s)
            for mr in self.merge_rules:
                ret, _ = self.apply_merge_rule(mr, ret)
            self.bpe_cache[s] = ret
            return ret

    def token_mapping(self):
        tokens = self.alphabet + [a + b for a, b in self.merge_rules]
        return {tok: i for i, tok in enumerate(tokens)}


# WordPiece Tokenizer (simplified)
class WordPieceTokenizer:
    def __init__(self, vocab, unk_token='[UNK]'):
        self.vocab = vocab
        self.unk_token = unk_token

    def tokenize(self, word):
        """
        Tokenize the input word using WordPiece.
        """
        if word in self.vocab:
            return [word]
        tokens = []
        for i in range(len(word)):
            subword = word[:i+1]
            if subword in self.vocab:
                tokens.append(subword)
            else:
                tokens.append(self.unk_token)
        return tokens


# Step 2: Download and Preprocess Data
def download_and_preprocess_data():
    """
    Download the Wikipedia dataset and preprocess it.
    Students will run this function to get a few sentences for tokenization.
    """
    print("Downloading and preprocessing data...")

    # Hint: Use the load_dataset function and limit to 1000 sentences
    dataset = load_dataset("wikipedia", "20220301.en", split="train[0:1000]", trust_remote_code=True)

    # Hint: For each example, extract the first sentence by splitting on '.'
    sentences = [text.split('.') for text in dataset['text']][0][0:5]

    print("Sample sentences for tokenization:")
    for i, sentence in enumerate(sentences):
        print(f"{i+1}. {sentence}")

    return sentences


# Step 3: Tokenization Process and Comparison (students will fill in parts here)
def tokenization_demo(sentences):
    """
    Demo of BPE and WordPiece tokenization on preprocessed sentences.
    Students will run this function and compare the tokenized output.
    """

    # Hint: Use letters, special characters like '_t', and add tokens like [CLS], [SEP]
    alphabet = (["[CLS]", "[MASK]", "[SEP]", "[PAD]"] +
                [c for c in string.ascii_lowercase] +
                [f"_{c}" for c in string.ascii_lowercase])  # Preloaded example

    # Hint: Use common pairs of letters like ("h", "e") and ("_t", "he")
    merge_rules = [("h", "e"), ("_t", "he"), ("o", "r"), ("f", "or"), ("n", "d"), ("_a", "nd")]

    # Instantiate the BPE encoder
    bpe_encoder = BPEncoder(alphabet, merge_rules)

    # Define WordPiece vocab (students can leave this as is for the demo)
    wordpiece_vocab = ["un", "happiness", "hap", "##pi", "##ness", "[UNK]"]
    wp_tokenizer = WordPieceTokenizer(vocab=wordpiece_vocab)

    # Tokenize each sentence using both BPE and WordPiece
    print("\nTokenizing with BPE and WordPiece:\n")

    for sentence in sentences:
        print(f"Original sentence: {sentence}")

        # BPE Tokenization
        bpe_tokens = bpe_encoder.encode('_' + sentence.lower().replace(' ', '_'))
        tok2idx_bpe = bpe_encoder.token_mapping()
        bpe_numeric = [tok2idx_bpe[tok] for tok in bpe_tokens]

        print(f"BPE tokens: {bpe_tokens}")
        print(f"BPE numeric: {bpe_numeric}")

        # WordPiece Tokenization
        wp_tokens = wp_tokenizer.tokenize(sentence.lower())
        print(f"WordPiece tokens: {wp_tokens}")
        print("-" * 40)


# Step 4: Run the full process
if __name__ == "__main__":
    # Step 1: Download and preprocess data
    sentences = download_and_preprocess_data()

    # Step 2: Run the tokenization demo and compare outputs
    tokenization_demo(sentences)
