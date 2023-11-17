from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.get("/")
async def user_get():
    """
    OAuth2 password flow login, get an access token for future requests
    """
    return {"Get user": True}


@router.post("/")
async def user_add(data: dict = Body()):
    """
    OAuth2 password flow login, get an access token for future requests
    """
    return {"Added User": data}


@router.delete("/")
async def delete():
    return {"delete": True}
