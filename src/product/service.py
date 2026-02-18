from .models import Category
from fastapi import HTTPException, status

def create_category_service(category, db, current_user):
    user = current_user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    new_category = Category(
        title=category.title,
        description=category.description,
        user=user
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def category_service(db, current_user):
    user = current_user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    categories = db.query(Category).filter(Category.user_id == user.uid).all()
    total = db.query(Category).filter(Category.user_id == user.uid).count()

    return {
        "total": total,
        "categories": categories
    }