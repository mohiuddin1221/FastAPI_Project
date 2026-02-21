from fastapi import HTTPException, status
from sqlalchemy import select, outerjoin
from sqlalchemy import func
from .models import Category, Product


def create_category_service(category, db, current_user):
    user = current_user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    new_category = Category(
        title=category.title, description=category.description, user=user
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
    total = current_user.total_categories

    return {"total": total, "categories": categories}


def create_product_service(product, db, current_user):
    try:
        user = current_user
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
            )
        print("user.......................", user)
        category_obj = (
            db.query(Category)
            .filter(Category.uid == product.category_id, Category.user_id == user.uid)
            .first()
        )
        print("category_obj.......................", category_obj)
        if not category_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
            )
        new_product = Product(
            title=product.title,
            description=product.description,
            price=product.price,
            stock=product.stock,
            category=category_obj,
            user=user,
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


def product_service(db, current_user):
    user = current_user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    products = db.query(Product).filter(Product.user_id == user.uid).all()
    total_products = current_user.total_products

    return {"total_products": total_products, "products": products}


def category_with_count_service(db, current_user):
    user = current_user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    results = (
        db.query(
            Category.uid, Category.title, func.count(Product.uid).label("product_count")
        )
        .where(Category.user_id == user.uid)
        .outerjoin(Product, Product.category_id == Category.uid)
        .group_by(Category.uid)
        .all()
    )


    return [
        {"uid": uid, "title": title, "product_count": count}
        for uid, title, count in results
    ]
