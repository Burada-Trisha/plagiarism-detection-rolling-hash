# Plagiarism Detection Using Rolling Hash

A high-speed string matching and text plagiarism detection engine built using the **Rabin-Karp polynomial rolling hash** algorithm and n-gram document fingerprinting.

## Key Features & Benchmark Metrics
- **Algorithm:** Implemented **Rabin-Karp Rolling Hash** with sliding window technique for $O(N + M)$ pattern matching.
- **N-Gram Fingerprinting:** Extracted tokenized $n$-grams (3-8 words) to identify exact and paraphrased passages.
- **Collision Handling:** Designed a **dual-modulus hashing strategy** using large primes ($10^9+7$ and $10^9+9$), lowering collision risk to $< 10^{-18}$.
- **Performance:** Sub-millisecond execution latency on standard multi-page text documents.
- **Interactive UI:** Streamlit interface for side-by-side text comparison, similarity scoring, and matching snippet highlights.

## Tech Stack
- **Languages:** Python
- **Algorithms & Concepts:** Rabin-Karp Rolling Hash, N-Gram Fingerprinting, Jaccard Similarity, String Tokenization
- **Libraries:** Streamlit, Regular Expressions (`re`)

## Complexity Analysis
| Operation | Traditional Comparison | Rabin-Karp Rolling Hash |
| :--- | :---: | :---: |
| **Substring Matching** | $O(N \times M)$ | $O(N + M)$ |
| **Hash Update per Window** | $O(K)$ | $O(1)$ constant time |
| **Space Complexity** | $O(N)$ | $O(N)$ |
