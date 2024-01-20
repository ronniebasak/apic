from pydantic import BaseModel, field_validator
from apic.__dep_ui import ApicUI
import streamlit as st

class Shona(BaseModel):
    name: str
    age: int
    address: str
    is_employed: bool
    height: float
    hobbies: list = []

    @field_validator('age')
    def age_must_be_positive(cls, v):
        assert v > 0, 'age must be positive'
        return v




k = ApicUI(Shona).render()



def handle_submit():
    print('submitted', k.json())

btn = st.button('Submit', on_click=handle_submit)
# print(k)  