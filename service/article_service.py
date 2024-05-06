import os
from sentence_transformers import SentenceTransformer, util
from repository.article_repository import getArticleEmbbed,saveArticleEmbbed, deleteArticleEmbbed
from model.article_model import ArticleModel
from dotenv import load_dotenv

def filterScore(score, point):
    if score['score'] <= point:
        return False
    return True

class ArticleService:
    load_dotenv()

    def __init__(self):
        model_name = os.getenv('SENTENCE_MODEL_NAME')
        self.sentenceModel = SentenceTransformer(model_name)

    def sentenceEncode(sefl, text):
        return sefl.sentenceModel.encode(text, convert_to_tensor=True)
    
    def encodeArticle(sefl, title, description):
        return sefl.sentenceEncode(title + "[SEP]" +  description)

    def compute_scores(self, text, embeddings,top_k):
        encode_value = self.sentenceEncode(text)
        return util.semantic_search(encode_value,embeddings,top_k=top_k)

    @classmethod
    def saveArticleEmbbed(self, article: ArticleModel):
        articleVector = self.encodeArticle(article.title,article.description)
        return saveArticleEmbbed(article.id,articleVector)
        
    @classmethod
    def search(self, text,minscore = 0.2,top_k = 10, tags=None):
        article_ids, embeded =  getArticleEmbbed(tags)
        scores = self.compute_scores(text, embeded,top_k)
        scores = scores[0]
        scores = filter(lambda x:  filterScore(x,minscore),scores)
        print([(score['corpus_id'], score['score'], article_ids[score['corpus_id']]) for score in scores])

    @classmethod
    def delete(id):
        deleteArticleEmbbed(id)