ariticleEmbeddeds = []

def getArticleEmbedded(tags):
    ids = []
    embedded = []
    for (id,em) in ariticleEmbeddeds:
        ids.append(id)
        embedded.append(em)
    return ids,embedded
def saveArticleEmbedded(id, embeded):
    ariticleEmbeddeds.append((id,embeded))
    return id
def deleteArticleEmbedded(id):
    ariticleEmbeddeds.remove(id)
    return True