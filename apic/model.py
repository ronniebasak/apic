import streamlit as st

class ApicUI:
    dantic_model = None
    counters = {}
    list_values = {}

    def __init__(self, dantic_model):
        self.dantic_model = dantic_model


    def _field_render(self, field_name, field):
        def _add_list_item(field_name):
            def _add_list_item_inner():
                if field_name not in self.counters:
                    self.counters[field_name] = 1
                self.counters[field_name] += 1

                self.list_values[field_name].append(None)
                return None
            return _add_list_item_inner

        field_type = field.__origin__ if hasattr(field, '__origin__') else field

        if field_type is str:
            return st.text_input(field_name.capitalize())
        elif field_type is int:
            return st.number_input(field_name.capitalize(), step=1)
        elif field_type is float:
            return st.number_input(field_name.capitalize(), step=0.1)
        elif field_type is bool:
            return st.checkbox(field_name.capitalize())
        elif field_type is list:
            if field_name not in self.counters:
                self.counters[field_name] = 0

            if field_name not in self.list_values:
                self.list_values[field_name] = [None] * self.counters[field_name]
            
            for i in range(self.counters[field_name]):
                self.list_values[field_name][i] = st.text_input(field_name.capitalize() + ' ' + str(i))

            st.button('Add ' + field_name.capitalize(), on_click=_add_list_item(field_name))

            return self.list_values[field_name]
        else:
            return None


    def render(self):
        # inspect the model
        kv = {}
        for field_name, field in self.dantic_model.__annotations__.items():
            kv[field_name] = self._field_render(field_name, field)

        st.write(kv)
        p = self.dantic_model(**kv)
        return p