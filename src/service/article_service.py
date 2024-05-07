from sentence_transformers import SentenceTransformer, util
from repository.article_repository import semanticSearch, saveOrUpdate, delete
import os
from dto.search_response import SearchResponse, Score

def filterScore(score, point):
    if score['score'] <= point:
        return False
    return True

class ArticleService:

    model_name = os.getenv('SENTENCE_MODEL_NAME')
    sentenceModel = SentenceTransformer(model_name)

    def sentenceEncode(sefl, text):
        return sefl.sentenceModel.encode(text, convert_to_tensor=True)
    
    def encodeArticle(sefl, title, description):
        return sefl.sentenceEncode(title + "[SEP]" +  description)

    def compute_scores(self, text, embeddings,top_k):
        encode_value = self.sentenceEncode(text)
        return util.semantic_search(encode_value,embeddings,top_k=top_k)

    def saveArticleEmbedding(self, id, title, description , tags):
        embedding = self.encodeArticle(title, description)
        return saveOrUpdate(id,embedding, tags)
        
    def search(self, text,minscore,page, size, tags = None):
        results, total = semanticSearch(self.sentenceEncode(text),tags,minscore,page,size)
        return SearchResponse(
                            scores = [Score(score=result['score'],article_id=result['id']) for result in results],
                            page = page,
                            size = size,
                            total = total
            )

    def delete(self,id):
        return delete(id)