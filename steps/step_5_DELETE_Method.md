## Delete Method
>
> As the name says, this will delete the data. Code for that are given billow
> 
```commandline
@app.delete("/val{_id}", tags=['VAL'])
async def delete_val(_id: int) -> dict:
    for val in values:
        if int(val['id']) == _id:
            values.remove(val)
            return {
                "data": f"id {_id} has been updated"
            }

    return {
        "data": f"id {_id} not Found"
    }
```
> This is how it looks like ...
> 
> [![DeleteMethod](../ss/ss24.PNG)](https://apparky.vercel.app/)
> 
> To Delete data follow the same ..
> 
> [![DeleteExecute](../ss/ss25.PNG)](https://apparky.vercel.app/)
> 
> `Curl` Code to Delete data ..
> 
> [![CurlDelete](../ss/ss27.PNG)](https://apparky.vercel.app/)
> 
> 
> 
> [Click](step_1_basic_API.md) Here to Start from [Beginning](step_1_basic_API.md) 
> 
> [Click](../README.md) Here to go to main [Overview](../README.md) Page 
> 
> We are done.
> 
> Thanks and regards [**Apparky**](https://apparky.vercel.app/)
> 
> 
> 
> [Click](../README.md) Here to go to main [Overview](../README.md) Page 