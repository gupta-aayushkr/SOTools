import streamlit as st

st.title('Excel Column Divider')
st.write('Paste your Excel column data below:')
column_data = st.text_area('Column Data')

if column_data:
    rows_in_column_data = len(column_data.split('\n'))
    st.write(f"Total rows in Column Data: {rows_in_column_data}")

divide_number = st.number_input("Enter the number of rows you want to divide by:", min_value=1, step=1, value=300)

if st.button('Divide Rows'):
    if column_data:
        values = column_data.split('\n')
        divided_values = [','.join(values[i:i+divide_number]) for i in range(0, len(values), divide_number)]
        st.write('Divided Rows:')
        idx = 1
        for row in divided_values:
            count = len(row.split(","))
            with st.expander(f'Divided Set {idx}: ({count} rows)', expanded=True):
                st.text_area(f'Divided Data {idx}', value=row, height=300)
            idx += 1
    else:
        st.warning('Please paste some data to divide.')


