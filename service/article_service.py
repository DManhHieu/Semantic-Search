from sentence_transformers import SentenceTransformer, util
from repository.article_repository import getArticleEmbbed,saveArticleEmbbed, deleteArticleEmbbed
from model.article_model import ArticleModel

def filterScore(score, point):
    if score['score'] <= point:
        return False
    return True

class ArticleService:
    def __init__(self,sentenceModel : SentenceTransformer):
        self.sentenceModel = sentenceModel

    def sentenceEncode(sefl, text):
        return sefl.sentenceModel.encode(text, convert_to_tensor=True)
    
    def encodeArticle(sefl, title, description):
        return sefl.sentenceEncode(sefl,title + "[SEP]" +  description)

    def compute_scores(self, text, embeddings,top_k):
        encode_value = self.sentenceEncode(self,text)
        return util.semantic_search(encode_value,embeddings,top_k=top_k)

    @classmethod
    def saveArticleEmbbed(self, article: ArticleModel):
        articleVector = self.encodeArticle(self,article.title, article.description)
        return saveArticleEmbbed(article.id,articleVector)
        
    @classmethod
    def search(self, text,minscore = 0.2,top_k = 10, tags=None):
        article_ids, embeded =  getArticleEmbbed(tags)
        scores = self.compute_scores(self,text, embeded,top_k)
        scores = scores[0]
        scores = filter(lambda x:  filterScore(x,minscore),scores)
        print([(score['corpus_id'], score['score'], article_ids[score['corpus_id']]) for score in scores])

    @classmethod
    def delete(id):
        deleteArticleEmbbed(id)