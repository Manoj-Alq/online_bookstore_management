from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, Depends
from sqlalchemy.ext.declarative import declarative_base
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "postgresql://postgres:12345@localhost/online_bookstore_management"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

router = FastAPI(debug=True, title="Online bookstore management📚",openapi_extra={
        "swagger_ui": {
            "persistAuthorization": True,  # This option persists the authorization status
            "oauth": {
                "clientId": "your-client-id",  # Replace with your client ID
                "clientSecret": "your-client-secret",  # Replace with your client secret
                "appName": "Paadhukaapu",  # Customize the app name
            },
        },
    })




def get_session():
    session = sessionLocal()
    try:
        yield session
    finally:
        session.close()