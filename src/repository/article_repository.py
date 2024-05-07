from pydantic import BaseModel
from config.database_connection import connection
import pickle
from sentence_transformers import util
from torch import Tensor
import json

insert_command = "INSERT INTO article (id, embedding, tags) VALUES (%s, %s,%s)"
delete_by_article_id = "DELETE FROM article WHERE id = %s "
article_query = "SELECT id, embedding, tags FROM article"
update_command = "UPDATE article SET embedding = %s , tags = %s WHERE id = %s "
check_exists = "SELECT id FROM article WHERE id = %s"
con = connection()

class SearchResponse(BaseModel):
    score: float
    article_id: int
def haveTags(queryTags,tags):
    if queryTags==None:
        return True
    if tags==None:
        return False
    tags = json.loads(tags)
    if len(set(queryTags).intersection(tags)) != 0:
        return True
    return False

def semanticSearch(query_embeddings : Tensor ,query_tags ,minscore, page, size):
    cur = con.cursor()
    cur.execute(article_query)
    queries_result = []
    row = cur.fetchone()
    while row is not None:
        id, embedding, tags = row            
        if(haveTags(query_tags,tags)):
            score = util.cos_sim(query_embeddings, pickle.loads(embedding))
            if(score>=minscore):
                queries_result.append({"id" : id, "score" : score})
        row = cur.fetchone()    
    sorted(queries_result, key=lambda x: x["score"], reverse=True)
    if page==None or size==None :
        return queries_result, len(queries_result)
    return queries_result[size*page:size*(page+1)], len(queries_result)

def checkExists(id):
    cur = con.cursor()
    cur.execute(check_exists,(id,))
    if cur.fetchone() == None:
        return False
    return True

def saveOrUpdate(id, embedding , tags):
    if checkExists(id):
        return update(id,embedding,tags)
    return save(id,embedding,tags)

def update(id, embedding , tags):
    cur = con.cursor()
    cur.execute(update_command,(pickle.dumps(embedding),json.dumps(tags),id))
    con.commit()
    return id

def save(id, embedding , tags):
    cur = con.cursor()
    cur.execute(insert_command,(id,pickle.dumps(embedding),json.dumps(tags)))
    con.commit()
    return id

def delete(id):
    cur = con.cursor()
    cur.execute(delete_by_article_id, (id,))
    con.commit()
    return True