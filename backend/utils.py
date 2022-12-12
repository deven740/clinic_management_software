def commit_refresh(db, model):
    db.add(model)
    db.commit()
    db.refresh(model)