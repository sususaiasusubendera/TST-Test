import json
from fastapi import FastAPI, HTTPException

with open("data-mahasiswa.json", "r") as read_file:
	data = json.load(read_file)
app = FastAPI()
@app.get('/data-mahasiswa/{item_NIM}')

async def read_data(item_NIM: int):
	for menu_item in data['menu']:
		if menu_item['id'] == item_id:
			return menu_item
	raise HTTPException(
		status_code=404, detail=f'Item not found'
	)
