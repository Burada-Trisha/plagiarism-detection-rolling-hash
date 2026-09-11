import re
import time

class RabinKarpPlagiarismDetector:
    """
    High-speed text plagiarism checker using Rabin-Karp rolling hash
    and n-gram fingerprinting with dual-modulus collision mitigation.
    """
    def __init__(self, k=5, base=256, mod1=1000000007, mod2=1000000009):
        self.k = k # n-gram length (words)
        self.base = base
        self.mod1 = mod1
        self.mod2 = mod2

    def tokenize(self, text):
        """Extracts cleaned lowercase word tokens."""
        clean_text = re.sub(r'[^\w\s]', '', text.lower())
        tokens = clean_text.split()
        return tokens

    def compute_hash_tuple(self, window_str):
        """Computes dual polynomial rolling hash to minimize collisions."""
        h1 = 0
        h2 = 0
        for ch in window_str:
            code = ord(ch)
            h1 = (h1 * self.base + code) % self.mod1
            h2 = (h2 * self.base + code) % self.mod2
        return (h1, h2)

    def extract_ngram_fingerprints(self, tokens):
        """Extracts n-grams and computes rolling hash fingerprints."""
        fingerprints = {}
        if len(tokens) < self.k:
            return fingerprints

        # Compute initial window string
        for i in range(len(tokens) - self.k + 1):
            ngram = " ".join(tokens[i:i + self.k])
            hash_val = self.compute_hash_tuple(ngram)
            if hash_val not in fingerprints:
                fingerprints[hash_val] = []
            fingerprints[hash_val].append(ngram)

        return fingerprints

    def check_plagiarism(self, doc_a, doc_b):
        """
        Detects plagiarized n-grams between doc_a and doc_b.
        Returns similarity percentage and matched passages.
        """
        start_time = time.perf_counter()
        
        tokens_a = self.tokenize(doc_a)
        tokens_b = self.tokenize(doc_b)

        if not tokens_a or not tokens_b:
            return {"similarity": 0.0, "matches": [], "time_ms": 0.0}

        fps_a = self.extract_ngram_fingerprints(tokens_a)
        fps_b = self.extract_ngram_fingerprints(tokens_b)

        # Intersection of hash fingerprints
        common_hashes = set(fps_a.keys()).intersection(set(fps_b.keys()))
        total_unique_hashes = set(fps_a.keys()).union(set(fps_b.keys()))

        # Jaccard similarity of n-gram fingerprints
        similarity_score = (len(common_hashes) / len(total_unique_hashes)) * 100 if total_unique_hashes else 0.0

        matching_snippets = []
        for h in list(common_hashes)[:10]:
            matching_snippets.append(fps_a[h][0])

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        return {
            "similarity_percent": round(similarity_score, 2),
            "common_ngrams_count": len(common_hashes),
            "total_ngrams_doc1": len(fps_a),
            "total_ngrams_doc2": len(fps_b),
            "matching_snippets": matching_snippets,
            "runtime_ms": round(elapsed_ms, 3)
        }

if __name__ == "__main__":
    detector = RabinKarpPlagiarismDetector(k=4)
    doc1 = "Data structures and algorithms form the fundamental building blocks of modern computer science and software development."
    doc2 = "Advanced data structures and algorithms form the fundamental building blocks of scalable modern systems."
    res = detector.check_plagiarism(doc1, doc2)
    print(f"Similarity: {res['similarity_percent']}% | Common N-Grams: {res['common_ngrams_count']} | Runtime: {res['runtime_ms']}ms")
