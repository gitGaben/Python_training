from fastapi import FastAPI
import os

app = FastAPI()

@app.post("/create-folder/")
def create_folder(folder_name: str = "NewFolder"):
    # Define the path for the new folder
    desktop_path = os.path.join(os.path.expanduser("~/Desktop"), folder_name)

    # Check if the folder already exists
    if not os.path.exists(desktop_path):
        # Create the folder
        os.makedirs(desktop_path)
        return {"message": f"Folder '{folder_name}' created on Desktop."}
    else:
        return {"message": f"Folder '{folder_name}' already exists on Desktop."}