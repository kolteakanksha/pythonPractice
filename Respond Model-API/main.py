from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import sessionlocal
import model
import uvicorn

app = FastAPI()
db = sessionlocal()


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Person(OurBaseModel):
    id: int
    fname: str
    lname: str
    ismale: bool


@app.get('/', response_model=list[Person], status_code=status.HTTP_200_OK)
def getall_person():
    getallperson = db.query(model.person).all()
    return (getallperson)


@app.get('/getsingle/{person_id}', response_model=Person, status_code=status.HTTP_200_OK)
def get_single(person_id: int):
    getsingle = db.query(model.person).filter(model.person.id == person_id).first()
    return (getsingle)


@app.post('/addperson', response_model=Person, status_code=status.HTTP_201_CREATED)
def add_person(person: Person):
    addperson = model.person(
        id=person.id,
        fname=person.fname,
        lname=person.lname,
        ismale=person.ismale
    )
    find_person = db.query(model.person).filter(model.person.id == person.id).first()

    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Person with this ID Exists")

    db.add(addperson)
    db.commit()
    return addperson


@app.put('/update_person/{person_id}/', response_model=Person, status_code=status.HTTP_202_ACCEPTED)
def updateThePerson(person_id: int, person: Person):
    updatePerson = db.query(model.person).filter(model.person.id == person_id).first()
    updatePerson.id = person.id,
    updatePerson.fname = person.fname,
    updatePerson.lname = person.lname,
    updatePerson.ismale = person.ismale

    db.commit()
    return updatePerson


@app.delete('/deletePerson/{deli}', response_model=Person, status_code=status.HTTP_202_ACCEPTED)
def deletePerson(deli: int):
    find_person = db.query(model.person).filter(model.person.id == deli).first()
    if find_person is not None:
        db.delete(find_person)
        db.commit()
        return find_person
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail=" person deleted successfully")


    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=" person is not in table or already deleted")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)