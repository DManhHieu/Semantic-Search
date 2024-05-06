embbeds = []

def getArticleEmbbed(tags):
    return embbeds
def saveArticleEmbbed(id, embbed):
    embbeds.append((id,embbed))
    return id
def deleteArticleEmbbed(id):
    embbeds.remove(id)
    return True