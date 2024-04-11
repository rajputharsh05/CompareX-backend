from fastapi import APIRouter , Request , HTTPException , status
from app.database.db import connectDB
import bcrypt

router = APIRouter()

class MissingKeyError(Exception):
    pass

@router.post("/login")
async def handleLogin(request : Request):

    try:
        response = await request.json()
        loginID = response.get("loginID")
        loginPass = response.get("loginPass")

        collection = connectDB();
        document = collection.find({"leetcodeID" : loginID})


        for doc in document:
            password = doc["password"]
            res = bcrypt.checkpw(loginPass.encode(),password)
            print(res)
            if res:
                return {"message": "Login successful"}
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid details")  
                


    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error Something missing")     


@router.post("/register")
async def handleRegister(request : Request):
    try:
        response = await request.json()
        expected_keys = ["registerID" , "registerName" , "registerPass"]

        for key in expected_keys:
            if response.get(key) is "":
                raise MissingKeyError(f"Missing key '{key}' in request body")

        
        collection = connectDB();

        def create_user_document(name, password, leetcodeID, friends=[]):
            return {
                "name": name,
                "password": password,
                "leetcodeID": leetcodeID,
                "friends": friends
            }


        registerID = response.get("registerID")
        registerName = response.get("registerName")
        registerPass = response.get("registerPass")

   
        hasedpass = bcrypt.hashpw(registerPass.encode(),bcrypt.gensalt());
        
        user_document = create_user_document(registerName, hasedpass , registerID,)
        collection.insert_one(user_document)
        
        
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error Something missing")

        