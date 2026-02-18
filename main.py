# main.py
from fastapi import FastAPI
from admin_setup import site
from src.auth.router import router as auth_router
from src.product.router import router as product_router


import src.auth.admin 
import src.product.admin

app = FastAPI()
app.include_router(auth_router)
app.include_router(product_router)
site.mount_app(app) 