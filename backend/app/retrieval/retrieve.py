# from .import bnq 
import app.main.retrieval.bnq as bnq
# import asyncio    

# async def retrieve_products_async(search):
#     return await asyncio.gather(bnq.retrieve(search))

def retrieve_products(search):
    # return asyncio.run(retrieve_products_async(search))
    # return [[(1, 'red paint', '$10', 'youtube.com', 'google.com', 0, 'homebase')]]
    return bnq.retrieve(search)
