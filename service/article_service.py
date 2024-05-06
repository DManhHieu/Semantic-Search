from sentence_transformers import SentenceTransformer, util
from repository.article_repository import getArticleEmbedded,saveArticleEmbedded, deleteArticleEmbedded
import os
from dotenv import load_dotenv

load_dotenv()

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

    def saveArticleEmbedded(self, id, title, description):
        articleVector = self.encodeArticle(title, description)
        return saveArticleEmbedded(id,articleVector)
        
    def search(self, text,minscore = 0.2,top_k = 10, tags=None):
        article_ids, embeddeds =  getArticleEmbedded(tags)
        if len(embeddeds) == 0 :
            return None
        scores = self.compute_scores(text, embeddeds,top_k)
        scores = scores[0]
        scores = filter(lambda x:  filterScore(x,minscore),scores)
        return [{"score" : score['score'],"article_id" : article_ids[score['corpus_id']]} for score in scores]

    def delete(id):
        deleteArticleEmbedded(id)