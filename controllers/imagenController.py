# -*- coding: utf-8 -*-
# intente algo como
def index():
    images = db().select(db.image.ALL,orderby=db.image.title)
    return dict(images=images)


def show():
    image = db.image(request.args (0)) or redirect (URL('index'))
    db.comment.image_id.default = image.id
    form = crud.create(db.comment, 
                                message = 'your comment is posted',
                                next = URL(args=image.id))
    comments = db(db.comment.image_id==image.id).select()
    return dict (image=image, comments=comments, form=form)

def download():
    return response.download(request, db)
