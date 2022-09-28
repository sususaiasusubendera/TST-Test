import json
from fastapi import FastAPI, HTTPException
with open("data-mahasiswa.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()
@app.get("/")
async def root():
    return {"Page": "Root"}

@app.get('/mahasiswa/{item}')
async def read_mahasiswa():
    dictMahasiswa = []
    for dataMahasiswa in data['data-mahasiswa']:
        dictMahasiswa.append(dataMahasiswa)
    return dictMahasiswa
    
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )
