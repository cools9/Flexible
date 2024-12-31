from fastapi import FastAPI

app = FastAPI()
toilets:str = ["Kaushik"]
yapping_section:str=[]
title:str = ["my-cat"]
aura:int = [10]
flex:str = ["[picture-of-my-cat]"]

@app.get("/")
async def display_flexes():
    flexs = list(zip(title, flex, aura))  # Generate fresh flexs for the response
    return {"top-100": flexs}

@app.get("/positive-aura/{title_name}")
async def like(title_name: str):
    if title_name in title:  # Check if title_name exists in title
        index = title.index(title_name)  # Get the index of the title_name
        aura[index] += 1
        return {"success": f"Thanks for the AURA"}
    else:
        return {"stoopid-failure": "Not possible moron"}

@app.get("/negative-aura/{title_name}")
async def like(title_name: str):
    if title_name in title:
        index = title.index(title_name)
        aura[index] -= 1
        return {"success": f"No Thanks For The aura"}
    else:
        return {"stoopid-failure": "Not possible moron"}

@app.get("/flex/{title_name}/{content}")
async def generate_brainrot(title_name:str,content:str):
    title.append(title_name)
    flex.append(content)
    aura.append(0)

@app.get("/busson/{bussinon}/{toilet}/{yap}"):
async def add_more_brainrot(bussinon,toilet,yap):
    yapping_section.append(bussinon,toilet,yap)
