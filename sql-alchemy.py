from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from your_models_module import YourModel

# Create an SQLAlchemy engine and session
engine = create_engine('your_database_uri')
Session = sessionmaker(bind=engine)
session = Session()

# Perform an alphabetical ordering query
results = session.query(YourModel).order_by(YourModel.name).all()

# Process the results
for result in results:
    print(result.name)