from datetime import date

from fastapi import HTTPException


async def validate_id_in_objects(objs, obj_id: int) -> None:
    for obj in objs:
        if obj.id == obj_id:
            break
    else:
        if objs:
            detail: str = f"Not Found [{obj.__class__.__name__} id: {obj_id}]"
        else:
            detail: str = f"No Data"
        raise HTTPException(status_code=404, detail=detail)


async def validate_period(open_date: date, due_date: date) -> None:
    if open_date > due_date:
        raise HTTPException(
            status_code=400, detail=f"due_date must be later than open_date"
        )
