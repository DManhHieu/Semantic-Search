# [SBert](https://sbert.net/)
Sentence-BERT (SBERT) is a BERT model modification that produces consistent and contextually rich sentence embeddings.

## SentenceTransformers
SentenceTransformers is a Python framework for state-of-the-art sentence, text and image embeddings.

## Cosine similarity
Cosine similarity is a measure of similarity between two non-zero vectors defined in an inner product space.

## Semantic Search

Embed all entries in the corpus:
- Title and description of the article into a vector space

At search time:
- The query is embedded into the same vector space
- Finds the closest embeddings. 
    - Compute the cosine-similarity between the query and all entries in the corpus
## Implement
- Import model
    ```python
        sentenceModel = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    ```
    - The all-mpnet-base-v2 model provides the best quality 
    https://sbert.net/docs/pretrained_models.html
    https://huggingface.co/models?library=sentence-transformers

    - The model will be automatically downloaded from huggingface and saved to the transformer library cache

    - Can use offline mode
- Encode article
    ```python
       sentenceModel.encode(title + "[SEP]" +  description, convert_to_tensor=True)
    ```
    - encode() Computes sentence embeddings
    - [SEP] token, short for “separator” in BERT serves as a separator between input segments, contributes to positional encoding to capture token positions accurately, and can also function as an end-of-sequence marker in certain contexts.
- Search
    ```python
        query_embedding = sentenceModel.encode(query,convert_to_tensor=True)
        score = sentence_transformers.util.cos_sim(query_embeddings, corpus_embedding)
    ```
    - Computes sentence embedding of query
    - Get all corpus embeddings from database, use util.cos_sim compute the score between query_embedding and corpus_embedding then can select top n or paging results.
    - https://sbert.net/docs/package_reference/util.html
    - Can use `sentence_transformers.util.semantic_search` but must load all record at a time