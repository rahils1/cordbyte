from src.core.Database.Database import db

async def getModel(model_name):
    """
    Retrieve a database collection/model by name.

    Args:
        model_name (str): The name of the collection/model to retrieve.

    Returns:
        The database collection object if successful, else None.

    NOTE:
    This function assumes a MongoDB-like interface.
    Different databases or ORMs will have different methods for
    accessing models or tables, so adapt this function as needed.
    """
    try:
        model = db[model_name]
        return model
    except Exception:
        print("There was an error accessing the specified model")